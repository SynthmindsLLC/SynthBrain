"""The ingest pipeline: RawDoc -> chunks -> tags -> index. Source-agnostic.

Every adapter yields RawDocs; this module turns them into tagged MemoryChunks
and writes them to the index. Adding a new source = writing an adapter, never
touching this file.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Callable, Iterable

from .index import BrainIndex
from .schema import MemoryChunk
from .tag import classify_layer, tag_entities, tag_project

if TYPE_CHECKING:
    from .entities import EntityStore

ClassifyFn = Callable[[str], str]

# Flush accumulated chunks to the index in batches so a bulk run (tens of
# thousands of chunks) never holds the whole corpus in memory before writing.
FLUSH_EVERY = 256

# Cap on stored per-run error samples: enough to debug, small enough to log.
MAX_ERROR_SAMPLES = 10


@dataclass
class IngestStats:
    """Counters for one ingest run — what the ledger row and dry-run report show."""

    docs: int = 0
    chunks: int = 0
    errors: int = 0
    llm_classified: int = 0
    heuristic_classified: int = 0
    by_layer: dict[str, int] = field(default_factory=dict)
    by_project: dict[str, int] = field(default_factory=dict)
    by_source: dict[str, int] = field(default_factory=dict)
    error_samples: list[str] = field(default_factory=list)

    def record_error(self, sample: str) -> None:
        self.errors += 1
        if len(self.error_samples) < MAX_ERROR_SAMPLES:
            self.error_samples.append(sample)


@dataclass
class RawDoc:
    """What an adapter emits. The pipeline does the rest."""

    text: str
    source: str
    source_id: str
    url: str = ""
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    meta: dict[str, Any] = field(default_factory=dict)


_HEADER = re.compile(r"^(#{1,6})\s+(.*)$")


def header_aware_chunks(text: str, max_chars: int = 1800) -> list[str]:
    """Split on markdown headers, carrying the nearest header as context.
    Falls back to size-splitting any oversized section. Header-aware beats
    fixed-size by ~9% recall per the chunking studies cited in the research."""
    sections: list[str] = []
    current_header = ""
    buf: list[str] = []

    def flush() -> None:
        body = "\n".join(buf).strip()
        if body:
            prefix = f"{current_header}\n" if current_header else ""
            sections.append((prefix + body).strip())

    for line in text.splitlines():
        m = _HEADER.match(line)
        if m:
            flush()
            buf = []
            current_header = m.group(2).strip()
        else:
            buf.append(line)
    flush()

    # Size-split any section that blew past the budget.
    out: list[str] = []
    for s in sections:
        if len(s) <= max_chars:
            out.append(s)
        else:
            for i in range(0, len(s), max_chars):
                out.append(s[i : i + max_chars])
    return out or ([text.strip()] if text.strip() else [])


def _classify(piece: str, classify_fn: ClassifyFn | None, counter: dict[str, int]) -> str:
    """Errors from the LLM classifier fall back to the heuristic per-chunk so a
    single API hiccup doesn't kill the whole ingest run. Counts which path won
    into a per-doc counter — merged into run stats only if the whole doc
    chunks cleanly, so a mid-doc failure counts as one error, not N phantom
    classifications."""
    if classify_fn is None:
        counter["heuristic"] += 1
        return classify_layer(piece)
    try:
        layer = classify_fn(piece)
        counter["llm"] += 1
        return layer
    except Exception:
        counter["heuristic"] += 1
        return classify_layer(piece)


def _build_canon_map(entity_store: "EntityStore") -> dict[str, list[str]]:
    """One pass over the (small) entity graph: lower(name|alias) -> entity ids.

    Bulk corpora tag hundreds of thousands of mostly-unique capitalized
    spans; a per-name find_by_name() store scan turned canonicalization into
    the ingest bottleneck the moment the graph was seeded (observed: the
    70k-chunk vault run crawling at <256 chunks/min). Entities don't change
    mid-run, so one upfront load + O(1) dict lookups is both faster and
    semantically identical (case-insensitive exact name/alias match)."""
    canon: dict[str, list[str]] = {}
    for e in entity_store.all_entities():
        for label in (e.name, *e.aliases):
            key = str(label).strip().lower()
            if not key:
                continue
            ids = canon.setdefault(key, [])
            if e.id not in ids:
                ids.append(e.id)
    return canon


def _entity_tags(piece: str, canon: dict[str, list[str]] | None) -> list[str]:
    """B9: raw extracted names, plus any canonical graph ids they exact/alias
    match ('person:jeff-torres' style). Raw names are kept; ids are appended
    and deduped. No map (or an empty one) means raw names only — unchanged
    behavior."""
    names = tag_entities(piece)
    if not canon:
        return names
    tags = list(names)
    for name in names:
        for eid in canon.get(name.lower(), ()):
            if eid not in tags:
                tags.append(eid)
    return tags


def _chunk_doc(
    doc: RawDoc,
    classify_fn: ClassifyFn | None,
    stats: IngestStats,
    canon: dict[str, list[str]] | None = None,
) -> list[MemoryChunk]:
    counter = {"llm": 0, "heuristic": 0}
    chunks = [
        MemoryChunk(
            text=piece,
            source=doc.source,
            source_id=doc.source_id,
            url=doc.url,
            created_at=doc.created_at,
            project_tags=tag_project(piece),
            entity_tags=_entity_tags(piece, canon),
            layer=_classify(piece, classify_fn, counter),
            chunk_index=i,
        )
        for i, piece in enumerate(header_aware_chunks(doc.text))
    ]
    # Reached only when every chunk of the doc built cleanly.
    stats.llm_classified += counter["llm"]
    stats.heuristic_classified += counter["heuristic"]
    return chunks


def _emit_entities(doc: RawDoc, store: "EntityStore") -> None:
    """Meta -> graph. Adapters that know who was involved declare it in
    RawDoc.meta: an `attendees` name list and/or a `from`/`sender` string.
    Meeting-shaped docs (title + attendees) become an Event node with
    `attended` edges — the same shape the calendar adapter emits — so
    conversational sources (granola, emails, future zoom/teams) grow the
    dossier graph instead of only the chunk index. Upserts are
    merge-on-conflict, so repeat ingests are idempotent. Entities created
    here become canonicalization targets on the NEXT run (the canon map is
    built once per run)."""
    from email.utils import parseaddr

    from .entities import Edge, Entity

    meta = doc.meta or {}
    ref = f"{doc.source}:{doc.source_id}"
    people: list[Entity] = []
    for raw in meta.get("attendees") or []:
        name = str(raw).strip()
        if name:
            people.append(Entity(kind="person", name=name, source_refs=[ref]))
    for key in ("from", "sender"):
        raw = str(meta.get(key) or "").strip()
        if not raw:
            continue
        display, email = parseaddr(raw)
        name = (display or email or raw).strip()
        if not name:
            continue
        people.append(Entity(
            kind="person", name=name,
            aliases=[email] if email and email != name else [],
            attributes={"emails": [email]} if email else {},
            source_refs=[ref],
        ))
    if not people:
        return

    event: Entity | None = None
    title = str(meta.get("title") or "").strip()
    if title and meta.get("attendees"):
        event = Entity(
            kind="event", name=title,
            attributes={"date": doc.created_at.astimezone(timezone.utc).isoformat(),
                        "source": doc.source},
            source_refs=[ref],
        )
        store.upsert_entity(event)
    for p in people:
        store.upsert_entity(p)
        if event is not None:
            store.add_edge(Edge(src=p.id, rel="attended", dst=event.id,
                                attributes={"via": doc.source}))


def ingest(
    index: BrainIndex,
    docs: Iterable[RawDoc],
    *,
    classify_fn: ClassifyFn | None = None,
    dry_run: bool = False,
    stats: IngestStats | None = None,
    entity_store: "EntityStore | None" = None,
) -> int:
    """`classify_fn` overrides the layer classifier (e.g. for the LLM path).

    Per-doc error isolation: one doc whose chunking/tagging blows up is counted
    and sampled, not fatal — the rest of the run continues. Chunks flush to the
    index every FLUSH_EVERY so bulk runs stream instead of accumulating.
    `dry_run` runs the full chunk+tag pass but writes nothing. Pass an
    IngestStats to collect per-run counters (ledger row / dry-run report).
    Pass an `entity_store` to canonicalize extracted entity names against the
    graph (B9) — omitted or empty, entity_tags are unchanged.
    Returns the total chunk count either way."""
    st = stats if stats is not None else IngestStats()
    # One upfront graph load instead of a store scan per unique name — see
    # _build_canon_map for why (bulk-ingest bottleneck).
    canon = _build_canon_map(entity_store) if entity_store is not None else None
    pending: list[MemoryChunk] = []
    for doc in docs:
        try:
            doc_chunks = _chunk_doc(doc, classify_fn, st, canon)
        except Exception as exc:
            src = f"{getattr(doc, 'source', '?')}:{getattr(doc, 'source_id', '?')}"
            st.record_error(f"{src}: {type(exc).__name__}: {exc}")
            continue
        st.docs += 1
        if entity_store is not None and not dry_run:
            try:
                _emit_entities(doc, entity_store)
            except Exception as exc:
                # A failed graph emit must not void the doc's chunks.
                src = f"{getattr(doc, 'source', '?')}:{getattr(doc, 'source_id', '?')}"
                st.record_error(f"{src}: entity-emit {type(exc).__name__}: {exc}")
        for c in doc_chunks:
            st.chunks += 1
            st.by_layer[c.layer] = st.by_layer.get(c.layer, 0) + 1
            st.by_source[c.source] = st.by_source.get(c.source, 0) + 1
            for p in c.project_tags:
                st.by_project[p] = st.by_project.get(p, 0) + 1
            pending.append(c)
            if len(pending) >= FLUSH_EVERY and not dry_run:
                index.add_chunks(pending)
                pending = []
    if pending and not dry_run:
        index.add_chunks(pending)
    return st.chunks
