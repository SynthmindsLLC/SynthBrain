"""The ingest pipeline: RawDoc -> chunks -> tags -> index. Source-agnostic.

Every adapter yields RawDocs; this module turns them into tagged MemoryChunks
and writes them to the index. Adding a new source = writing an adapter, never
touching this file.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Iterable

from .index import BrainIndex
from .schema import MemoryChunk
from .tag import classify_layer, tag_entities, tag_project

ClassifyFn = Callable[[str], str]


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


def ingest(
    index: BrainIndex,
    docs: Iterable[RawDoc],
    *,
    classify_fn: ClassifyFn | None = None,
) -> int:
    """`classify_fn` overrides the layer classifier (e.g. for the LLM path).
    Errors from the LLM classifier fall back to the heuristic per-chunk so a
    single API hiccup doesn't kill the whole ingest run."""
    fn = classify_fn or classify_layer
    chunks: list[MemoryChunk] = []
    for doc in docs:
        for i, piece in enumerate(header_aware_chunks(doc.text)):
            try:
                layer = fn(piece)
            except Exception:
                layer = classify_layer(piece)
            chunks.append(
                MemoryChunk(
                    text=piece,
                    source=doc.source,
                    source_id=doc.source_id,
                    url=doc.url,
                    created_at=doc.created_at,
                    project_tags=tag_project(piece),
                    entity_tags=tag_entities(piece),
                    layer=layer,
                    chunk_index=i,
                )
            )
    return index.add_chunks(chunks)
