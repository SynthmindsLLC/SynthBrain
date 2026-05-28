"""iMessage adapter tests — build a synthetic chat.db; never touch real one."""

from __future__ import annotations

import sqlite3
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from brain.adapters.imessage_adapter import (
    IMessageAdapter,
    _apple_ns_to_datetime,
    _datetime_to_apple_ns,
)
from brain.core.checkpoint import CheckpointStore


def _build_fake_chatdb(path: Path) -> None:
    conn = sqlite3.connect(str(path))
    conn.executescript(
        """
        CREATE TABLE chat (
            ROWID INTEGER PRIMARY KEY,
            guid TEXT,
            display_name TEXT,
            chat_identifier TEXT,
            style INTEGER
        );
        CREATE TABLE handle (
            ROWID INTEGER PRIMARY KEY,
            id TEXT,
            country TEXT
        );
        CREATE TABLE message (
            ROWID INTEGER PRIMARY KEY,
            text TEXT,
            attributedBody BLOB,
            handle_id INTEGER,
            date INTEGER,
            is_from_me INTEGER
        );
        CREATE TABLE chat_message_join (
            chat_id INTEGER,
            message_id INTEGER
        );
        CREATE TABLE chat_handle_join (
            chat_id INTEGER,
            handle_id INTEGER
        );
        """
    )
    conn.commit()
    conn.close()


def _now_ns() -> int:
    return _datetime_to_apple_ns(datetime.now(timezone.utc))


def _add_chat(conn, *, chat_id, guid, display, identifier, style=45):
    conn.execute(
        "INSERT INTO chat (ROWID, guid, display_name, chat_identifier, style) VALUES (?,?,?,?,?)",
        (chat_id, guid, display, identifier, style),
    )


def _add_handle(conn, *, handle_id, identifier):
    conn.execute("INSERT INTO handle (ROWID, id, country) VALUES (?,?, '')",
                 (handle_id, identifier))


def _add_message(conn, *, msg_id, text, handle_id, date_ns, is_from_me, attributed=None):
    conn.execute(
        "INSERT INTO message (ROWID, text, attributedBody, handle_id, date, is_from_me) VALUES (?,?,?,?,?,?)",
        (msg_id, text, attributed, handle_id, date_ns, is_from_me),
    )


def _link_message(conn, *, chat_id, message_id):
    conn.execute(
        "INSERT INTO chat_message_join (chat_id, message_id) VALUES (?,?)",
        (chat_id, message_id),
    )


def test_extracts_chat_into_speakered_chunks():
    with tempfile.TemporaryDirectory() as d:
        db_path = Path(d) / "chat.db"
        _build_fake_chatdb(db_path)
        conn = sqlite3.connect(str(db_path))
        _add_chat(conn, chat_id=1, guid="iMessage;-;jeff@acme.com",
                  display="Jeff Torres", identifier="jeff@acme.com")
        _add_handle(conn, handle_id=11, identifier="jeff@acme.com")
        base = _now_ns() - 1_000_000_000  # 1s ago
        _add_message(conn, msg_id=101, text="hey", handle_id=None,
                     date_ns=base, is_from_me=1)
        _add_message(conn, msg_id=102, text="sup", handle_id=11,
                     date_ns=base + 1_000, is_from_me=0)
        _add_message(conn, msg_id=103, text="lunch tomorrow?", handle_id=None,
                     date_ns=base + 2_000, is_from_me=1)
        _add_message(conn, msg_id=104, text="yeah let's do it", handle_id=11,
                     date_ns=base + 3_000, is_from_me=0)
        for mid in (101, 102, 103, 104):
            _link_message(conn, chat_id=1, message_id=mid)
        conn.commit()
        conn.close()

        docs = list(IMessageAdapter(
            db_path=str(db_path),
            since_days=7,
            words_per_group=200,
        ).fetch())
    assert len(docs) == 1
    doc = docs[0]
    assert doc.source == "imessage"
    assert doc.source_id.startswith("chat:iMessage;-;jeff@acme.com:")
    assert "me: hey" in doc.text
    assert "jeff@acme.com: sup" in doc.text
    assert "lunch tomorrow?" in doc.text
    assert doc.meta["participants"] == ["jeff@acme.com"]


