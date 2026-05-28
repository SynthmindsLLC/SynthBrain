"""Email filter tests — the personal/work-only triage."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from brain.core.email_filter import (
    Decision,
    EmailMeta,
    classify_email,
)


def _msg(**kw) -> EmailMeta:
    base = {
        "from_addr": "", "from_name": "",
        "to_addrs": [], "subject": "", "body": "", "headers": {},
    }
    base.update(kw)
    return EmailMeta(**base)


# ---- hard drops ----------------------------------------------------------

def test_list_unsubscribe_header_drops_immediately(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    v = classify_email(_msg(
        from_addr="real-human@friend.com",
        subject="Hey",
        headers={"List-Unsubscribe": "<https://example.com/unsub>"},
    ))
    assert v.decision is Decision.DROP
    assert v.stage == "list-unsubscribe"


def test_noreply_local_part_drops():
    v = classify_email(_msg(from_addr="noreply@bigco.com", subject="Receipt"))
    assert v.decision is Decision.DROP
    assert v.stage == "hard-block-local"


def test_esp_domain_drops():
    v = classify_email(_msg(from_addr="alex@stuff.mailchimp.com", subject="newsletter"))
    assert v.decision is Decision.DROP
    assert v.stage == "hard-block-domain"


def test_subject_unsubscribe_pattern_drops():
    v = classify_email(_msg(
        from_addr="real@friend.com",
        subject="50% off! View in browser to unsubscribe",
    ))
    assert v.decision is Decision.DROP
    assert v.stage == "hard-block-subject"


def test_body_unsubscribe_boilerplate_drops():
    v = classify_email(_msg(
        from_addr="real@somesite.com",
        subject="Update",
        body="Hello. You are receiving this email because you opted in.",
    ))
    assert v.decision is Decision.DROP
    assert v.stage == "hard-block-body"


# ---- keeps ---------------------------------------------------------------

def test_sender_in_allowlist_is_kept():
    v = classify_email(
        _msg(from_addr="Jeff.Torres@acme.com", subject="lunch?"),
        allowlist=["jeff.torres@acme.com"],
    )
    assert v.decision is Decision.KEEP
    assert v.label == "personal"
    assert v.stage == "allowlist"


def test_own_domain_sender_is_kept_as_work():
    v = classify_email(
        _msg(from_addr="colleague@synthminds.ai", subject="status"),
        own_domains=["synthminds.ai"],
    )
    assert v.decision is Decision.KEEP
    assert v.label == "work"


def test_transactional_pattern_is_kept_even_without_allowlist():
    v = classify_email(_msg(
        from_addr="receipts@somestore.com",
        subject="Receipt for your order #4821",
        body="Total: $42.00",
    ))
    assert v.decision is Decision.KEEP
    assert v.label == "transactional"


# ---- default-drop --------------------------------------------------------

def test_unknown_sender_with_no_signal_drops_by_default(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    v = classify_email(_msg(
        from_addr="someone@unknown.com",
        subject="Hi there",
        body="Just reaching out.",
    ))
    assert v.decision is Decision.DROP
    assert v.stage == "default"


# ---- LLM tiebreaker ------------------------------------------------------

def test_llm_tiebreaker_returns_personal_keeps_message(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    with patch("brain.core.email_filter._llm_label", return_value="personal"):
        v = classify_email(_msg(
            from_addr="ambiguous@example.com",
            subject="Hi from someone",
        ))
    assert v.decision is Decision.KEEP
    assert v.label == "personal"
    assert v.stage == "llm"


def test_llm_tiebreaker_returns_marketing_drops(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    with patch("brain.core.email_filter._llm_label", return_value="marketing"):
        v = classify_email(_msg(
            from_addr="ambiguous@example.com",
            subject="A new offer",
        ))
    assert v.decision is Decision.DROP


def test_llm_can_be_disabled():
    """Even with a key set, llm_tiebreaker=False skips that stage."""
    import os
    os.environ["ANTHROPIC_API_KEY"] = "test"
    try:
        with patch("brain.core.email_filter._llm_label") as mocked:
            v = classify_email(_msg(
                from_addr="ambiguous@example.com",
                subject="generic",
            ), llm_tiebreaker=False)
            mocked.assert_not_called()
        assert v.decision is Decision.DROP
        assert v.stage == "default"
    finally:
        del os.environ["ANTHROPIC_API_KEY"]


# ---- allowlist builder ---------------------------------------------------

def test_build_allowlist_from_store_pulls_emails_from_people():
    from brain.core.entities import Entity, EntityStore
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as d:
        store = EntityStore(str(Path(d) / "e.db"))
        store.upsert_entity(Entity(
            kind="person", name="Jeff Torres",
            attributes={"emails": ["jeff@acme.com", "Jeff.Personal@gmail.com"]},
            aliases=["jeff@old-email.com"],
        ))
        from brain.core.email_filter import build_allowlist_from_store
        allow = build_allowlist_from_store(store)
        assert "jeff@acme.com" in allow
        assert "jeff.personal@gmail.com" in allow
        assert "jeff@old-email.com" in allow
