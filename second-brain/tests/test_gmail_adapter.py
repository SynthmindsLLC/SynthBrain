"""Gmail adapter tests — mock the Gmail API service end-to-end."""

from __future__ import annotations

import base64
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from brain.adapters.gmail_adapter import GmailAdapter
from brain.core.checkpoint import CheckpointStore


@pytest.fixture(autouse=True)
def _env(monkeypatch):
    monkeypatch.setenv("GOOGLE_OAUTH_CLIENT_ID", "id")
    monkeypatch.setenv("GOOGLE_OAUTH_CLIENT_SECRET", "secret")
    monkeypatch.setenv("GOOGLE_OAUTH_REFRESH_TOKEN", "refresh")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)


def _b64(s: str) -> str:
    return base64.urlsafe_b64encode(s.encode("utf-8")).decode("ascii").rstrip("=")


def _msg(*, id: str, from_addr: str, subject: str, body: str,
         headers_extra=None, internal_date_ms: int = 1748419200000) -> dict:
    headers = [
        {"name": "From", "value": from_addr},
        {"name": "Subject", "value": subject},
        {"name": "To", "value": "wes@synthminds.ai"},
    ]
    if headers_extra:
        headers.extend(headers_extra)
    return {
        "id": id,
        "threadId": f"thr_{id}",
        "historyId": str(int(id.split("_")[-1]) if "_" in id else 1),
        "internalDate": str(internal_date_ms),
        "labelIds": ["INBOX"],
        "payload": {
            "mimeType": "text/plain",
            "headers": headers,
            "body": {"data": _b64(body)},
        },
    }


def _fake_service(messages: list[dict], history_id_after: str = "100"):
    """Build a MagicMock Gmail service returning the supplied messages on
    the first list call, then nothing."""
    # list page
    list_pages = [{"messages": [{"id": m["id"]} for m in messages]}, {"messages": []}]
    list_calls = {"n": 0}

    def messages_list(**kwargs):
        i = list_calls["n"]
        list_calls["n"] += 1
        page = list_pages[i] if i < len(list_pages) else {"messages": []}
        m = MagicMock(); m.execute.return_value = page
        return m

    msg_by_id = {m["id"]: m for m in messages}

    def messages_get(*, userId, id, format):
        m = MagicMock(); m.execute.return_value = msg_by_id[id]
        return m

    msgs = MagicMock()
    msgs.list = messages_list
    msgs.get = messages_get

    profile = MagicMock(); profile.execute.return_value = {"historyId": history_id_after}
    users = MagicMock()
    users.messages.return_value = msgs
    users.getProfile = MagicMock(return_value=profile)

    history_mock = MagicMock()
    history_mock.list = MagicMock(return_value=MagicMock(
        execute=MagicMock(return_value={"history": []})
    ))
    users.history.return_value = history_mock

    service = MagicMock()
    service.users.return_value = users
    return service


def test_marketing_message_is_dropped_personal_kept():
    messages = [
        _msg(id="m_1", from_addr="Jeff Torres <jeff@acme.com>",
             subject="lunch next week?", body="Hey, free for lunch?"),
        _msg(id="m_2", from_addr="noreply@store.com",
             subject="50% off everything", body="Click here to unsubscribe."),
    ]
    service = _fake_service(messages)
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch("brain.adapters.gmail_adapter._gmail_service", return_value=service):
            docs = list(GmailAdapter(checkpoint_db=cp_db, llm_tiebreaker=False,
                                     own_domains=["acme.com"]).fetch())
        assert len(docs) == 1
        assert docs[0].source_id == "m_1"
        assert "lunch" in docs[0].text.lower()


def test_allowlist_from_brain_keeps_unknown_domain_sender():
    """A sender not on our own domain still passes if their email is in
    the brain's Person.aliases / emails (i.e. you have them as a contact)."""
    from brain.core.entities import Entity, EntityStore
    messages = [
        _msg(id="m_1", from_addr="ali@randomperson.io",
             subject="trip planning", body="we should meet"),
    ]
    service = _fake_service(messages)
    with tempfile.TemporaryDirectory() as d:
        entdb = str(Path(d) / "e.db")
        store = EntityStore(entdb)
        store.upsert_entity(Entity(
            kind="person", name="Ali B",
            attributes={"emails": ["ali@randomperson.io"]},
        ))
        with patch("brain.adapters.gmail_adapter._gmail_service", return_value=service):
            docs = list(GmailAdapter(
                checkpoint_db=entdb, entdb=entdb,
                llm_tiebreaker=False, own_domains=[],
            ).fetch())
        assert [d.source_id for d in docs] == ["m_1"]


def test_history_id_is_persisted_after_run():
    messages = [_msg(id="m_5", from_addr="x@synthminds.ai", subject="ok", body="ok")]
    service = _fake_service(messages, history_id_after="999")
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch("brain.adapters.gmail_adapter._gmail_service", return_value=service):
            list(GmailAdapter(checkpoint_db=cp_db, llm_tiebreaker=False,
                              own_domains=["synthminds.ai"]).fetch())
        # latest message's historyId wins over profile's
        assert CheckpointStore(cp_db).get("gmail", key="history_id") == "5"


def test_html_only_body_is_extracted_as_text():
    msg = {
        "id": "h_1",
        "threadId": "h",
        "historyId": "1",
        "internalDate": "1748419200000",
        "labelIds": ["INBOX"],
        "payload": {
            "mimeType": "multipart/alternative",
            "headers": [
                {"name": "From", "value": "real@synthminds.ai"},
                {"name": "Subject", "value": "html msg"},
            ],
            "body": {},
            "parts": [
                {"mimeType": "text/html",
                 "body": {"data": _b64("<p>Hello <b>Wes</b></p>")}},
            ],
        },
    }
    service = _fake_service([msg])
    with patch("brain.adapters.gmail_adapter._gmail_service", return_value=service):
        docs = list(GmailAdapter(llm_tiebreaker=False,
                                 own_domains=["synthminds.ai"]).fetch())
    assert len(docs) == 1
    assert "Hello Wes" in docs[0].text


def test_quoted_reply_trailer_is_stripped():
    """Verify the quoted-reply stripper runs before chunking. Sender added
    to the brain's Person nodes so the filter keeps the message."""
    from brain.core.entities import Entity, EntityStore
    body = (
        "Sure, let's grab lunch.\n\n"
        "On Mon, May 28, 2026, Wes <wes@synthminds.ai> wrote:\n"
        "> hey, free for lunch?\n"
    )
    service = _fake_service([_msg(id="q_1", from_addr="jeff@acme.com",
                                  subject="re: lunch", body=body)])
    with tempfile.TemporaryDirectory() as d:
        entdb = str(Path(d) / "e.db")
        store = EntityStore(entdb)
        store.upsert_entity(Entity(
            kind="person", name="Jeff Torres",
            attributes={"emails": ["jeff@acme.com"]},
        ))
        with patch("brain.adapters.gmail_adapter._gmail_service", return_value=service):
            docs = list(GmailAdapter(
                entdb=entdb, llm_tiebreaker=False, own_domains=["synthminds.ai"],
            ).fetch())
        assert len(docs) == 1
        assert "Sure, let's grab lunch." in docs[0].text
        assert "hey, free for lunch?" not in docs[0].text
