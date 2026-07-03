"""Universal-intake tests: inbox drop folder, .eml parsing, AgentMail poller,
POST /inbox, and the watch loop's empty-cycle ledger pruning."""

from __future__ import annotations

import argparse
import json
from datetime import timezone
from pathlib import Path

import pytest

from brain.adapters.agentmail_adapter import AgentMailAdapter
from brain.adapters.inbox_adapter import InboxAdapter, html_to_text
from brain.core.checkpoint import CheckpointStore
from brain.core.embed import FakeEmbedder
from brain.core.index import BrainIndex
from brain.core.ledger import IngestLedger

EML = b"""From: Nick <nick@example.com>
To: wes@synthminds.ai
Subject: Fwd: enclosure decision
Date: Tue, 01 Jul 2026 10:30:00 -0400
Content-Type: text/plain; charset="utf-8"

We decided to go with the milsbo enclosure because of humidity control.
"""

EML_HTML = b"""From: bot@example.com
To: wes@synthminds.ai
Subject: html only
Date: Tue, 01 Jul 2026 11:00:00 -0400
MIME-Version: 1.0
Content-Type: text/html; charset="utf-8"

<html><body><style>p{}</style><p>First line.</p><p>Second <b>bold</b> line.</p></body></html>
"""


def _inbox(tmp_path: Path) -> Path:
    d = tmp_path / "BrainInbox"
    d.mkdir()
    return d


# --- inbox adapter -----------------------------------------------------------


def test_inbox_ingests_text_and_eml(tmp_path):
    d = _inbox(tmp_path)
    (d / "note.md").write_text("# A note\n\nremember this", encoding="utf-8")
    (d / "forward.eml").write_bytes(EML)

    docs = list(InboxAdapter(str(d)).fetch())
    assert len(docs) == 2
    by_ext = {Path(doc.meta["path"]).suffix: doc for doc in docs}
    assert "remember this" in by_ext[".md"].text
    eml = by_ext[".eml"]
    assert eml.text.startswith("# Fwd: enclosure decision")
    assert "**From:** Nick <nick@example.com>" in eml.text
    assert "milsbo enclosure" in eml.text
    assert eml.meta["kind"] == "eml"
    # created_at comes from the Date header, tz-aware UTC.
    assert eml.created_at.tzinfo is not None
    assert eml.created_at.astimezone(timezone.utc).hour == 14  # 10:30 -0400


def test_inbox_html_email_falls_back_to_stripped_html(tmp_path):
    d = _inbox(tmp_path)
    (d / "h.eml").write_bytes(EML_HTML)
    (doc,) = InboxAdapter(str(d)).fetch()
    assert "First line." in doc.text
    assert "Second bold line." in doc.text
    assert "<p>" not in doc.text and "style" not in doc.text.lower()


def test_inbox_moves_only_on_commit(tmp_path):
    d = _inbox(tmp_path)
    (d / "note.txt").write_text("hello", encoding="utf-8")
    (d / "junk.xyz").write_text("???", encoding="utf-8")

    a = InboxAdapter(str(d))
    docs = list(a.fetch())
    assert len(docs) == 1
    assert a.skip_report["unsupported_ext"]["count"] == 1
    # Nothing moved before commit — a failed run must leave the queue intact.
    assert (d / "note.txt").exists() and (d / "junk.xyz").exists()

    a.commit_checkpoint()
    assert not (d / "note.txt").exists()
    processed = list((d / "processed").rglob("note.txt"))
    assert len(processed) == 1
    assert (d / "failed" / "junk.xyz").exists()
    # Queue is now empty: a fresh fetch yields nothing.
    assert list(InboxAdapter(str(d)).fetch()) == []


def test_inbox_skips_processed_failed_and_hidden(tmp_path):
    d = _inbox(tmp_path)
    (d / "processed").mkdir()
    (d / "processed" / "old.md").write_text("done", encoding="utf-8")
    (d / "failed").mkdir()
    (d / "failed" / "bad.md").write_text("bad", encoding="utf-8")
    (d / ".DS_Store").write_text("x", encoding="utf-8")
    assert list(InboxAdapter(str(d)).fetch()) == []
    assert not InboxAdapter(str(d)).has_pending()


def test_inbox_name_collision_in_processed(tmp_path):
    d = _inbox(tmp_path)
    for round_ in range(2):
        (d / "same.md").write_text(f"round {round_}", encoding="utf-8")
        a = InboxAdapter(str(d))
        assert len(list(a.fetch())) == 1
        a.commit_checkpoint()
    moved = sorted(p.name for p in (d / "processed").rglob("same*.md"))
    assert len(moved) == 2 and moved[0] != moved[1]


def test_inbox_missing_dir_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        InboxAdapter(str(tmp_path / "nope"))


def test_html_to_text_survives_pathological_markup():
    assert "hello" in html_to_text("<p>hello")
    assert html_to_text("") == ""


# --- agentmail adapter --------------------------------------------------------


class _FakeResp:
    def __init__(self, payload: dict):
        self._body = json.dumps(payload).encode()

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _fake_urlopen(pages: dict[str, dict]):
    def opener(req, timeout=0):
        url = req.full_url
        for key, payload in pages.items():
            if key in url:
                return _FakeResp(payload)
        return _FakeResp({})
    return opener


