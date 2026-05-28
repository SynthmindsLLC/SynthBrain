"""Fieldy adapter tests — fully offline (mock the HTTP layer).

Covers: auth error, pagination, segment-shape transcripts, direct-text
transcripts, checkpoint resumption, --limit short-circuit, idempotent id.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from brain.adapters.fieldy_adapter import (
    FieldyAdapter,
    FieldyAuthError,
)
from brain.core.checkpoint import CheckpointStore


class _Page:
    def __init__(self, items, next_cursor=None):
        self.items = items
        self.next_cursor = next_cursor

    def payload(self):
        return {"data": self.items, "next_cursor": self.next_cursor}


def _patch_get(pages):
    """Make FieldyAdapter._get return successive page payloads."""
    calls = {"n": 0}

    def fake_get(self, path, params):
        i = calls["n"]
        calls["n"] += 1
        if i >= len(pages):
            return {"data": []}
        return pages[i].payload()

    return patch.object(FieldyAdapter, "_get", new=fake_get), calls


def test_raises_when_key_missing(monkeypatch):
    monkeypatch.delenv("FIELDY_API_KEY", raising=False)
    with pytest.raises(FieldyAuthError):
        FieldyAdapter()


def test_segment_shape_transcript_becomes_speakered_text():
    items = [
        {
            "id": "tx_1",
            "created_at": "2026-05-28T12:00:00Z",
            "speakers": [{"name": "Wes"}, {"name": "Jeff"}],
            "segments": [
                {"speaker": "Wes", "text": "Hey, how's the curator gig?"},
                {"speaker": "Jeff", "text": "Busy. We're restoring the Morgan."},
            ],
        }
    ]
    patcher, _ = _patch_get([_Page(items)])
    with patcher:
        a = FieldyAdapter(api_key="dummy")
        docs = list(a.fetch())
    assert len(docs) == 1
    d = docs[0]
    assert d.source == "fieldy"
    assert d.source_id == "tx_1"
    assert "Wes: Hey" in d.text
    assert "Jeff: Busy" in d.text
    assert d.meta["speakers"] == ["Wes", "Jeff"]


def test_direct_text_transcript_is_kept_verbatim():
    items = [{"id": "tx_2", "transcript": "single line transcript",
              "created_at": "2026-05-28T13:00:00Z"}]
    patcher, _ = _patch_get([_Page(items)])
    with patcher:
        docs = list(FieldyAdapter(api_key="dummy").fetch())
    assert "single line transcript" in docs[0].text


def test_pagination_walks_until_no_cursor():
    pages = [
        _Page([{"id": "a", "transcript": "alpha"}], next_cursor="c1"),
        _Page([{"id": "b", "transcript": "bravo"}], next_cursor="c2"),
        _Page([{"id": "c", "transcript": "charlie"}], next_cursor=None),
    ]
    patcher, calls = _patch_get(pages)
    with patcher:
        docs = list(FieldyAdapter(api_key="dummy").fetch())
    assert [d.source_id for d in docs] == ["a", "b", "c"]
    assert calls["n"] == 3


def test_limit_short_circuits_pagination():
    items = [{"id": f"id_{i}", "transcript": f"t{i}"} for i in range(10)]
    pages = [_Page(items, next_cursor="more"), _Page([], next_cursor=None)]
    patcher, _ = _patch_get(pages)
    with patcher:
        docs = list(FieldyAdapter(api_key="dummy", limit=3).fetch())
    assert len(docs) == 3


def test_checkpoint_records_newest_created_at():
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        items = [
            {"id": "old", "transcript": "x", "created_at": "2026-05-20T10:00:00Z"},
            {"id": "new", "transcript": "y", "created_at": "2026-05-28T10:00:00Z"},
        ]
        patcher, _ = _patch_get([_Page(items)])
        with patcher:
            list(FieldyAdapter(api_key="dummy", checkpoint_db=cp_db).fetch())
        cp = CheckpointStore(cp_db)
        assert cp.get("fieldy") == "2026-05-28T10:00:00Z"


def test_empty_or_idless_transcripts_skipped():
    items = [
        {"id": "ok", "transcript": "good"},
        {"id": "", "transcript": "no id"},        # dropped
        {"id": "blank", "transcript": ""},         # dropped
    ]
    patcher, _ = _patch_get([_Page(items)])
    with patcher:
        docs = list(FieldyAdapter(api_key="dummy").fetch())
    assert [d.source_id for d in docs] == ["ok"]


def test_chunk_id_is_deterministic_across_runs():
    """Same Fieldy id should produce the same chunk id => idempotent upsert."""
    from brain.core.schema import MemoryChunk
    a = MemoryChunk(text="x", source="fieldy", source_id="tx_999", chunk_index=0)
    b = MemoryChunk(text="x", source="fieldy", source_id="tx_999", chunk_index=0)
    assert a.id == b.id


def test_pagination_breaks_on_cursor_loop():
    """Defensive: if the server keeps returning the same cursor, we bail."""
    pages = [
        _Page([{"id": "a", "transcript": "alpha"}], next_cursor="stuck"),
        _Page([{"id": "b", "transcript": "bravo"}], next_cursor="stuck"),
        _Page([{"id": "c", "transcript": "charlie"}], next_cursor="stuck"),
    ]
    patcher, calls = _patch_get(pages)
    with patcher:
        docs = list(FieldyAdapter(api_key="dummy").fetch())
    # Should stop after the second page detects the repeated cursor.
    assert calls["n"] == 2
    assert [d.source_id for d in docs] == ["a", "b"]
