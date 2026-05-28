"""Sync-state store: remember where each adapter left off.

Every connector that does incremental sync (Fieldy webhooks, Google Calendar
syncToken, People API syncToken, Drive changes token, filesystem mtime) needs
a durable "last seen X" marker. They all share one shape and one store, so we
don't reinvent it per adapter.

Stored in SQLite alongside the entity graph. Adapter-keyed; values are
opaque strings (sync token, iso8601 timestamp, file hash, whatever the
upstream uses).
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone


class CheckpointStore:
    def __init__(self, db_path: str = "./entities.db") -> None:
        self._db = sqlite3.connect(db_path)
        self._db.execute(
            """
            CREATE TABLE IF NOT EXISTS checkpoints (
                adapter TEXT NOT NULL,
                key TEXT NOT NULL,
                value TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                PRIMARY KEY (adapter, key)
            )
            """
        )
        self._db.commit()

    def get(self, adapter: str, key: str = "last_sync") -> str | None:
        r = self._db.execute(
            "SELECT value FROM checkpoints WHERE adapter=? AND key=?",
            (adapter, key),
        ).fetchone()
        return r[0] if r else None

    def set(self, adapter: str, value: str, key: str = "last_sync") -> None:
        now = datetime.now(timezone.utc).isoformat()
        self._db.execute(
            """INSERT INTO checkpoints (adapter, key, value, updated_at)
               VALUES (?,?,?,?)
               ON CONFLICT(adapter, key) DO UPDATE SET
                 value=excluded.value, updated_at=excluded.updated_at""",
            (adapter, key, value, now),
        )
        self._db.commit()

    def clear(self, adapter: str, key: str | None = None) -> None:
        if key:
            self._db.execute(
                "DELETE FROM checkpoints WHERE adapter=? AND key=?",
                (adapter, key),
            )
        else:
            self._db.execute("DELETE FROM checkpoints WHERE adapter=?", (adapter,))
        self._db.commit()

    def all(self) -> list[dict]:
        rows = self._db.execute(
            "SELECT adapter, key, value, updated_at FROM checkpoints ORDER BY adapter, key"
        ).fetchall()
        return [
            {"adapter": r[0], "key": r[1], "value": r[2], "updated_at": r[3]}
            for r in rows
        ]