def test_agentmail_requires_key(monkeypatch):
    monkeypatch.delenv("AGENTMAIL_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="AGENTMAIL_API_KEY"):
        AgentMailAdapter()


def test_agentmail_fetch_renders_and_defers_watermark(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENTMAIL_API_KEY", "test-key")
    import brain.adapters.agentmail_adapter as mod

    listing = {"messages": [
        {"message_id": "m1", "timestamp": "2026-07-03T12:00:00Z",
         "from": "a@example.com", "subject": "hello brain"},
    ]}
    full = {"message_id": "m1", "timestamp": "2026-07-03T12:00:00Z",
            "from": "a@example.com", "to": ["synthbrain@agentmail.to"],
            "subject": "hello brain", "text": "the body"}
    monkeypatch.setattr(mod.urllib.request, "urlopen",
                        _fake_urlopen({"/messages/m1": full, "/messages": listing}))

    entdb = str(tmp_path / "e.db")
    a = AgentMailAdapter(checkpoint_db=entdb)
    (doc,) = a.fetch()
    assert doc.source == "agentmail" and doc.source_id == "m1"
    assert doc.text.startswith("# hello brain")
    assert "the body" in doc.text
    # Watermark deferred until commit.
    cp = CheckpointStore(entdb)
    assert cp.get("agentmail", a.checkpoint_key) is None
    a.commit_checkpoint()
    assert cp.get("agentmail", a.checkpoint_key) == "2026-07-03T12:00:00+00:00"

    # Second poll with the committed watermark yields nothing new.
    b = AgentMailAdapter(checkpoint_db=entdb)
    monkeypatch.setattr(mod.urllib.request, "urlopen",
                        _fake_urlopen({"/messages/m1": full, "/messages": listing}))
    assert list(b.fetch()) == []


def test_agentmail_html_fallback_and_camelcase(monkeypatch, tmp_path):
    monkeypatch.setenv("AGENTMAIL_API_KEY", "test-key")
    import brain.adapters.agentmail_adapter as mod

    listing = {"messages": [
        {"messageId": "m2", "createdAt": "2026-07-03T13:00:00Z", "subject": "s"},
    ]}
    full = {"messageId": "m2", "createdAt": "2026-07-03T13:00:00Z",
            "subject": "s", "html": "<p>only html</p>", "threadId": "t9"}
    monkeypatch.setattr(mod.urllib.request, "urlopen",
                        _fake_urlopen({"/messages/m2": full, "/messages": listing}))
    (doc,) = AgentMailAdapter(checkpoint_db=str(tmp_path / "e.db")).fetch()
    assert "only html" in doc.text
    assert doc.meta["thread_id"] == "t9"


# --- POST /inbox + watch pruning ----------------------------------------------


def _fresh_api_client(tmp_path, monkeypatch):
    """Reload brain.api with a clean env — earlier auth tests may have left
    the module loaded with a bearer token."""
    import importlib

    from fastapi.testclient import TestClient

    monkeypatch.setenv("BRAIN_INBOX_DIR", str(tmp_path / "drop"))
    monkeypatch.setenv("BRAIN_DB", str(tmp_path / "lance"))
    monkeypatch.setenv("BRAIN_ENTDB", str(tmp_path / "e.db"))
    monkeypatch.setenv("BRAIN_EMBEDDER", "fake")
    monkeypatch.delenv("BRAIN_BEARER_TOKEN", raising=False)
    import brain.api as api
    importlib.reload(api)
    return TestClient(api.app)


def test_post_inbox_writes_drop_file(tmp_path, monkeypatch):
    client = _fresh_api_client(tmp_path, monkeypatch)
    r = client.post("/inbox", json={"text": "forwarded text body",
                                     "title": "From Messages",
                                     "source_hint": "ios-shortcut"})
    assert r.status_code == 200
    name = r.json()["saved"]
    saved = tmp_path / "drop" / name
    assert saved.exists()
    content = saved.read_text(encoding="utf-8")
    assert content.startswith("# From Messages")
    assert "forwarded text body" in content
    assert "ios-shortcut" in content
    # And the inbox adapter picks it up.
    (doc,) = InboxAdapter(str(tmp_path / "drop")).fetch()
    assert "forwarded text body" in doc.text


def test_post_inbox_validation(tmp_path, monkeypatch):
    client = _fresh_api_client(tmp_path, monkeypatch)
    assert client.post("/inbox", json={"text": ""}).status_code == 422


def test_watch_cycle_prunes_empty_ledger_rows(tmp_path, capsys):
    """cmd_ingest with prune_empty leaves no row for a nothing-to-do cycle,
    but keeps rows for cycles that ingested."""
    from brain.cli import cmd_ingest

    d = _inbox(tmp_path)
    db, entdb = str(tmp_path / "lance"), str(tmp_path / "e.db")

    def _ns() -> argparse.Namespace:
        return argparse.Namespace(
            adapter="inbox", source=str(d), db=db, entdb=entdb,
            embedder="fake", dry_run=False, exclude=None,
            llm_classifier=False, prune_empty=True,
        )

    assert cmd_ingest(_ns()) == 0
    assert IngestLedger(entdb).runs() == []  # empty cycle -> no row

    (d / "drop.md").write_text("# hi\n\ncontent", encoding="utf-8")
    assert cmd_ingest(_ns()) == 0
    capsys.readouterr()
    runs = IngestLedger(entdb).runs()
    assert len(runs) == 1 and runs[0]["status"] == "completed"
    assert runs[0]["chunks"] >= 1
    assert BrainIndex(db, FakeEmbedder()).count() >= 1
    # Clean run committed the move.
    assert not (d / "drop.md").exists()
    assert list((d / "processed").rglob("drop.md"))
