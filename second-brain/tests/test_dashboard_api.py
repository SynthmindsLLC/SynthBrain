"""Dashboard API tests — /stats/breakdown, /ingest/runs, /chunks/recent, and
the degree-sampled /graph. Fresh per-test brain, fake embedder, offline."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient

from brain.core.embed import FakeEmbedder
from brain.core.entities import Edge, Entity, EntityStore
from brain.core.index import BrainIndex
from brain.core.ledger import IngestLedger
from brain.core.pipeline import RawDoc, ingest


def _dt(day: int) -> datetime:
    return datetime(2026, 7, day, 12, 0, 0, tzinfo=timezone.utc)


@pytest.fixture()
def dash(monkeypatch, tmp_path):
    """Brain seeded for breakdown math: 3 chunks across sources/layers/days
    (one multi-project-tag), a small graph, and 3 ledger runs."""
    db = str(tmp_path / "lance")
    entdb = str(tmp_path / "e.db")
    monkeypatch.setenv("BRAIN_DB", db)
    monkeypatch.setenv("BRAIN_ENTDB", entdb)
    monkeypatch.setenv("BRAIN_EMBEDDER", "fake")
    monkeypatch.delenv("BRAIN_BEARER_TOKEN", raising=False)

    index = BrainIndex(db, FakeEmbedder())
    ingest(index, [
        # Multi-tag: mentions both pbtv and synthbrain keywords.
        RawDoc(text="Alpha note about pbtv and synthbrain plumbing.",
               source="mem", source_id="m1", created_at=_dt(1)),
        RawDoc(text="plain artifact note", source="filesystem",
               source_id="f1", created_at=_dt(1)),
        RawDoc(text="We decided to use LanceDB for the index.",
               source="claude-code", source_id="s1", created_at=_dt(2)),
    ])

    store = EntityStore(entdb)
    store.upsert_entity(Entity(kind="person", name="Jeff Torres"))
    store.upsert_entity(Entity(kind="person", name="Ana Ruiz"))
    store.upsert_entity(Entity(kind="event", name="Fall Block Party"))
    store.upsert_entity(Entity(kind="org", name="Acme Robotics"))
    store.add_edge(Edge(src="person:jeff-torres", rel="attended",
                        dst="event:fall-block-party"))
    store.add_edge(Edge(src="person:ana-ruiz", rel="attended",
                        dst="event:fall-block-party"))
    store.add_edge(Edge(src="person:jeff-torres", rel="works_at",
                        dst="org:acme-robotics"))

    ledger = IngestLedger(entdb)
    run_ids = []
    for i, adapter in enumerate(("mem", "filesystem", "claude-code")):
        rid = ledger.start(adapter, f"/src/{i}")
        ledger.finish(rid, "completed", docs=1, chunks=i + 1)
        run_ids.append(rid)

    import importlib
    from brain import api as brain_api
    importlib.reload(brain_api)
    client = TestClient(brain_api.app)
    return {"client": client, "index": index, "run_ids": run_ids}


# --- D1: /stats/breakdown -------------------------------------------------------

def test_breakdown_math_against_seeded_index(dash):
    r = dash["client"].get("/stats/breakdown")
    assert r.status_code == 200
    body = r.json()
    assert body["chunks_total"] == 3
    assert body["by_source"] == {"mem": 1, "filesystem": 1, "claude-code": 1}
    assert body["by_layer"] == {"artifact": 2, "decision": 1}
    # The multi-tag chunk counts once per project tag.
    assert body["by_project"] == {"pbtv": 1, "synthbrain": 1}
    assert body["by_day"] == [
        {"date": "2026-07-01", "chunks": 2},
        {"date": "2026-07-02", "chunks": 1},
    ]
    assert body["entities"] == {
        "total": 4, "by_kind": {"person": 2, "event": 1, "org": 1},
    }
    assert body["edges"] == {"total": 3, "by_rel": {"attended": 2, "works_at": 1}}
    assert body["generated_at"]


def test_breakdown_is_cached_within_ttl(dash):
    client = dash["client"]
    assert client.get("/stats/breakdown").json()["chunks_total"] == 3
    # Write behind the API's back: the 30s cache should serve the stale count.
    ingest(dash["index"], [RawDoc(text="sneaky", source="mem", source_id="m9")])
    assert client.get("/stats/breakdown").json()["chunks_total"] == 3


def test_ingest_text_busts_breakdown_cache(dash):
    client = dash["client"]
    assert client.get("/stats/breakdown").json()["chunks_total"] == 3
    r = client.post("/ingest-text", json={
        "text": "fresh chunk", "source": "api", "source_id": "adhoc-1",
    })
    assert r.status_code == 200
    assert client.get("/stats/breakdown").json()["chunks_total"] == 4


# --- D2: /ingest/runs -----------------------------------------------------------

def test_ingest_runs_newest_first_with_full_row_shape(dash):
    r = dash["client"].get("/ingest/runs")
    assert r.status_code == 200
    runs = r.json()["runs"]
    assert [x["run_id"] for x in runs] == list(reversed(dash["run_ids"]))
    top = runs[0]
    assert top["adapter"] == "claude-code"
    assert top["status"] == "completed"
    assert top["chunks"] == 3
    for key in ("run_id", "adapter", "source", "started_at", "finished_at",
                "status", "docs", "chunks", "errors", "skipped",
                "llm_classified", "heuristic_classified"):
        assert key in top
    assert isinstance(top["error_samples"], list)
    assert isinstance(top["meta"], dict)


def test_ingest_runs_limit_enforced(dash):
    client = dash["client"]
    assert len(client.get("/ingest/runs", params={"limit": 1}).json()["runs"]) == 1
    assert client.get("/ingest/runs", params={"limit": 0}).status_code == 422
    assert client.get("/ingest/runs", params={"limit": 501}).status_code == 422


# --- D3: /chunks/recent ---------------------------------------------------------

def test_recent_chunks_sorted_desc_with_shape(dash):
    r = dash["client"].get("/chunks/recent")
    assert r.status_code == 200
    chunks = r.json()["chunks"]
    assert len(chunks) == 3
    assert chunks[0]["source_id"] == "s1"  # 2026-07-02, newest
    dates = [c["created_at"] for c in chunks]
    assert dates == sorted(dates, reverse=True)
    for key in ("id", "text", "source", "source_id", "url", "layer",
                "project_tags", "entity_tags", "created_at"):
        assert key in chunks[0]
    assert isinstance(chunks[0]["project_tags"], list)
    assert isinstance(chunks[0]["entity_tags"], list)


def test_recent_chunks_truncates_long_text(dash):
    long_text = "y" * 900
    ingest(dash["index"], [RawDoc(text=long_text, source="mem", source_id="long1")])
    r = dash["client"].get("/chunks/recent", params={"source": "mem", "limit": 100})
    texts = [c["text"] for c in r.json()["chunks"]]
    truncated = [t for t in texts if t.endswith("…")]
    assert truncated
    assert len(truncated[0]) == 401


def test_recent_chunks_filters_by_source_and_layer(dash):
    client = dash["client"]
    by_source = client.get("/chunks/recent", params={"source": "mem"}).json()["chunks"]
    assert [c["source"] for c in by_source] == ["mem"]
    by_layer = client.get("/chunks/recent", params={"layer": "decision"}).json()["chunks"]
    assert [c["layer"] for c in by_layer] == ["decision"]
    # A source value that would break a filter string is just a no-match here.
    weird = client.get("/chunks/recent", params={"source": "x') OR ('1'='1"})
    assert weird.status_code == 200
    assert weird.json()["chunks"] == []


def test_recent_chunks_validation(dash):
    client = dash["client"]
    assert client.get("/chunks/recent", params={"layer": "bogus"}).status_code == 422
    assert client.get("/chunks/recent", params={"limit": 0}).status_code == 422
    assert client.get("/chunks/recent", params={"limit": 101}).status_code == 422


# --- D6: /graph degree sampling + filters ---------------------------------------

def test_graph_nodes_carry_degree(dash):
    r = dash["client"].get("/graph")
    assert r.status_code == 200
    nodes = {n["id"]: n for n in r.json()["nodes"]}
    assert nodes["person:jeff-torres"]["degree"] == 2
    assert nodes["event:fall-block-party"]["degree"] == 2
    assert nodes["person:ana-ruiz"]["degree"] == 1
    assert nodes["org:acme-robotics"]["degree"] == 1
    assert len(r.json()["links"]) == 3


def test_graph_limit_samples_top_degree_with_stable_tiebreak(dash):
    r = dash["client"].get("/graph", params={"limit": 2})
    body = r.json()
    # Both degree-2 hubs win over the degree-1 nodes; ties break by id asc.
    assert [n["id"] for n in body["nodes"]] == [
        "event:fall-block-party", "person:jeff-torres",
    ]
    # Links only between included nodes.
    assert body["links"] == [{
        "source": "person:jeff-torres", "target": "event:fall-block-party",
        "rel": "attended",
    }]


def test_graph_kind_filter_csv(dash):
    client = dash["client"]
    people = client.get("/graph", params={"kind": "person"}).json()
    assert {n["kind"] for n in people["nodes"]} == {"person"}
    assert people["links"] == []  # no person->person edges
    both = client.get("/graph", params={"kind": "person,event"}).json()
    assert {n["kind"] for n in both["nodes"]} == {"person", "event"}
    assert any(l["rel"] == "attended" for l in both["links"])
    # Degree still reflects the full edge set even when kinds are filtered.
    jeff = next(n for n in people["nodes"] if n["id"] == "person:jeff-torres")
    assert jeff["degree"] == 2


def test_graph_min_degree_filter(dash):
    r = dash["client"].get("/graph", params={"min_degree": 2})
    body = r.json()
    assert {n["id"] for n in body["nodes"]} == {
        "person:jeff-torres", "event:fall-block-party",
    }
    assert len(body["links"]) == 1


def test_graph_param_validation(dash):
    client = dash["client"]
    assert client.get("/graph", params={"kind": "person,alien"}).status_code == 422
    assert client.get("/graph", params={"limit": 0}).status_code == 422
    assert client.get("/graph", params={"limit": 2001}).status_code == 422
    assert client.get("/graph", params={"min_degree": -1}).status_code == 422


# --- auth: new endpoints honor the bearer token ----------------------------------

def test_new_endpoints_require_bearer_when_set(monkeypatch, tmp_path):
    db = str(tmp_path / "lance")
    entdb = str(tmp_path / "e.db")
    monkeypatch.setenv("BRAIN_DB", db)
    monkeypatch.setenv("BRAIN_ENTDB", entdb)
    monkeypatch.setenv("BRAIN_EMBEDDER", "fake")
    monkeypatch.setenv("BRAIN_BEARER_TOKEN", "s3cret")
    BrainIndex(db, FakeEmbedder())
    EntityStore(entdb)

    import importlib
    from brain import api as brain_api
    importlib.reload(brain_api)
    client = TestClient(brain_api.app)

    ok = {"Authorization": "Bearer s3cret"}
    for path in ("/stats/breakdown", "/ingest/runs", "/chunks/recent", "/graph"):
        assert client.get(path).status_code == 401, path
        assert client.get(path, headers=ok).status_code == 200, path
