"""Granola adapter tests — JSON export + markdown-folder paths, checkpoint."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from brain.adapters.granola_adapter import GranolaAdapter
from brain.core.checkpoint import CheckpointStore


JSON_FIXTURE = {
    "id": "mtg_1",
    "title": "PBTV product review",
    "created_at": "2026-05-28T10:00:00Z",
    "summary": "Decided to pivot to local-first.",
    "transcript": [
        {"speaker": "Wes", "text": "Where do we land on the canonical store?"},
        {"speaker": "Jeff", "text": "Local. Mem is just a feeder."},
    ],
    "attendees": [{"name": "Wes Shields"}, {"name": "Jeff Torres"}],
}


def test_json_export_becomes_one_speakered_doc():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "mtg.json"
        p.write_text(json.dumps(JSON_FIXTURE), encoding="utf-8")
        docs = list(GranolaAdapter(str(p)).fetch())
        assert len(docs) == 1
        doc = docs[0]
        assert doc.source == "granola"
        assert doc.source_id == "mtg_1"
        assert "PBTV product review" in doc.text
        assert "Wes: Where" in doc.text
        assert "Decided to pivot" in doc.text
        assert "Wes Shields" in doc.meta["attendees"]


def test_directory_walks_json_and_markdown():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "a.json").write_text(json.dumps(JSON_FIXTURE), encoding="utf-8")
        (root / "b.md").write_text("# meeting b\n\nbody", encoding="utf-8")
        (root / "c.bin").write_bytes(b"\x00")
        docs = list(GranolaAdapter(str(root)).fetch())
        ids = {d.source_id for d in docs}
        assert ids == {"mtg_1", "b"}


def test_checkpoint_skips_already_seen_meetings():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        cp_db = str(root / "e.db")
        (root / "a.json").write_text(json.dumps(JSON_FIXTURE), encoding="utf-8")
        first = list(GranolaAdapter(str(root), checkpoint_db=cp_db).fetch())
        assert len(first) == 1
        second = list(GranolaAdapter(str(root), checkpoint_db=cp_db).fetch())
        assert second == []  # same meeting, already past watermark


def test_empty_json_skipped():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "empty.json"
        p.write_text(json.dumps({"id": "x", "title": "empty"}), encoding="utf-8")
        docs = list(GranolaAdapter(str(p)).fetch())
        assert docs == []
