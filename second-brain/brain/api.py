"""Brain HTTP API — the retrieval surface other clients call.

Speaks JSON over HTTP. apps/web (Phase 3) and the glasses companion
(Phase 4) both consume this; the Python brain on disk is the source of truth.

Routes:
  GET  /healthz                              service liveness
  GET  /stats                                index + graph sizes
  POST /resolve   {mention, context, kind}   context-aware entity resolution
  POST /dossier   {mention, event, context}  the popup card (no LLM by default)
  GET  /who/{name}                           graph traversal (events + co-attendees)
  POST /query     {text, k, layer, project}  semantic search over chunks
  GET  /graph     ?limit=N                   nodes + edges (for the 3D viz)
  POST /ingest-text {text, source, source_id} adhoc single-doc ingest

Auth model: localhost-only by default. Set BRAIN_BEARER_TOKEN to require
`Authorization: Bearer <token>` on every non-healthz request (LAN serving).

Run:
  uvicorn brain.api:app --reload --port 8088
  curl localhost:8088/healthz
"""

from __future__ import annotations

import os
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from .core.dossier import dossier
from .core.embed import get_embedder
from .core.entities import EntityStore
from .core.index import BrainIndex
from .core.pipeline import RawDoc, ingest
from .core.resolve import Status, resolve
from .core.salience import build_idf, filter_by_salience, score_chunk

DEFAULT_DB = os.environ.get("BRAIN_DB", "./brain_index")
DEFAULT_ENTDB = os.environ.get("BRAIN_ENTDB", "./entities.db")
DEFAULT_EMBEDDER = os.environ.get("BRAIN_EMBEDDER", "fake")
BEARER_TOKEN = os.environ.get("BRAIN_BEARER_TOKEN", "")


app = FastAPI(title="SynthBrain", version="0.2.0")


# --- stores cached on the app -----------------------------------------------

def _index() -> BrainIndex:
    cached = getattr(app.state, "_index", None)
    if cached is None:
        cached = BrainIndex(DEFAULT_DB, get_embedder(DEFAULT_EMBEDDER))
        app.state._index = cached
    return cached


def _store() -> EntityStore:
    cached = getattr(app.state, "_store", None)
    if cached is None:
        cached = EntityStore(DEFAULT_ENTDB)
        app.state._store = cached
    return cached


def _require_auth(request: Request) -> None:
    if not BEARER_TOKEN:
        return
    auth = request.headers.get("authorization", "")
    if not auth.startswith("Bearer "):
        raise HTTPException(401, "missing bearer token")
    if auth.removeprefix("Bearer ").strip() != BEARER_TOKEN:
        raise HTTPException(403, "invalid bearer token")


# --- request / response models ----------------------------------------------

class ResolveBody(BaseModel):
    mention: str
    context: str = ""
    kind: str = "person"


class DossierBody(BaseModel):
    mention: str
    event: str = ""
    context: str = ""
    use_chunks: bool = True
    k: int = 6


class QueryBody(BaseModel):
    text: str
    k: int = Field(default=5, ge=1, le=50)
    layer: str | None = None
    project: str | None = None
    salience: bool = False             # add salience score per result
    salience_threshold: float = 0.0   # if >0, drop rows below this score


class IngestTextBody(BaseModel):
    text: str
    source: str = "api"
    source_id: str


# --- routes -----------------------------------------------------------------

@app.get("/healthz")
def healthz() -> dict:
    return {"ok": True}


@app.get("/stats", dependencies=[Depends(_require_auth)])
def stats() -> dict:
    return {
        "chunks": _index().count(),
        "graph": _store().counts(),
        "db": DEFAULT_DB,
        "entdb": DEFAULT_ENTDB,
        "embedder": DEFAULT_EMBEDDER,
    }


@app.post("/resolve", dependencies=[Depends(_require_auth)])
def post_resolve(body: ResolveBody) -> dict:
    r = resolve(_store(), body.mention, body.context, body.kind)
    return {
        "status": r.status.value,
        "confidence": r.confidence,
        "rationale": r.rationale,
        "entity": _entity_dict(r.entity) if r.entity else None,
        "candidates": [_entity_dict(c) for c in r.candidates],
        "scores": [{"id": eid, "score": s} for eid, s in r.scores],
    }


