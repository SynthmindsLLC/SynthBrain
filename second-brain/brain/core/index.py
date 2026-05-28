"""The canonical index. LanceDB, embedded, on-disk, owned by Wes.

This is the thing the uploaded G2 research assumed would be "a mirror of Mem."
In this architecture it is the brain itself: every adapter writes here, and both
chat and (eventually) the glasses read here. Mem is just one of the writers.
"""

from __future__ import annotations

from typing import Any

import lancedb

from .embed import Embedder
from .schema import MemoryChunk, arrow_schema

TABLE = "memory"


class BrainIndex:
    def __init__(self, db_path: str, embedder: Embedder) -> None:
        self._db = lancedb.connect(db_path)
        self._embedder = embedder
        self._schema = arrow_schema(embedder.dim)
        if TABLE not in self._db.list_tables():
            self._db.create_table(TABLE, schema=self._schema)
        self._table = self._db.open_table(TABLE)

    def add_chunks(self, chunks: list[MemoryChunk]) -> int:
        if not chunks:
            return 0
        vectors = self._embedder.embed([c.text for c in chunks])
        rows: list[dict[str, Any]] = [c.to_row(v) for c, v in zip(chunks, vectors)]
        # Idempotent upsert on the deterministic id: delete-then-add.
        ids = "', '".join(r["id"] for r in rows)
        self._table.delete(f"id IN ('{ids}')")
        self._table.add(rows)
        return len(rows)

    def query(
        self,
        text: str,
        k: int = 5,
        layer: str | None = None,
        project: str | None = None,
    ) -> list[dict[str, Any]]:
        vec = self._embedder.embed([text])[0]
        q = self._table.search(vec).metric("cosine").limit(k)
        filters: list[str] = []
        if layer:
            filters.append(f"layer = '{layer}'")
        if project:
            filters.append(f"array_has(project_tags, '{project}')")
        if filters:
            q = q.where(" AND ".join(filters))
        return q.to_list()

    def count(self) -> int:
        return self._table.count_rows()
