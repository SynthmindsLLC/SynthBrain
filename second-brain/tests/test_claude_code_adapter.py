"""Claude Code session adapter tests — synthetic JSONL fixtures, offline."""

from __future__ import annotations

import json
import os
from pathlib import Path

from brain.adapters.claude_code_adapter import (
    MAX_DOC_CHARS,
    TRUNCATION_MARKER,
    ClaudeCodeAdapter,
)
from brain.core.checkpoint import CheckpointStore


def _user(text) -> dict:
    return {"type": "user", "message": {"role": "user", "content": text}}


def _assistant(content) -> dict:
    return {"type": "assistant", "message": {"role": "assistant", "content": content}}


def _write_session(root: Path, project: str, stem: str, events, mtime: float | None = None) -> Path:
    d = root / project
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{stem}.jsonl"
    lines = [e if isinstance(e, str) else json.dumps(e) for e in events]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if mtime is not None:
        os.utime(path, (mtime, mtime))
    return path


def test_renders_session_in_speaker_idiom(tmp_path):
    _write_session(tmp_path, "my-proj", "sess-1", [
        _user("hello brain"),
        _assistant([{"type": "text", "text": "hi there"}]),
        _user([{"type": "text", "text": "block-style user text"}]),
    ])
    docs = list(ClaudeCodeAdapter(str(tmp_path)).fetch())
    assert len(docs) == 1
    doc = docs[0]
    assert doc.source == "claude-code"
    assert doc.source_id == "sess-1"
    assert doc.url == ""
    assert doc.created_at.tzinfo is not None
    assert doc.text.startswith("# Claude Code — my-proj — sess-1")
    assert "**user:** hello brain" in doc.text
    assert "**assistant:** hi there" in doc.text
    assert "**user:** block-style user text" in doc.text
    assert doc.meta["project"] == "my-proj"
    assert doc.meta["messages"] == 3
    assert doc.meta["truncated"] is False


def test_skips_meta_lines_tool_blocks_and_bad_json(tmp_path):
    _write_session(tmp_path, "proj", "sess", [
        {"type": "last-prompt", "leafUuid": "x"},
        {"type": "file-history-snapshot", "snapshot": {}},
        _user("real question"),
        _assistant([
            {"type": "thinking", "thinking": "private"},
            {"type": "tool_use", "id": "t1", "name": "Bash", "input": {"command": "ls"}},
        ]),
        _user([{"type": "tool_result", "tool_use_id": "t1", "content": "file.txt"}]),
        _assistant([{"type": "text", "text": "real answer"}]),
        "this is {not json",
        _user("   "),
        {"type": "user", "message": "not-a-dict"},
    ])
    adapter = ClaudeCodeAdapter(str(tmp_path))
    docs = list(adapter.fetch())
    assert len(docs) == 1
    text = docs[0].text
    assert "**user:** real question" in text
    assert "**assistant:** real answer" in text
    assert "private" not in text
    assert "tool_use" not in text
    assert "file.txt" not in text
    assert docs[0].meta["messages"] == 2
    assert adapter.skip_report["bad_line"]["count"] == 1
    assert adapter.skip_report["bad_line"]["samples"][0].endswith(":7")


def test_session_with_no_messages_is_skipped_as_empty(tmp_path):
    _write_session(tmp_path, "proj", "meta-only", [
        {"type": "mode", "mode": "normal"},
        {"type": "ai-title", "title": "x"},
    ])
    adapter = ClaudeCodeAdapter(str(tmp_path))
    assert list(adapter.fetch()) == []
    assert adapter.skip_report["empty"]["count"] == 1


def test_excludes_defaults_node_modules_and_custom_terms(tmp_path):
    _write_session(tmp_path, "good", "s1", [_user("keep me")])
    _write_session(tmp_path, "alltheplants", "s2", [_user("not mine")])
    _write_session(tmp_path, "-Users-x-node_modules-dep", "s3", [_user("vendored")])
    _write_session(tmp_path, "secret-proj", "s4", [_user("excluded by flag")])

    default = ClaudeCodeAdapter(str(tmp_path))
    ids = [d.source_id for d in default.fetch()]
    assert ids == ["s1", "s4"]
    assert default.skip_report["excluded"]["count"] == 2

    # Custom terms ADD to the defaults — alltheplants stays excluded.
    custom = ClaudeCodeAdapter(str(tmp_path), exclude=["secret"])
    ids = [d.source_id for d in custom.fetch()]
    assert ids == ["s1"]
    assert custom.skip_report["excluded"]["count"] == 3


