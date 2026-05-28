"""LLM synthesis tests — patch the Anthropic HTTP call so no network is hit."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from brain.core.entities import Entity
from brain.core.synthesize import (
    SynthesizeError,
    classify_layer_llm,
    synthesize_dossier,
)


def _fake_response(text: str) -> dict:
    return {"content": [{"type": "text", "text": text}]}


def test_classify_layer_llm_returns_recognized_label(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    with patch("brain.core.synthesize._post_anthropic", return_value=_fake_response("decision")):
        assert classify_layer_llm("we chose X over Y") == "decision"


def test_classify_layer_llm_extracts_label_from_chatty_response(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    with patch(
        "brain.core.synthesize._post_anthropic",
        return_value=_fake_response("The right label here is workaround."),
    ):
        assert classify_layer_llm("a hack to bypass") == "workaround"


def test_classify_layer_llm_raises_on_unrecognized(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    with patch("brain.core.synthesize._post_anthropic", return_value=_fake_response("nonsense")):
        with pytest.raises(SynthesizeError):
            classify_layer_llm("text")


def test_classify_layer_llm_raises_without_api_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    with pytest.raises(SynthesizeError):
        classify_layer_llm("text")


def test_synthesize_dossier_returns_bullets(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    rendered = "VP at Acme\nMet at the Block Party\nFamily: Dana, Mia, Leo\n"
    with patch("brain.core.synthesize._post_anthropic", return_value=_fake_response(rendered)):
        person = Entity(kind="person", name="Jeff Torres")
        bullets = synthesize_dossier(person, None, [{"text": "some excerpt"}])
        assert bullets == ["VP at Acme", "Met at the Block Party", "Family: Dana, Mia, Leo"]


def test_synthesize_dossier_caps_bullets_at_five(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    rendered = "\n".join(f"bullet {i}" for i in range(10))
    with patch("brain.core.synthesize._post_anthropic", return_value=_fake_response(rendered)):
        person = Entity(kind="person", name="Jeff")
        bullets = synthesize_dossier(person, None, [{"text": "x"}])
        assert len(bullets) == 5


def test_synthesize_dossier_handles_empty_chunks(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    person = Entity(kind="person", name="Jeff")
    assert synthesize_dossier(person, None, []) == []
    assert synthesize_dossier(person, None, [{"text": ""}]) == []
