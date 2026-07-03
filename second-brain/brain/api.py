"""Brain HTTP API — the retrieval surface other clients call.

Speaks JSON over HTTP. apps/web (Phase 3) and the glasses companion
(Phase 4) both consume this; the Python brain on disk is the source of truth.

Routes:
  GET  /healthz                              service liveness
  GET  /stats                                index + graph sizes
  GET  /stats/breakdown                      dashboard rollups (30s cache)
  GET  /ingest/runs   ?limit=N               ingest ledger, newest-first
  GET  /chunks/recent ?limit=&source=&layer= latest indexed chunks
  POST /resolve   {mention, context, kind}   context-aware entity resolution
  POST /dossier   {mention, event, context}  the popup card (no LLM by default)
  GET  /who/{name}                           graph traversal (events + co-attendees)
  POST /query     {text, k, layer, project}  semantic search over chunks
  GET  /graph     ?limit=&kind=&min_degree=  top-degree nodes + edges (3D viz)
  POST /ingest-text {text, source, source_id} adhoc single-doc ingest

Auth model: localhost-only by default. Set BRAIN_BEARER_TOKEN to require
`Authorization: Bearer <token>` on every non-healthz request (LAN serving).

Run:
  uvicorn brain.api:app --reload --port 8088
  curl localhost:8088/healthz
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timezone
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Query, Request
from pydantic import BaseModel, Field, field_validator

from .core.dossier import dossier
from .core.embed import get_embedder
from .core.entities import KINDS, EntityStore
from .core.index import BrainIndex
from .core.ledger import IngestLedger
from .core.pipeline import RawDoc, ingest
from .core.resolve import Status, resolve
from .core.salience import build_idf, filter_by_salience, score_chunk
from .core.schema import LAYERS

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


def _ledger() -> IngestLedger:
    cached = getattr(app.state, "_ledger", None)
    if cached is None:
        cached = IngestLedger(DEFAULT_ENTDB)
        app.state._ledger = cached
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

    @field_validator("layer")
    @classmethod
    def _layer_in_schema(cls, v: str | None) -> str | None:
        if v is not None and v not in LAYERS:
            raise ValueError(f"layer must be one of {LAYERS}")
        return v

    @field_validator("project")
    @classmethod
    def _project_no_quotes(cls, v: str | None) -> str | None:
        # project is interpolated into the LanceDB filter string; quotes are
        # rejected at the boundary rather than escaped downstream.
        if v is not None and ("'" in v or '"' in v):
            raise ValueError("project must not contain quote characters")
        return v


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


# In-process cache for /stats/breakdown: the dashboard polls every few seconds
# but a full-column scan of a bulk index is not free. Busted on /ingest-text.
BREAKDOWN_CACHE_TTL = 30.0
_breakdown_cache: dict[str, Any] = {"at": 0.0, "data": None}


def _bust_breakdown_cache() -> None:
    _breakdown_cache["data"] = None


@app.get("/stats/breakdown", dependencies=[Depends(_require_auth)])
def get_stats_breakdown() -> dict:
    now = time.monotonic()
    if (
        _breakdown_cache["data"] is not None
        and now - _breakdown_cache["at"] < BREAKDOWN_CACHE_TTL
    ):
        return _breakdown_cache["data"]
    data = _compute_breakdown()
    _breakdown_cache["at"] = now
    _breakdown_cache["data"] = data
    return data


def _compute_breakdown() -> dict:
    tbl = _index().scan(["source", "layer", "project_tags", "created_at"])
    by_source: dict[str, int] = {}
    by_layer: dict[str, int] = {}
    by_project: dict[str, int] = {}
    by_day: dict[str, int] = {}
    for source, layer, projects, created in zip(
        tbl["source"].to_pylist(),
        tbl["layer"].to_pylist(),
        tbl["project_tags"].to_pylist(),
        tbl["created_at"].to_pylist(),
    ):
        by_source[source] = by_source.get(source, 0) + 1
        by_layer[layer] = by_layer.get(layer, 0) + 1
        for p in projects or []:
            by_project[p] = by_project.get(p, 0) + 1
        day = (created or "")[:10]
        if day:
            by_day[day] = by_day.get(day, 0) + 1
    store = _store()
    with store._lock:  # noqa: SLF001 - raw read shares the store's connection
        ent_rows = store._db.execute(  # noqa: SLF001 - read-only rollup
            "SELECT kind, COUNT(*) c FROM entities GROUP BY kind"
        ).fetchall()
        edge_rows = store._db.execute(  # noqa: SLF001 - read-only rollup
            "SELECT rel, COUNT(*) c FROM edges GROUP BY rel"
        ).fetchall()
    by_kind = {r["kind"]: r["c"] for r in ent_rows}
    by_rel = {r["rel"]: r["c"] for r in edge_rows}
    return {
        "chunks_total": tbl.num_rows,
        "by_source": by_source,
        "by_layer": by_layer,
        "by_project": by_project,
        "by_day": [{"date": d, "chunks": c} for d, c in sorted(by_day.items())],
        "entities": {"total": sum(by_kind.values()), "by_kind": by_kind},
        "edges": {"total": sum(by_rel.values()), "by_rel": by_rel},
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/ingest/runs", dependencies=[Depends(_require_auth)])
def get_ingest_runs(limit: int = Query(default=50, ge=1, le=500)) -> dict:
    return {"runs": _ledger().runs(limit=limit)}


RECENT_TEXT_CHARS = 400


@app.get("/chunks/recent", dependencies=[Depends(_require_auth)])
def get_chunks_recent(
    limit: int = Query(default=20, ge=1, le=100),
    source: str | None = None,
    layer: str | None = None,
) -> dict:
    if layer is not None and layer not in LAYERS:
        raise HTTPException(422, f"layer must be one of {LAYERS}")
    rows = _index().scan(
        ["id", "text", "source", "source_id", "url", "layer",
         "project_tags", "entity_tags", "created_at"]
    ).to_pylist()
    # Source/layer are compared literally in Python — nothing is interpolated
    # into a LanceDB filter string, so arbitrary values are safe here.
    if source is not None:
        rows = [r for r in rows if r["source"] == source]
    if layer is not None:
        rows = [r for r in rows if r["layer"] == layer]
    rows.sort(key=lambda r: r["created_at"] or "", reverse=True)
    out = []
    for r in rows[:limit]:
        text = r["text"] or ""
        if len(text) > RECENT_TEXT_CHARS:
            text = text[:RECENT_TEXT_CHARS] + "…"
        out.append({
            "id": r["id"],
            "text": text,
            "source": r["source"],
            "source_id": r["source_id"],
            "url": r["url"],
            "layer": r["layer"],
            "project_tags": r["project_tags"] or [],
            "entity_tags": r["entity_tags"] or [],
            "created_at": r["created_at"],
        })
    return {"chunks": out}


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


def _parse_kinds(kind: str | None) -> set[str] | None:
    if not kind:
        return None
    kinds = {t.strip() for t in kind.split(",") if t.strip()}
    bad = kinds - set(KINDS)
    if bad:
        raise HTTPException(422, f"kind must be a CSV of {KINDS}")
    return kinds or None


@app.get("/graph", dependencies=[Depends(_require_auth)])
def get_graph(
    limit: int = Query(default=500, ge=1, le=2000),
    kind: str | None = None,
    min_degree: int = Query(default=0, ge=0),
) -> dict:
    """Top-N nodes by degree (stable id tiebreak) — a bulk graph should show
    its hubs, not whatever happened to insert first. Degree is computed over
    the FULL edge set before any kind/min_degree filtering, so a filtered
    node's degree still reflects its real connectivity."""
    kinds = _parse_kinds(kind)
    store = _store()
    with store._lock:  # noqa: SLF001 - raw read shares the store's connection
        rows = store._db.execute(  # noqa: SLF001 - read-only export
            "SELECT src, rel, dst FROM edges"
        ).fetchall()
    edges = [(r["src"], r["rel"], r["dst"]) for r in rows]
    degree: dict[str, int] = {}
    for src, _rel, dst in edges:
        degree[src] = degree.get(src, 0) + 1
        degree[dst] = degree.get(dst, 0) + 1
    candidates = [
        e for e in store.all_entities()
        if (kinds is None or e.kind in kinds)
        and degree.get(e.id, 0) >= min_degree
    ]
    candidates.sort(key=lambda e: (-degree.get(e.id, 0), e.id))
    picked = candidates[:limit]
    seen = {e.id for e in picked}
    nodes = [
        {
            "id": e.id,
            "name": e.name,
            "kind": e.kind,
            "label": e.name,
            "degree": degree.get(e.id, 0),
        }
        for e in picked
    ]
    links = [
        {"source": src, "target": dst, "rel": rel}
        for src, rel, dst in edges
        if src in seen and dst in seen
    ]
    return {"nodes": nodes, "links": links}


@app.post("/ingest-text", dependencies=[Depends(_require_auth)])
def post_ingest_text(body: IngestTextBody) -> dict:
    doc = RawDoc(text=body.text, source=body.source, source_id=body.source_id)
    n = ingest(_index(), [doc])
    _bust_breakdown_cache()
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
    with store._lock:  # noqa: SLF001 - raw read shares the store's connection
        rows = store._db.execute(  # noqa: SLF001
            "SELECT src FROM edges WHERE rel='attended' AND dst=?", (event_id,)
        ).fetchall()
        return [(None, store.get_entity(r["src"])) for r in rows]
