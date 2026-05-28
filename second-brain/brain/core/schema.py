"""The common record every source normalizes into: the MemoryChunk.

This is the single contract the whole second brain is built around. Every
adapter (Drive, M365, Granola, Claude, ChatGPT, Fieldy, the hard drive, and
eventually the G2 mic) produces these and nothing else. The index, the tagger,
and the retrieval surface all speak MemoryChunk. Change this carefully.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any

import pyarrow as pa

# The Context-Graph layer (Klarity framing). Pass-2 tagging classifies into one
# of these. "artifact" is the cheap default; the other three are the high-value
# tribal-knowledge layer that makes recall worth surfacing on the glasses.
LAYERS = ("artifact", "decision", "reasoning", "workaround")


@dataclass
class MemoryChunk:
    """One retrievable unit of memory. ~300-500 tokens of text + provenance + tags."""

    text: str
    source: str                     # adapter name, e.g. "mem", "drive", "granola"
    source_id: str                  # stable id within that source (note id, file id, msg id)
    url: str = ""                   # deep link back to the original, if any
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    project_tags: list[str] = field(default_factory=list)   # pass-1: #project/* wings
    entity_tags: list[str] = field(default_factory=list)    # pass-1: people/orgs/products
    layer: str = "artifact"                                  # pass-2: see LAYERS
    chunk_index: int = 0            # position within the source doc (0-based)
    id: str = ""                    # deterministic; derived if left blank

    def __post_init__(self) -> None:
        if self.layer not in LAYERS:
            raise ValueError(f"layer must be one of {LAYERS}, got {self.layer!r}")
        if not self.id:
            self.id = self._derive_id()

    def _derive_id(self) -> str:
        # Deterministic so re-ingesting the same source chunk overwrites rather
        # than duplicates. Source + source_id + chunk position is the natural key.
        raw = f"{self.source}:{self.source_id}:{self.chunk_index}"
        return hashlib.sha1(raw.encode("utf-8")).hexdigest()

    def to_row(self, embedding: list[float]) -> dict[str, Any]:
        d = asdict(self)
        d["created_at"] = self.created_at.astimezone(timezone.utc).isoformat()
        d["embedding"] = embedding
        return d


def arrow_schema(embedding_dim: int) -> pa.Schema:
    """LanceDB table schema. embedding_dim is set by the active embedder."""
    return pa.schema(
        [
            pa.field("id", pa.string()),
            pa.field("text", pa.string()),
            pa.field("source", pa.string()),
            pa.field("source_id", pa.string()),
            pa.field("url", pa.string()),
            pa.field("created_at", pa.string()),
            pa.field("project_tags", pa.list_(pa.string())),
            pa.field("entity_tags", pa.list_(pa.string())),
            pa.field("layer", pa.string()),
            pa.field("chunk_index", pa.int32()),
            pa.field("embedding", pa.list_(pa.float32(), embedding_dim)),
        ]
    )
