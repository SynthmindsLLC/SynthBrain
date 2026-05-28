"""M365 (Graph API) adapter tests — patch HTTP, never touch the network."""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from brain.adapters.m365_adapter import M365Adapter, M365AuthError
from brain.core.checkpoint import CheckpointStore


@pytest.fixture(autouse=True)
def _env(monkeypatch):
    monkeypatch.setenv("MS_CLIENT_ID", "test-client")
    monkeypatch.setenv("MS_REFRESH_TOKEN", "rt")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)


def _patch_mint(_self):
    return "access-token-stub"


SAMPLE_MAIL = {
    "value": [
        {
            "id": "msg_personal",
            "from": {"emailAddress": {"address": "jeff@acme.com", "name": "Jeff Torres"}},
            "toRecipients": [{"emailAddress": {"address": "wes@synthminds.ai"}}],
            "subject": "lunch tomorrow?",
            "body": {"contentType": "text", "content": "Hey, free for lunch?"},
            "receivedDateTime": "2026-05-28T10:00:00Z",
            "internetMessageHeaders": [],
        },
        {
            "id": "msg_marketing",
            "from": {"emailAddress": {"address": "newsletter@brandx.com"}},
            "toRecipients": [{"emailAddress": {"address": "wes@synthminds.ai"}}],
            "subject": "50% off — view in browser",
            "body": {"contentType": "html", "content": "<p>Click to unsubscribe</p>"},
            "receivedDateTime": "2026-05-28T11:00:00Z",
            "internetMessageHeaders": [
                {"name": "List-Unsubscribe", "value": "<https://brandx.com/unsub>"}
            ],
        },
    ],
    "@odata.deltaLink": "https://graph.example.com/me/messages/delta?$deltatoken=NEW",
}

SAMPLE_CAL = {
    "value": [
        {
            "id": "ev_1",
            "subject": "Q3 review",
            "start": {"dateTime": "2026-06-01T15:00:00Z"},
            "end": {"dateTime": "2026-06-01T16:00:00Z"},
            "location": {"displayName": "Conf Room A"},
            "lastModifiedDateTime": "2026-05-28T09:00:00Z",
            "attendees": [
                {"emailAddress": {"address": "jeff@acme.com", "name": "Jeff Torres"}},
            ],
            "body": {"contentType": "text", "content": "Quarterly checkpoint."},
            "webLink": "https://outlook.office.com/calendar/item/ev_1",
        }
    ]
}


def test_raises_when_credentials_missing(monkeypatch):
    monkeypatch.delenv("MS_CLIENT_ID")
    with pytest.raises(M365AuthError):
        M365Adapter("mail")


def test_mail_run_filters_marketing_keeps_personal():
    """End-to-end: refresh-token mint, mail fetch, filter applied."""
    with patch.object(M365Adapter, "_mint_access_token", new=_patch_mint), \
         patch.object(M365Adapter, "_get_url", return_value=SAMPLE_MAIL):
        docs = list(M365Adapter(
            "mail",
            llm_tiebreaker=False,
            own_domains=["synthminds.ai", "acme.com"],
        ).fetch())
    ids = {d.source_id for d in docs}
    assert ids == {"msg_personal"}
    assert "lunch" in docs[0].text.lower()


def test_mail_delta_link_is_persisted():
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch.object(M365Adapter, "_mint_access_token", new=_patch_mint), \
             patch.object(M365Adapter, "_get_url", return_value=SAMPLE_MAIL):
            list(M365Adapter(
                "mail", checkpoint_db=cp_db, llm_tiebreaker=False,
                own_domains=["synthminds.ai", "acme.com"],
            ).fetch())
        saved = CheckpointStore(cp_db).get("m365", key="mail_delta")
        assert saved == "https://graph.example.com/me/messages/delta?$deltatoken=NEW"


def test_calendar_emits_doc_with_attendees_and_location():
    with patch.object(M365Adapter, "_mint_access_token", new=_patch_mint), \
         patch.object(M365Adapter, "_get_url", return_value=SAMPLE_CAL):
        docs = list(M365Adapter("calendar", llm_tiebreaker=False).fetch())
    assert len(docs) == 1
    d = docs[0]
    assert d.source == "m365"
    assert d.source_id == "ev_1"
    assert "Q3 review" in d.text
    assert "Conf Room A" in d.text
    assert "Jeff Torres" in d.text or "Jeff Torres" in " ".join(d.meta["attendees"])


def test_calendar_watermark_advances():
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch.object(M365Adapter, "_mint_access_token", new=_patch_mint), \
             patch.object(M365Adapter, "_get_url", return_value=SAMPLE_CAL):
            list(M365Adapter("calendar", checkpoint_db=cp_db).fetch())
        saved = CheckpointStore(cp_db).get("m365", key="calendar_watermark")
        assert saved == "2026-05-28T09:00:00Z"


def test_invalid_source_kind_raises():
    with pytest.raises(ValueError):
        M365Adapter("contacts")
