"""IMAP adapter tests — fake the IMAP4_SSL connection end-to-end."""

from __future__ import annotations

import tempfile
from email.message import EmailMessage
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


def _make_raw(*, from_addr: str, subject: str, body: str,
              date: str = "Thu, 28 May 2026 12:00:00 +0000",
              mid: str = "<abc@test>",
              extra_headers: dict | None = None) -> bytes:
    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = "wes@synthminds.ai"
    msg["Subject"] = subject
    msg["Date"] = date
    msg["Message-ID"] = mid
    if extra_headers:
        for k, v in extra_headers.items():
            msg[k] = v
    msg.set_content(body)
    return msg.as_bytes()


class FakeIMAP:
    """Minimal stand-in for imaplib.IMAP4_SSL."""

    def __init__(self, raw_by_uid: dict[int, bytes], uidvalidity: str = "1000"):
        self._raw = raw_by_uid
        self._uidvalidity = uidvalidity

    def login(self, user, pw):  # noqa: ARG002
        return ("OK", [b""])

    def select(self, folder, readonly=False):  # noqa: ARG002
        return ("OK", [b""])

    def response(self, name):
        if name == "UIDVALIDITY":
            return ("OK", [self._uidvalidity.encode()])
        return ("OK", [])

    def status(self, *_args):
        return ("OK", [f"INBOX (UIDVALIDITY {self._uidvalidity})".encode()])

    def uid(self, command, *args):
        if command == "SEARCH":
            return ("OK", [" ".join(str(u) for u in sorted(self._raw)).encode()])
        if command == "FETCH":
            uid = int(args[0])
            raw = self._raw.get(uid)
            if not raw:
                return ("OK", [None])
            return ("OK", [(f"{uid} (BODY[] {{{len(raw)}}}".encode(), raw)])
        return ("BAD", [])

    def logout(self):
        return ("OK", [b""])

    @property
    def state(self):
        return "SELECTED"


@pytest.fixture(autouse=True)
def _env(monkeypatch):
    monkeypatch.setenv("IMAP_USERNAME", "wes@me.com")
    monkeypatch.setenv("IMAP_PASSWORD", "app-specific-pw")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)


def test_imap_filters_marketing_keeps_personal(monkeypatch):
    raws = {
        1: _make_raw(
            from_addr="Jeff Torres <jeff@acme.com>",
            subject="lunch?",
            body="Hey, free for lunch next week?",
        ),
        2: _make_raw(
            from_addr="noreply@store.com",
            subject="50% off!",
            body="Click here to unsubscribe.",
            extra_headers={"List-Unsubscribe": "<https://store.com/unsub>"},
        ),
    }
    fake = FakeIMAP(raws)
    from brain.adapters.imap_adapter import IMAPAdapter

    with tempfile.TemporaryDirectory() as d:
        from brain.core.entities import Entity, EntityStore
        entdb = str(Path(d) / "e.db")
        store = EntityStore(entdb)
        store.upsert_entity(Entity(
            kind="person", name="Jeff Torres",
            attributes={"emails": ["jeff@acme.com"]},
        ))
        with patch("imaplib.IMAP4_SSL", return_value=fake):
            docs = list(IMAPAdapter(
                checkpoint_db=entdb, entdb=entdb,
                llm_tiebreaker=False, own_domains=["synthminds.ai"],
            ).fetch())
        assert len(docs) == 1
        assert "lunch" in docs[0].text.lower()


def test_imap_advances_uid_checkpoint():
    raws = {
        5: _make_raw(from_addr="wes@synthminds.ai", subject="ok", body="ok"),
        7: _make_raw(from_addr="wes@synthminds.ai", subject="ok2", body="ok2"),
    }
    fake = FakeIMAP(raws, uidvalidity="2222")
    from brain.adapters.imap_adapter import IMAPAdapter
    from brain.core.checkpoint import CheckpointStore

    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch("imaplib.IMAP4_SSL", return_value=fake):
            list(IMAPAdapter(
                checkpoint_db=cp_db, llm_tiebreaker=False,
                own_domains=["synthminds.ai"],
            ).fetch())
        saved = CheckpointStore(cp_db).get("imap", key="uid::INBOX")
        assert saved == "2222:7"


def test_imap_skips_already_seen_uids():
    """Second run with the same checkpoint should yield nothing."""
    raws = {3: _make_raw(from_addr="wes@synthminds.ai", subject="a", body="a")}
    fake = FakeIMAP(raws, uidvalidity="9")
    from brain.adapters.imap_adapter import IMAPAdapter

    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch("imaplib.IMAP4_SSL", return_value=fake):
            first = list(IMAPAdapter(
                checkpoint_db=cp_db, llm_tiebreaker=False,
                own_domains=["synthminds.ai"],
            ).fetch())
            second = list(IMAPAdapter(
                checkpoint_db=cp_db, llm_tiebreaker=False,
                own_domains=["synthminds.ai"],
            ).fetch())
        assert len(first) == 1
        assert second == []


def test_imap_raises_when_credentials_missing(monkeypatch):
    monkeypatch.delenv("IMAP_PASSWORD")
    from brain.adapters.imap_adapter import IMAPAdapter
    with pytest.raises(RuntimeError, match="IMAP_USERNAME"):
        IMAPAdapter()
