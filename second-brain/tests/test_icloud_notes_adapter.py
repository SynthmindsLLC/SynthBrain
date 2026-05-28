"""iCloud Notes adapter tests — both folder-of-exports and NoteStore.sqlite."""

from __future__ import annotations

import gzip
import sqlite3
import tempfile
import time
from pathlib import Path

import pytest

from brain.adapters.icloud_notes_adapter import ICloudNotesAdapter
from brain.core.checkpoint import CheckpointStore


# ---- folder-of-exports path -------------------------------------------

def test_folder_of_markdown_notes_ingested():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "trip-planning.md").write_text("# Trip planning\n\nFlights booked.", encoding="utf-8")
        (root / "groceries.txt").write_text("eggs\nmilk\nbread", encoding="utf-8")
        (root / "skipme.bin").write_bytes(b"\x00\x01")
        docs = list(ICloudNotesAdapter(str(root)).fetch())
        assert {Path(d.meta["path"]).name for d in docs} == {"trip-planning.md", "groceries.txt"}


def test_folder_html_export_is_stripped_to_text():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "note.html").write_text(
            "<html><body><h1>Title</h1><p>Body &amp; more</p></body></html>",
            encoding="utf-8",
        )
        docs = list(ICloudNotesAdapter(str(root)).fetch())
        assert len(docs) == 1
        assert "<" not in docs[0].text
        assert "Body & more" in docs[0].text


def test_folder_checkpoint_skips_unchanged():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        cp_db = str(root / "e.db")
        (root / "a.md").write_text("first", encoding="utf-8")
        first = list(ICloudNotesAdapter(str(root), checkpoint_db=cp_db).fetch())
        assert len(first) == 1
        second = list(ICloudNotesAdapter(str(root), checkpoint_db=cp_db).fetch())
        assert second == []
        time.sleep(1.0)
        (root / "b.md").write_text("second", encoding="utf-8")
        third = list(ICloudNotesAdapter(str(root), checkpoint_db=cp_db).fetch())
        names = {Path(d.meta["path"]).name for d in third}
        assert "b.md" in names and "a.md" not in names


# ---- NoteStore.sqlite path --------------------------------------------

def _build_fake_notestore(path: Path, *, notes: list[dict]) -> None:
    conn = sqlite3.connect(str(path))
    # Recreate just enough of the Notes schema to satisfy the adapter query.
    conn.executescript(
        """
        CREATE TABLE Z_PRIMARYKEY (
            Z_ENT INTEGER PRIMARY KEY, Z_NAME TEXT
        );
        CREATE TABLE ZICCLOUDSYNCINGOBJECT (
            Z_PK INTEGER PRIMARY KEY,
            Z_ENT INTEGER,
            ZIDENTIFIER TEXT,
            ZTITLE1 TEXT,        -- note title
            ZTITLE2 TEXT,        -- folder title (when row is a folder)
            ZSNIPPET TEXT,
            ZMODIFICATIONDATE REAL,
            ZISPASSWORDPROTECTED INTEGER DEFAULT 0,
            ZMARKEDFORDELETION INTEGER DEFAULT 0,
            ZFOLDER INTEGER
        );
        CREATE TABLE ZICNOTEDATA (
            Z_PK INTEGER PRIMARY KEY,
            ZNOTE INTEGER,
            ZDATA BLOB
        );
        INSERT INTO Z_PRIMARYKEY VALUES (11, 'ICNote');
        INSERT INTO Z_PRIMARYKEY VALUES (12, 'ICFolder');
        INSERT INTO ZICCLOUDSYNCINGOBJECT (Z_PK, Z_ENT, ZTITLE2)
          VALUES (1, 12, 'Notes');
        """
    )
    for i, n in enumerate(notes, start=2):
        body = n.get("body", "").encode("utf-8")
        gz = gzip.compress(body)
        conn.execute(
            "INSERT INTO ZICCLOUDSYNCINGOBJECT "
            "(Z_PK, Z_ENT, ZIDENTIFIER, ZTITLE1, ZSNIPPET, ZMODIFICATIONDATE, "
            " ZISPASSWORDPROTECTED, ZMARKEDFORDELETION, ZFOLDER) "
            "VALUES (?, 11, ?, ?, ?, ?, ?, ?, 1)",
            (i, n["id"], n["title"], n.get("snippet", ""), n["mod"],
             1 if n.get("locked") else 0,
             1 if n.get("deleted") else 0),
        )
        conn.execute(
            "INSERT INTO ZICNOTEDATA (ZNOTE, ZDATA) VALUES (?, ?)",
            (i, gz),
        )
    conn.commit()
    conn.close()


def test_sqlite_path_extracts_notes_skips_locked_and_deleted():
    with tempfile.TemporaryDirectory() as d:
        db = Path(d) / "NoteStore.sqlite"
        _build_fake_notestore(db, notes=[
            {"id": "n1", "title": "Trip", "body": "Flights booked. Hotel TBD.",
             "mod": 750000000.0},
            {"id": "n2", "title": "Locked", "body": "secret", "mod": 750100000.0,
             "locked": True},
            {"id": "n3", "title": "Deleted", "body": "junk", "mod": 750200000.0,
             "deleted": True},
            {"id": "n4", "title": "Project notes",
             "body": "Decided on local-first canonical store.",
             "mod": 750300000.0},
        ])
        docs = list(ICloudNotesAdapter(str(db)).fetch())
        ids = {d.source_id for d in docs}
        assert ids == {"n1", "n4"}


def test_sqlite_checkpoint_advances_to_latest_modification():
    with tempfile.TemporaryDirectory() as d:
        db = Path(d) / "NoteStore.sqlite"
        cp_db = str(Path(d) / "e.db")
        _build_fake_notestore(db, notes=[
            {"id": "n1", "title": "A", "body": "alpha", "mod": 750000000.0},
            {"id": "n2", "title": "B", "body": "bravo body content", "mod": 750200000.0},
        ])
        list(ICloudNotesAdapter(str(db), checkpoint_db=cp_db).fetch())
        saved = CheckpointStore(cp_db).get("icloud-notes")
        assert float(saved) == 750200000.0
        # Second run should yield nothing
        second = list(ICloudNotesAdapter(str(db), checkpoint_db=cp_db).fetch())
        assert second == []


def test_raises_when_source_missing():
    with pytest.raises(FileNotFoundError):
        ICloudNotesAdapter("/nope/never/here")
