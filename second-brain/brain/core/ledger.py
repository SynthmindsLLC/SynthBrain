"""Ingest run ledger: one durable row per ingest run.

Every CLI ingest (real or dry-run) opens a row as 'running' and finalizes it
with counts when the run ends — completed, failed, or dry-run. The dashboard's
"is the brain being fed?" panel reads this table; the heuristic-vs-LLM counters
make classification-quality work measurable instead of anecdotal.

Lives in the SAME SQLite db as checkpoints and entities so there is exactly one
operational database to back up. Timestamps are tz-aware UTC ISO; error samples
are capped so one pathological run can't bloat the row.
"""

from __future__ import annotations

import json
import sqlite3
import threading
import uuid
from datetime import datetime, timezone
from typing import Any

STATUSES = ("running", "completed", "failed", "dry-run")
MAX_ERROR_SAMPLES = 10


class IngestLedger:
    def __init__(self, db_path: str = "./entities.db") -> None:
        self._db = sqlite3.connect(db_path, check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._lock = threading.RLock()
        self._db.execute(
            """
            CREATE TABLE IF NOT EXISTS ingest_runs (
                run_id TEXT PRIMARY KEY,
                adapter TEXT NOT NULL,
                source TEXT NOT NULL,
                started_at TEXT NOT NULL,
                finished_at TEXT,
                status TEXT NOT NULL,
                docs INTEGER NOT NULL DEFAULT 0,
                chunks INTEGER NOT NULL DEFAULT 0,
                errors INTEGER NOT NULL DEFAULT 0,
                skipped INTEGER NOT NULL DEFAULT 0,
                llm_classified INTEGER NOT NULL DEFAULT 0,
                heuristic_classified INTEGER NOT NULL DEFAULT 0,
                error_samples TEXT NOT NULL DEFAULT '[]',
                meta TEXT NOT NULL DEFAULT '{}'
            )
            """
        )
        self._db.commit()

    def start(self, adapter: str, source: str, *, meta: dict[str, Any] | None = None) -> str:
        run_id = uuid.uuid4().hex
        now = datetime.now(timezone.utc).isoformat()
        with self._lock:
            self._db.execute(
                """INSERT INTO ingest_runs
                   (run_id, adapter, source, started_at, status, meta)
                   VALUES (?,?,?,?,'running',?)""",
                (run_id, adapter, source, now, json.dumps(meta or {})),
            )
            self._db.commit()
        return run_id

    def finish(
        self,
        run_id: str,
        status: str,
        *,
        docs: int = 0,
        chunks: int = 0,
        errors: int = 0,
        skipped: int = 0,
        llm_classified: int = 0,
        heuristic_classified: int = 0,
        error_samples: list[str] | None = None,
        meta: dict[str, Any] | None = None,
    ) -> None:
        if status not in STATUSES:
            raise ValueError(f"status must be one of {STATUSES}, got {status!r}")
        now = datetime.now(timezone.utc).isoformat()
        samples = json.dumps(list(error_samples or [])[:MAX_ERROR_SAMPLES])
        with self._lock:
            if meta is not None:
                self._db.execute(
                    "UPDATE ingest_runs SET meta=? WHERE run_id=?",
                    (json.dumps(meta), run_id),
                )
            self._db.execute(
                """UPDATE ingest_runs SET
                     finished_at=?, status=?, docs=?, chunks=?, errors=?, skipped=?,
                     llm_classified=?, heuristic_classified=?, error_samples=?
                   WHERE run_id=?""",
                (now, status, docs, chunks, errors, skipped,
                 llm_classified, heuristic_classified, samples, run_id),
            )
            self._db.commit()

    def get(self, run_id: str) -> dict[str, Any] | None:
        with self._lock:
            r = self._db.execute(
                "SELECT * FROM ingest_runs WHERE run_id=?", (run_id,)
            ).fetchone()
        return self._row_to_dict(r) if r else None

    def runs(self, limit: int = 50) -> list[dict[str, Any]]:
        with self._lock:
            rows = self._db.execute(
                "SELECT * FROM ingest_runs ORDER BY started_at DESC, run_id DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [self._row_to_dict(r) for r in rows]

    @staticmethod
    def _row_to_dict(r: sqlite3.Row) -> dict[str, Any]:
        d = dict(r)
        d["error_samples"] = json.loads(d["error_samples"])
        d["meta"] = json.loads(d["meta"])
        return d