def test_mtime_checkpoint_advances_and_skips_seen_sessions(tmp_path):
    cp_db = str(tmp_path / "e.db")
    root = tmp_path / "projects"
    path = _write_session(root, "proj", "s1", [_user("v1")], mtime=1_700_000_000)

    a = ClaudeCodeAdapter(str(root), checkpoint_db=cp_db)
    assert len(list(a.fetch())) == 1
    assert CheckpointStore(cp_db).get("claude-code", a.checkpoint_key) is not None

    # Fresh instance, same root: watermark suppresses the unchanged session.
    b = ClaudeCodeAdapter(str(root), checkpoint_db=cp_db)
    assert list(b.fetch()) == []

    # Touch the session newer than the watermark: it flows again.
    os.utime(path, (1_700_000_500, 1_700_000_500))
    c = ClaudeCodeAdapter(str(root), checkpoint_db=cp_db)
    assert len(list(c.fetch())) == 1


def test_two_roots_do_not_share_a_watermark(tmp_path):
    cp_db = str(tmp_path / "e.db")
    root_a, root_b = tmp_path / "a", tmp_path / "b"
    _write_session(root_a, "p", "s1", [_user("alpha")])
    _write_session(root_b, "p", "s2", [_user("beta")])

    a = ClaudeCodeAdapter(str(root_a), checkpoint_db=cp_db)
    assert len(list(a.fetch())) == 1
    b = ClaudeCodeAdapter(str(root_b), checkpoint_db=cp_db)
    assert len(list(b.fetch())) == 1
    assert a.checkpoint_key != b.checkpoint_key


def test_oversized_session_truncates_with_marker(tmp_path):
    big = "x" * (MAX_DOC_CHARS + 10_000)
    _write_session(tmp_path, "proj", "huge", [
        _user("small opener"),
        _assistant([{"type": "text", "text": big}]),
        _user("never rendered"),
    ])
    docs = list(ClaudeCodeAdapter(str(tmp_path)).fetch())
    assert len(docs) == 1
    doc = docs[0]
    assert doc.meta["truncated"] is True
    assert doc.text.endswith(TRUNCATION_MARKER.strip())
    assert "never rendered" not in doc.text
    assert len(doc.text) <= MAX_DOC_CHARS + len(TRUNCATION_MARKER) + 2


def test_missing_root_raises(tmp_path):
    import pytest

    with pytest.raises(FileNotFoundError):
        ClaudeCodeAdapter(str(tmp_path / "nope"))


def test_cli_registration_and_e2e_ingest(tmp_path, capsys):
    from brain.cli import ADAPTERS, main
    from brain.core.embed import FakeEmbedder
    from brain.core.index import BrainIndex
    from brain.core.ledger import IngestLedger

    assert "claude-code" in ADAPTERS
    root = tmp_path / "projects"
    _write_session(root, "proj", "s1", [
        _user("we decided to use LanceDB because it is local"),
        _assistant([{"type": "text", "text": "logged the decision"}]),
    ])
    db = str(tmp_path / "lance")
    entdb = str(tmp_path / "e.db")
    assert main(["--db", db, "--entdb", entdb, "ingest",
                 "--adapter", "claude-code", "--source", str(root)]) == 0
    capsys.readouterr()
    assert BrainIndex(db, FakeEmbedder()).count() >= 1
    runs = IngestLedger(entdb).runs()
    assert runs[0]["adapter"] == "claude-code"
    assert runs[0]["status"] == "completed"
    # Second run: watermark makes it a no-op.
    assert main(["--db", db, "--entdb", entdb, "ingest",
                 "--adapter", "claude-code", "--source", str(root)]) == 0
    capsys.readouterr()
    runs = IngestLedger(entdb).runs()
    assert runs[0]["chunks"] == 0
