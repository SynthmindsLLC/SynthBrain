"""ChatGPT + Claude export adapter tests — golden conversations.json fixtures."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from brain.adapters.chatgpt_adapter import ChatGPTAdapter
from brain.adapters.claude_adapter import ClaudeAdapter


CHATGPT_FIXTURE = [
    {
        "id": "conv_1",
        "title": "Brainstorm on SynthBrain",
        "create_time": 1748419200.0,
        "mapping": {
            "n1": {
                "message": {
                    "author": {"role": "system"},
                    "content": {"parts": ["You are helpful."]},
                    "create_time": 1748419200.0,
                }
            },
            "n2": {
                "message": {
                    "author": {"role": "user"},
                    "content": {"parts": ["What's the dossier flow?"]},
                    "create_time": 1748419300.0,
                }
            },
            "n3": {
                "message": {
                    "author": {"role": "assistant"},
                    "content": {"parts": ["Resolve, then graph-join, then synthesize."]},
                    "create_time": 1748419400.0,
                }
            },
        },
    }
]

CLAUDE_FIXTURE = [
    {
        "uuid": "abc-123",
        "name": "Plan the next sprint",
        "created_at": "2026-05-28T12:00:00Z",
        "chat_messages": [
            {"sender": "human", "text": "What should we do first?"},
            {"sender": "assistant", "text": "Build resolve() — it's the gate."},
            {"sender": "human", "text": ""},  # empty -> skipped
        ],
    },
    {
        "uuid": "no-msgs",
        "name": "Empty",
        "chat_messages": [],
    },
]


def test_chatgpt_export_renders_speakered_body_in_chronological_order():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "conversations.json"
        p.write_text(json.dumps(CHATGPT_FIXTURE), encoding="utf-8")
        docs = list(ChatGPTAdapter(str(p)).fetch())
        assert len(docs) == 1
        d0 = docs[0]
        assert d0.source == "chatgpt"
        assert d0.source_id == "conv_1"
        assert "Brainstorm on SynthBrain" in d0.text
        assert "user:" in d0.text and "assistant:" in d0.text
        assert "system:" not in d0.text  # system role suppressed
        # ordering by create_time
        assert d0.text.index("user:") < d0.text.index("assistant:")


def test_chatgpt_export_accepts_directory_source():
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "conversations.json").write_text(json.dumps(CHATGPT_FIXTURE), encoding="utf-8")
        docs = list(ChatGPTAdapter(d).fetch())
        assert len(docs) == 1


def test_claude_export_skips_empty_messages_and_empty_convos():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "conversations.json"
        p.write_text(json.dumps(CLAUDE_FIXTURE), encoding="utf-8")
        docs = list(ClaudeAdapter(str(p)).fetch())
        assert len(docs) == 1
        d0 = docs[0]
        assert d0.source == "claude"
        assert d0.source_id == "abc-123"
        assert "Build resolve()" in d0.text
        assert d0.meta["message_count"] == 2  # the empty one dropped


def test_claude_export_dir_source_resolves_to_conversations_json():
    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "conversations.json").write_text(json.dumps(CLAUDE_FIXTURE), encoding="utf-8")
        docs = list(ClaudeAdapter(d).fetch())
        assert len(docs) == 1