def test_attributedbody_fallback_when_text_is_null():
    """Recent macOS stores body in attributedBody as a binary plist; we scrape
    the longest printable run."""
    with tempfile.TemporaryDirectory() as d:
        db_path = Path(d) / "chat.db"
        _build_fake_chatdb(db_path)
        conn = sqlite3.connect(str(db_path))
        _add_chat(conn, chat_id=1, guid="g", display="Test", identifier="test")
        _add_handle(conn, handle_id=11, identifier="test@example.com")
        # Fake attributedBody with a real message buried among Apple class
        # markers; the extractor should pick the readable run.
        blob = (
            b"streamtyped" + b"\x84\x01@\x84\x84\x84"
            b"NSAttributedStringNSObject"
            b"\x86NSDictionary"
            b"The maritime conservation roadmap is on track"
            b"\x86NSDictionary"
        )
        _add_message(conn, msg_id=200, text=None, attributed=blob,
                     handle_id=11, date_ns=_now_ns() - 1_000, is_from_me=0)
        _link_message(conn, chat_id=1, message_id=200)
        conn.commit()
        conn.close()

        docs = list(IMessageAdapter(
            db_path=str(db_path),
            since_days=1,
            words_per_group=200,
        ).fetch())
    assert len(docs) == 1
    assert "maritime conservation roadmap" in docs[0].text


def test_watermark_skips_messages_before_since_days():
    with tempfile.TemporaryDirectory() as d:
        db_path = Path(d) / "chat.db"
        _build_fake_chatdb(db_path)
        conn = sqlite3.connect(str(db_path))
        _add_chat(conn, chat_id=1, guid="g", display="A", identifier="a")
        old_ns = _datetime_to_apple_ns(datetime.now(timezone.utc) - timedelta(days=30))
        new_ns = _now_ns() - 1_000
        _add_message(conn, msg_id=1, text="ancient", handle_id=None,
                     date_ns=old_ns, is_from_me=1)
        _add_message(conn, msg_id=2, text="recent", handle_id=None,
                     date_ns=new_ns, is_from_me=1)
        for mid in (1, 2):
            _link_message(conn, chat_id=1, message_id=mid)
        conn.commit()
        conn.close()

        docs = list(IMessageAdapter(
            db_path=str(db_path),
            since_days=7,           # 7-day backfill -> drops the 30-day-old one
            words_per_group=50,
        ).fetch())
    full = "\n\n".join(d.text for d in docs)
    assert "recent" in full
    assert "ancient" not in full


def test_checkpoint_advances_after_run():
    with tempfile.TemporaryDirectory() as d:
        db_path = Path(d) / "chat.db"
        _build_fake_chatdb(db_path)
        conn = sqlite3.connect(str(db_path))
        _add_chat(conn, chat_id=1, guid="g", display="A", identifier="a")
        ns = _now_ns() - 1_000
        _add_message(conn, msg_id=1, text="hello", handle_id=None,
                     date_ns=ns, is_from_me=1)
        _link_message(conn, chat_id=1, message_id=1)
        conn.commit()
        conn.close()

        cp_db = str(Path(d) / "e.db")
        list(IMessageAdapter(
            db_path=str(db_path), checkpoint_db=cp_db,
            since_days=1, words_per_group=10,
        ).fetch())
        saved = CheckpointStore(cp_db).get("imessage")
        assert saved and int(saved) >= ns


def test_groups_split_at_word_budget():
    """Force two output docs by setting a tiny budget."""
    with tempfile.TemporaryDirectory() as d:
        db_path = Path(d) / "chat.db"
        _build_fake_chatdb(db_path)
        conn = sqlite3.connect(str(db_path))
        _add_chat(conn, chat_id=1, guid="g", display="A", identifier="a")
        base = _now_ns() - 10_000
        for i in range(20):
            _add_message(conn, msg_id=i + 1,
                         text=" ".join(["word"] * 8),
                         handle_id=None,
                         date_ns=base + i, is_from_me=(i % 2))
            _link_message(conn, chat_id=1, message_id=i + 1)
        conn.commit()
        conn.close()

        docs = list(IMessageAdapter(
            db_path=str(db_path),
            since_days=1,
            words_per_group=20,
        ).fetch())
    assert len(docs) >= 2


def test_apple_epoch_round_trip():
    dt = datetime(2026, 5, 28, 12, 34, 56, tzinfo=timezone.utc)
    ns = _datetime_to_apple_ns(dt)
    out = _apple_ns_to_datetime(ns)
    assert abs((out - dt).total_seconds()) < 1.0


def test_raises_when_db_path_missing():
    import pytest
    with pytest.raises(FileNotFoundError):
        IMessageAdapter(db_path="/nope/never/here.db")
