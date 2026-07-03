"""HTTP API tests — FastAPI TestClient against a fresh per-test brain."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from brain.adapters.calendar_adapter import CalendarAdapter
from brain.adapters.contacts_adapter import ContactsAdapter
from brain.adapters.entity_base import ingest_entities
from brain.core.embed import FakeEmbedder
from brain.core.entities import EntityStore
from brain.core.index import BrainIndex
from brain.core.pipeline import RawDoc, ingest


VCF = """BEGIN:VCARD
VERSION:3.0
FN:Jeff Torres
N:Torres;Jeff;;;
ORG:Acme Robotics
TITLE:VP
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:Jeff Brennan
N:Brennan;Jeff;;;
ORG:Mystic Seaport Museum
TITLE:Curator
END:VCARD
"""

ICS = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//t//EN
BEGIN:VEVENT
UID:e1@t
SUMMARY:Fall Block Party
DTSTART:20251004T180000Z
LOCATION:Groton, CT
ATTENDEE;CN=Jeff Torres:mailto:jeff.torres@acme.com
END:VEVENT
END:VCALENDAR
"""


@pytest.fixture()
def brain(monkeypatch, tmp_path):
    """Boot a fresh isolated brain for each test."""
    db = str(tmp_path / "lance")
    entdb = str(tmp_path / "e.db")
    monkeypatch.setenv("BRAIN_DB", db)
    monkeypatch.setenv("BRAIN_ENTDB", entdb)
    monkeypatch.setenv("BRAIN_EMBEDDER", "fake")
    monkeypatch.delenv("BRAIN_BEARER_TOKEN", raising=False)

    # Seed graph + index BEFORE importing the app (uses env on first access).
    (tmp_path / "c.vcf").write_text(VCF, encoding="utf-8")
    (tmp_path / "c.ics").write_text(ICS, encoding="utf-8")
    store = EntityStore(entdb)
    ingest_entities(store, ContactsAdapter(str(tmp_path / "c.vcf")))
    ingest_entities(store, CalendarAdapter(str(tmp_path / "c.ics")))
    index = BrainIndex(db, FakeEmbedder())
    ingest(index, [RawDoc(
        text="Jeff Torres mentioned the maritime conservation roadmap at the Fall Block Party.",
        source="mem",
        source_id="n1",
    )])

    # Reload the API module so module-level DEFAULT_* picks up env.
    import importlib
    from brain import api as brain_api
    importlib.reload(brain_api)
    return TestClient(brain_api.app)


def test_healthz_is_open(brain):
    r = brain.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"ok": True}


def test_stats_returns_counts(brain):
    r = brain.get("/stats")
    assert r.status_code == 200
    body = r.json()
    assert body["chunks"] >= 1
    assert body["graph"]["entities"] >= 2


def test_resolve_unique_returns_entity(brain):
    r = brain.post("/resolve", json={"mention": "Jeff Torres"})
    body = r.json()
    assert body["status"] == "resolved"
    assert body["entity"]["name"] == "Jeff Torres"


def test_resolve_ambiguous_returns_candidates(brain):
    r = brain.post("/resolve", json={"mention": "Jeff", "context": ""})
    body = r.json()
    assert body["status"] == "ambiguous"
    assert {c["name"] for c in body["candidates"]} == {"Jeff Torres", "Jeff Brennan"}


def test_dossier_endpoint_returns_card_shape(brain):
    r = brain.post("/dossier", json={
        "mention": "Jeff",
        "event": "Fall Block Party",
        "context": "the party last fall",
        "use_chunks": True,
    })
    body = r.json()
    assert body["name"] == "Jeff Torres"
    assert "Fall Block Party" in body["where_met"]
    assert isinstance(body["discussed"], list)


def test_who_endpoint_returns_events_and_co_attendees(brain):
    r = brain.get("/who/Jeff%20Torres")
    body = r.json()
    assert body["matches"][0]["name"] == "Jeff Torres"
    events = body["matches"][0]["events"]
    assert any(ev["name"] == "Fall Block Party" for ev in events)


def test_query_returns_scored_chunks(brain):
    r = brain.post("/query", json={"text": "maritime conservation", "k": 3})
    body = r.json()
    assert body["results"]
    assert "score" in body["results"][0]


def test_query_rejects_invalid_layer(brain):
    r = brain.post("/query", json={"text": "x", "layer": "bogus"})
    assert r.status_code == 422


def test_query_accepts_valid_layer(brain):
    r = brain.post("/query", json={"text": "maritime", "layer": "artifact"})
    assert r.status_code == 200


def test_query_rejects_quotes_in_project(brain):
    for bad in ("pb'tv", 'pb"tv', "') OR ('1'='1"):
        r = brain.post("/query", json={"text": "x", "project": bad})
        assert r.status_code == 422, bad


def test_query_accepts_clean_project(brain):
    r = brain.post("/query", json={"text": "maritime", "project": "pbtv"})
    assert r.status_code == 200


def test_graph_endpoint_emits_nodes_and_links(brain):
    r = brain.get("/graph")
    body = r.json()
    assert any(n["kind"] == "person" for n in body["nodes"])
    assert any(n["kind"] == "event" for n in body["nodes"])
    assert any(l["rel"] == "attended" for l in body["links"])


def test_bearer_token_blocks_unauthenticated(monkeypatch, tmp_path):
    """When BRAIN_BEARER_TOKEN is set, /stats requires Bearer auth."""
    db = str(tmp_path / "lance")
    entdb = str(tmp_path / "e.db")
    monkeypatch.setenv("BRAIN_DB", db)
    monkeypatch.setenv("BRAIN_ENTDB", entdb)
    monkeypatch.setenv("BRAIN_EMBEDDER", "fake")
    monkeypatch.setenv("BRAIN_BEARER_TOKEN", "s3cret")

    EntityStore(entdb)
    BrainIndex(db, FakeEmbedder())

    import importlib
    from brain import api as brain_api
    importlib.reload(brain_api)
    client = TestClient(brain_api.app)

    assert client.get("/healthz").status_code == 200      # open
    assert client.get("/stats").status_code == 401         # blocked
    assert client.get("/stats", headers={"Authorization": "Bearer wrong"}).status_code == 403
    assert client.get("/stats", headers={"Authorization": "Bearer s3cret"}).status_code == 200
