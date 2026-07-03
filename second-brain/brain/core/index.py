"""The canonical index. LanceDB, embedded, on-disk, owned by Wes.

This is the thing the uploaded G2 research assumed would be "a mirror of Mem."
In this architecture it is the brain itself: every adapter writes here, and both
chat and (eventually) the glasses read here. Mem is just one of the writers.
"""

from __future__ import annotations

from typing import Any

import lancedb
import pyarrow as pa

from .embed import Embedder
from .schema import MemoryChunk, arrow_schema

TABLE = "memory"

# Embed calls batch so local models keep a bounded working set; the delete
# filter chunks so a bulk upsert never builds a megabyte-long `id IN (...)`.
EMBED_BATCH = 128
DELETE_BATCH = 500


class BrainIndex:
    def __init__(self, db_path: str, embedder: Embedder) -> None:
        self._db = lancedb.connect(db_path)
        self._embedder = embedder
        self._schema = arrow_schema(embedder.dim)
        if TABLE not in _list_table_names(self._db):
            self._db.create_table(TABLE, schema=self._schema)
        self._table = self._db.open_table(TABLE)

    def add_chunks(self, chunks: list[MemoryChunk]) -> int:
        if not chunks:
            return 0
        vectors: list[list[float]] = []
        for i in range(0, len(chunks), EMBED_BATCH):
            batch = chunks[i : i + EMBED_BATCH]
            vectors.extend(self._embedder.embed([c.text for c in batch]))
        rows: list[dict[str, Any]] = [c.to_row(v) for c, v in zip(chunks, vectors)]
        # Idempotent upsert on the deterministic id: delete-then-add.
        all_ids = [r["id"] for r in rows]
        for i in range(0, len(all_ids), DELETE_BATCH):
            ids = "', '".join(all_ids[i : i + DELETE_BATCH])
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

    def scan(self, columns: list[str]) -> pa.Table:
        """Full-table projection for analytics (stats breakdown, recent
        chunks). Selecting only the named columns keeps the embeddings out
        of the returned table."""
        return self._table.to_arrow().select(columns)


def _list_table_names(db) -> list[str]:
    """LanceDB 0.32 changed list_tables() to return a ListTablesResponse object
    (with .tables) instead of a bare list; the deprecated table_names() still
    returns a list. Try the new shape first, then fall back."""
    try:
        result = db.list_tables()
    except Exception:
        result = []
    if isinstance(result, list):
        return result
    tables = getattr(result, "tables", None)
    if isinstance(tables, list):
        return tables
    return list(db.table_names())
