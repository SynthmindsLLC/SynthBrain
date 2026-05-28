"""Slack adapter tests — patch the _get method, never touch the network."""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from brain.adapters.slack_adapter import SlackAdapter, SlackAuthError
from brain.core.checkpoint import CheckpointStore


def _make_fake_get(*, channels, history_by_channel,
                   replies_by_thread=None, users=None):
    """Build a _get matcher keyed by Slack method name."""
    replies_by_thread = replies_by_thread or {}
    users = users or {}

    history_calls = {ch_id: 0 for ch_id in history_by_channel}

    def fake_get(self, method, params):  # noqa: ARG001
        if method == "conversations.list":
            return {"channels": channels}
        if method == "conversations.history":
            ch = params.get("channel")
            i = history_calls.get(ch, 0)
            history_calls[ch] = i + 1
            pages = history_by_channel.get(ch, [])
            page = pages[i] if i < len(pages) else {"messages": []}
            return page
        if method == "conversations.replies":
            ts = params.get("ts")
            return replies_by_thread.get(ts, {"messages": []})
        if method == "users.info":
            uid = params.get("user")
            return {"user": {"profile": {"real_name": users.get(uid, uid)}}}
        raise AssertionError(f"unexpected method {method}")

    return fake_get


@pytest.fixture(autouse=True)
def _env(monkeypatch):
    monkeypatch.setenv("SLACK_USER_TOKEN", "xoxp-test")


def test_raises_without_token(monkeypatch):
    monkeypatch.delenv("SLACK_USER_TOKEN")
    with pytest.raises(SlackAuthError):
        SlackAdapter()


def test_dm_with_jeff_becomes_speakered_chunk():
    channels = [{"id": "D1", "is_im": True, "user": "U_JEFF"}]
    history = {"D1": [{"messages": [
        {"ts": "1748400000.001", "user": "U_WES",
         "text": "free for lunch?"},
        {"ts": "1748400060.002", "user": "U_JEFF",
         "text": "yeah, where?"},
        {"ts": "1748400120.003", "user": "U_WES",
         "text": "the new ramen place"},
    ]}]}
    users = {"U_WES": "Wes Shields", "U_JEFF": "Jeff Torres"}
    fake = _make_fake_get(channels=channels, history_by_channel=history,
                          users=users)
    with patch.object(SlackAdapter, "_get", new=fake):
        docs = list(SlackAdapter(include_threads=False, words_per_group=200).fetch())
    assert len(docs) == 1
    doc = docs[0]
    assert doc.source == "slack"
    assert doc.source_id.startswith("channel:D1:")
    assert "DM with Jeff Torres" in doc.text
    assert "Wes Shields: free for lunch?" in doc.text
    assert "Jeff Torres: yeah, where?" in doc.text


def test_per_channel_watermark_persists_after_run():
    channels = [{"id": "C1", "name": "general", "is_im": False, "is_group": True}]
    history = {"C1": [{"messages": [
        {"ts": "1748400000.001", "user": "U1", "text": "hi"},
        {"ts": "1748400500.002", "user": "U1", "text": "anyone there"},
    ]}]}
    users = {"U1": "Wes Shields"}
    fake = _make_fake_get(channels=channels, history_by_channel=history, users=users)
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch.object(SlackAdapter, "_get", new=fake):
            list(SlackAdapter(checkpoint_db=cp_db,
                              include_threads=False,
                              words_per_group=200).fetch())
        saved = CheckpointStore(cp_db).get("slack", key="latest_ts::C1")
        assert saved == "1748400500.002"


def test_threads_are_expanded_when_enabled():
    channels = [{"id": "C2", "name": "design", "is_im": False, "is_group": True}]
    parent = {"ts": "1748400000.001", "user": "U_WES",
              "text": "should we go with header-aware chunking?",
              "reply_count": 2, "thread_ts": "1748400000.001"}
    history = {"C2": [{"messages": [parent]}]}
    replies = {
        "1748400000.001": {"messages": [
            parent,
            {"ts": "1748400050.002", "user": "U_JEFF",
             "text": "the research backs it"},
            {"ts": "1748400060.003", "user": "U_WES",
             "text": "decision: header-aware"},
        ]}
    }
    users = {"U_WES": "Wes", "U_JEFF": "Jeff"}
    fake = _make_fake_get(channels=channels, history_by_channel=history,
                          replies_by_thread=replies, users=users)
    with patch.object(SlackAdapter, "_get", new=fake):
        docs = list(SlackAdapter(include_threads=True, words_per_group=200).fetch())
    assert len(docs) == 1
    assert "research backs it" in docs[0].text
    assert "decision: header-aware" in docs[0].text


def test_watermark_skips_already_seen_messages():
    """Second run with the saved watermark should fetch nothing."""
    channels = [{"id": "C3", "name": "ops", "is_im": False, "is_group": True}]
    history = {"C3": [{"messages": [
        {"ts": "1748400000.001", "user": "U1", "text": "hello world"},
    ]}]}
    users = {"U1": "Wes"}
    fake = _make_fake_get(channels=channels, history_by_channel=history, users=users)
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch.object(SlackAdapter, "_get", new=fake):
            first = list(SlackAdapter(
                checkpoint_db=cp_db, include_threads=False,
                words_per_group=200,
            ).fetch())
        assert first
        # New fake with the watermark applied -> nothing new
        empty_history = {"C3": [{"messages": []}]}
        fake_empty = _make_fake_get(channels=channels,
                                    history_by_channel=empty_history, users=users)
        with patch.object(SlackAdapter, "_get", new=fake_empty):
            second = list(SlackAdapter(
                checkpoint_db=cp_db, include_threads=False,
                words_per_group=200,
            ).fetch())
        assert second == []