@app.post("/dossier", dependencies=[Depends(_require_auth)])
def post_dossier(body: DossierBody) -> dict:
    index = _index() if body.use_chunks else None
    card = dossier(
        _store(),
        index,
        body.mention,
        event_hint=body.event,
        context=body.context,
        chunk_k=body.k,
    )
    return {
        "name": card.name,
        "role": card.role,
        "relationship": card.relationship,
        "where_met": card.where_met,
        "discussed": card.discussed,
        "confidence": card.confidence,
        "needs_disambiguation": card.needs_disambiguation,
        "rationale": card.rationale,
    }


@app.get("/who/{name}", dependencies=[Depends(_require_auth)])
def get_who(name: str) -> dict:
    store = _store()
    matches = store.find_by_name(name, "person")
    if not matches:
        return {"name": name, "matches": []}
    out = []
    for person in matches:
        events = []
        for _edge, ev in store.neighbors(person.id, "attended"):
            if not ev:
                continue
            others = [
                e.name for _, e in _co_attendees(store, ev.id)
                if e and e.id != person.id
            ]
            events.append({
                "id": ev.id,
                "name": ev.name,
                "date": ev.attributes.get("date", ""),
                "location": ev.attributes.get("location", ""),
                "co_attendees": others,
            })
        out.append({**_entity_dict(person), "events": events})
    return {"name": name, "matches": out}


@app.post("/query", dependencies=[Depends(_require_auth)])
def post_query(body: QueryBody) -> dict:
    rows = _index().query(body.text, k=body.k, layer=body.layer, project=body.project)
    out = []
    idf = _idf_cache(rows) if (body.salience or body.salience_threshold > 0) else None
    ctx_tokens = _ctx_tokens(body.text) if (body.salience or body.salience_threshold > 0) else None
    for r in rows:
        dist = r.get("_distance")
        row: dict = {
            "text": r.get("text", ""),
            "source": r.get("source", ""),
            "source_id": r.get("source_id", ""),
            "url": r.get("url", ""),
            "layer": r.get("layer", ""),
            "project_tags": r.get("project_tags", []) or [],
            "entity_tags": r.get("entity_tags", []) or [],
            "score": (1.0 - dist) if dist is not None else None,
        }
        if body.salience or body.salience_threshold > 0:
            s = score_chunk(r, idf=idf, context_tokens=ctx_tokens)
            row["salience"] = {
                "total": s.total, "tfidf": s.tfidf, "recency": s.recency,
                "entity": s.entity, "layer_score": s.layer, "context": s.context,
            }
            if body.salience_threshold > 0 and s.total < body.salience_threshold:
                continue
        out.append(row)
    return {"text": body.text, "results": out}


def _idf_cache(rows: list[dict]) -> dict[str, float]:
    cached = getattr(app.state, "_idf", None)
    if cached is None:
        cached = build_idf(r.get("text", "") for r in rows)
        app.state._idf = cached
    return cached


def _ctx_tokens(text: str) -> set[str]:
    import re
    return {m.group(0) for m in re.finditer(r"[a-z0-9][a-z0-9'\-]+", text.lower())}


@app.get("/graph", dependencies=[Depends(_require_auth)])
def get_graph(limit: int = 500) -> dict:
    store = _store()
    nodes = []
    seen: set[str] = set()
    for e in store.all_entities():
        if len(nodes) >= limit:
            break
        nodes.append({
            "id": e.id,
            "name": e.name,
            "kind": e.kind,
            "label": e.name,
        })
        seen.add(e.id)
    rows = store._db.execute(  # noqa: SLF001 - read-only export
        "SELECT src, rel, dst FROM edges"
    ).fetchall()
    links = [
        {"source": r["src"], "target": r["dst"], "rel": r["rel"]}
        for r in rows
        if r["src"] in seen and r["dst"] in seen
    ]
    return {"nodes": nodes, "links": links}


@app.post("/ingest-text", dependencies=[Depends(_require_auth)])
def post_ingest_text(body: IngestTextBody) -> dict:
    doc = RawDoc(text=body.text, source=body.source, source_id=body.source_id)
    n = ingest(_index(), [doc])
    return {"ingested": n}


# --- helpers ----------------------------------------------------------------

def _entity_dict(e) -> dict[str, Any]:
    return {
        "id": e.id,
        "kind": e.kind,
        "name": e.name,
        "aliases": e.aliases,
        "attributes": e.attributes,
    }


def _co_attendees(store: EntityStore, event_id: str):
    rows = store._db.execute(  # noqa: SLF001
        "SELECT src FROM edges WHERE rel='attended' AND dst=?", (event_id,)
    ).fetchall()
    return [(None, store.get_entity(r["src"])) for r in rows]
