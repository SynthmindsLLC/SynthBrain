"""Mem adapter — the first source, because the data is already clean.

Two intake modes, per the research's recommended sync pattern:
  1. SEED (implemented): parse a Mem Markdown export — a directory of .md files,
     one note per file. This is how you bootstrap the brain.
  2. INCREMENTAL (stubbed): poll GET /v2/notes?order_by=updated_at and re-ingest
     changed notes. Mem exposes no webhooks/since-filter, so polling is the path.
     Wire this in Phase 3.

Run the seed mode first: export your Mem workspace (Settings -> Export), unzip
into ./sample_mem_export/ (or point --source at it), and ingest.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from ..core.pipeline import RawDoc
from .base import Adapter


class MemAdapter(Adapter):
    name = "mem"

    def __init__(self, source_dir: str) -> None:
        self.source_dir = Path(source_dir)

    def fetch(self) -> Iterable[RawDoc]:
        if not self.source_dir.exists():
            raise FileNotFoundError(
                f"Mem export dir not found: {self.source_dir}. "
                "Export your workspace from Mem (Settings -> Export) and unzip here."
            )
        for md in sorted(self.source_dir.rglob("*.md")):
            text = md.read_text(encoding="utf-8", errors="replace").strip()
            if not text:
                continue
            ts = datetime.fromtimestamp(md.stat().st_mtime, tz=timezone.utc)
            yield RawDoc(
                text=text,
                source=self.name,
                source_id=md.stem,             # filename = stable id within Mem export
                url="",                         # Mem export doesn't carry note URLs
                created_at=ts,
                meta={"path": str(md)},
            )


class MemApiAdapter(Adapter):
    """INCREMENTAL sync stub. Implement in Phase 3.

    Polls Mem v2: GET /v2/notes?order_by=updated_at&limit=100, walk cursor until
    you pass the last-sync watermark, re-ingest changed notes only.
    """

    name = "mem"

    def __init__(self, watermark: datetime | None = None) -> None:
        self.api_key = os.environ.get("MEM_API_KEY")
        self.watermark = watermark

    def fetch(self) -> Iterable[RawDoc]:  # pragma: no cover - stub
        raise NotImplementedError(
            "MemApiAdapter is a Phase-3 stub. Use MemAdapter (markdown export) for the spike."
        )
