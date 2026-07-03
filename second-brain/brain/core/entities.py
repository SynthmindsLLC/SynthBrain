"""The entity/graph layer: the relational half of the brain.

Chunks (LanceDB) answer "what's similar." Entities + edges (here) answer
"who is this, and what are they connected to." The dossier query traverses this:
   resolve("Jeff") -> Person node -> edges(attended) -> Event node.

Stored in SQLite because the dossier is a JOIN, not a similarity search — exact
lookups and graph traversal are what relational engines are good at. Embeddings
for fuzzy resolve() get added in the next step; the column is reserved here.
"""

from __future__ import annotations

import json
import re
import sqlite3
import threading
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

KINDS = ("person", "event", "place", "org")
# Primary rels come from adapters; the last two are DERIVED by graphlab:
# co_attended = weighted one-mode projection of the person-event bipartite
# graph (Breiger 1974; Newman 2001 fractional weighting), co_mentioned =
# PMI-weighted chunk co-occurrence (Church & Hanks 1990).
RELS = ("attended", "mentioned_in", "discussed_with", "works_at", "family_of",
        "co_attended", "co_mentioned")


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "unknown"


def canonical_id(kind: str, name: str) -> str:
    return f"{kind}:{slug(name)}"


@dataclass
class Entity:
    kind: str
    name: str
    aliases: list[str] = field(default_factory=list)
    attributes: dict[str, Any] = field(default_factory=dict)
    source_refs: list[str] = field(default_factory=list)
    id: str = ""
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if self.kind not in KINDS:
            raise ValueError(f"kind must be one of {KINDS}, got {self.kind!r}")
        if not self.id:
            self.id = canonical_id(self.kind, self.name)


@dataclass
class Edge:
    src: str
    rel: str
    dst: str
    attributes: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.rel not in RELS:
            raise ValueError(f"rel must be one of {RELS}, got {self.rel!r}")


class EntityStore:
    def __init__(self, db_path: str = "./entities.db") -> None:
        # The FastAPI surface caches one store on app.state and serves sync
        # endpoints from a threadpool, so the connection crosses threads.
        # check_same_thread=False allows that; the RLock serializes access
        # (re-entrant because neighbors() calls get_entity() internally).
        self._db = sqlite3.connect(db_path, check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._lock = threading.RLock()
        self._init()

    def _init(self) -> None:
        self._db.executescript(
            """
            CREATE TABLE IF NOT EXISTS entities (
                id TEXT PRIMARY KEY,
                kind TEXT NOT NULL,
                name TEXT NOT NULL,
                aliases TEXT NOT NULL DEFAULT '[]',
                attributes TEXT NOT NULL DEFAULT '{}',
                source_refs TEXT NOT NULL DEFAULT '[]',
                created_at TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_entities_kind ON entities(kind);
            CREATE INDEX IF NOT EXISTS idx_entities_name ON entities(name COLLATE NOCASE);
            CREATE TABLE IF NOT EXISTS edges (
                src TEXT NOT NULL,
                rel TEXT NOT NULL,
                dst TEXT NOT NULL,
                attributes TEXT NOT NULL DEFAULT '{}',
                PRIMARY KEY (src, rel, dst)
            );
            CREATE INDEX IF NOT EXISTS idx_edges_src ON edges(src);
            CREATE INDEX IF NOT EXISTS idx_edges_dst ON edges(dst);
            """
        )
        self._db.commit()

    # --- writes -----------------------------------------------------------
    def upsert_entity(self, e: Entity) -> str:
        """Merge-on-conflict: aliases/source_refs union, attributes overlay.
        Re-ingesting the same person enriches rather than clobbers."""
        with self._lock:
            existing = self.get_entity(e.id)
            if existing:
                aliases = sorted(set(existing.aliases) | set(e.aliases))
                source_refs = sorted(set(existing.source_refs) | set(e.source_refs))
                attributes = {**existing.attributes, **e.attributes}
            else:
                aliases, source_refs, attributes = sorted(set(e.aliases)), e.source_refs, e.attributes
            self._db.execute(
                """INSERT INTO entities (id, kind, name, aliases, attributes, source_refs, created_at)
                   VALUES (?,?,?,?,?,?,?)
                   ON CONFLICT(id) DO UPDATE SET
                     name=excluded.name, aliases=excluded.aliases,
                     attributes=excluded.attributes, source_refs=excluded.source_refs""",
                (e.id, e.kind, e.name, json.dumps(aliases), json.dumps(attributes),
                 json.dumps(source_refs), e.created_at.astimezone(timezone.utc).isoformat()),
            )
            self._db.commit()
        return e.id

    def add_edge(self, edge: Edge) -> None:
        with self._lock:
            self._db.execute(
                """INSERT INTO edges (src, rel, dst, attributes) VALUES (?,?,?,?)
                   ON CONFLICT(src, rel, dst) DO UPDATE SET attributes=excluded.attributes""",
                (edge.src, edge.rel, edge.dst, json.dumps(edge.attributes)),
            )
            self._db.commit()

    # --- reads ------------------------------------------------------------
    def get_entity(self, entity_id: str) -> Entity | None:
        with self._lock:
            r = self._db.execute("SELECT * FROM entities WHERE id=?", (entity_id,)).fetchone()
        return self._row_to_entity(r) if r else None

    def find_by_name(self, name: str, kind: str | None = None) -> list[Entity]:
        """Exact (case-insensitive) match on name OR alias. This is the
        deterministic core that the future fuzzy resolve() will fall back on."""
        with self._lock:
            rows = self._db.execute(
                "SELECT * FROM entities" + (" WHERE kind=?" if kind else ""),
                (kind,) if kind else (),
            ).fetchall()
        low = name.lower()
        out = []
        for r in rows:
            e = self._row_to_entity(r)
            names = [e.name.lower()] + [a.lower() for a in e.aliases]
            if low in names:
                out.append(e)
        return out

    def neighbors(self, entity_id: str, rel: str | None = None) -> list[tuple[Edge, Entity | None]]:
        with self._lock:
            q = "SELECT * FROM edges WHERE src=?" + (" AND rel=?" if rel else "")
            rows = self._db.execute(q, (entity_id, rel) if rel else (entity_id,)).fetchall()
            out = []
            for r in rows:
                edge = Edge(src=r["src"], rel=r["rel"], dst=r["dst"], attributes=json.loads(r["attributes"]))
                out.append((edge, self.get_entity(edge.dst)))
        return out

    def all_entities(self, kind: str | None = None) -> list[Entity]:
        with self._lock:
            rows = self._db.execute(
                "SELECT * FROM entities" + (" WHERE kind=?" if kind else "") + " ORDER BY kind, name",
                (kind,) if kind else (),
            ).fetchall()
        return [self._row_to_entity(r) for r in rows]

    def counts(self) -> dict[str, int]:
        with self._lock:
            ent = self._db.execute("SELECT COUNT(*) c FROM entities").fetchone()["c"]
            edg = self._db.execute("SELECT COUNT(*) c FROM edges").fetchone()["c"]
        return {"entities": ent, "edges": edg}

    @staticmethod
    def _row_to_entity(r: sqlite3.Row) -> Entity:
        return Entity(
            id=r["id"], kind=r["kind"], name=r["name"],
            aliases=json.loads(r["aliases"]), attributes=json.loads(r["attributes"]),
            source_refs=json.loads(r["source_refs"]),
            created_at=datetime.fromisoformat(r["created_at"]),
        )
