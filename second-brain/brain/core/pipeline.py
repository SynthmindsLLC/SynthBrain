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


def _classify(piece: str, classify_fn: ClassifyFn | None, stats: IngestStats) -> str:
    """Errors from the LLM classifier fall back to the heuristic per-chunk so a
    single API hiccup doesn't kill the whole ingest run. Counts which path won
    so classification quality is measurable per run."""
    if classify_fn is None:
        stats.heuristic_classified += 1
        return classify_layer(piece)
    try:
        layer = classify_fn(piece)
        stats.llm_classified += 1
        return layer
    except Exception:
        stats.heuristic_classified += 1
        return classify_layer(piece)


def _entity_tags(
    piece: str,
    entity_store: "EntityStore | None",
    canon_cache: dict[str, list[str]],
) -> list[str]:
    """B9: raw extracted names, plus any canonical graph ids they exact/alias
    match ('person:jeff-torres' style). Raw names are kept; ids are appended
    and deduped. No store (or an empty one) means raw names only — unchanged
    behavior. `canon_cache` memoizes name -> ids per ingest run so bulk runs
    don't rescan the entities table for every repeated name."""
    names = tag_entities(piece)
    if entity_store is None:
        return names
    tags = list(names)
    for name in names:
        key = name.lower()
        ids = canon_cache.get(key)
        if ids is None:
            ids = [e.id for e in entity_store.find_by_name(name)]
            canon_cache[key] = ids
        for eid in ids:
            if eid not in tags:
                tags.append(eid)
    return tags


def _chunk_doc(
    doc: RawDoc,
    classify_fn: ClassifyFn | None,
    stats: IngestStats,
    entity_store: "EntityStore | None" = None,
    canon_cache: dict[str, list[str]] | None = None,
) -> list[MemoryChunk]:
    return [
        MemoryChunk(
            text=piece,
            source=doc.source,
            source_id=doc.source_id,
            url=doc.url,
            created_at=doc.created_at,
            project_tags=tag_project(piece),
            entity_tags=_entity_tags(piece, entity_store, canon_cache if canon_cache is not None else {}),
            layer=_classify(piece, classify_fn, stats),
            chunk_index=i,
        )
        for i, piece in enumerate(header_aware_chunks(doc.text))
    ]


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
    canon_cache: dict[str, list[str]] = {}
    pending: list[MemoryChunk] = []
    for doc in docs:
        try:
            doc_chunks = _chunk_doc(doc, classify_fn, st, entity_store, canon_cache)
        except Exception as exc:
            src = f"{getattr(doc, 'source', '?')}:{getattr(doc, 'source_id', '?')}"
            st.record_error(f"{src}: {type(exc).__name__}: {exc}")
            continue
        st.docs += 1
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
