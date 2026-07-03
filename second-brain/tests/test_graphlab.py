"""Network-science layer: derived edges, metrics, ego networks, endpoints —
plus the bookmarks adapter that feeds URL nodes into the corpus."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import pytest

from brain.adapters.bookmarks_adapter import BookmarksAdapter
from brain.core.checkpoint import CheckpointStore
from brain.core.embed import FakeEmbedder
from brain.core.entities import Edge, Entity, EntityStore
from brain.core.graphlab import (
    build_nx_graph,
    compute_metrics,
    derive_co_attendance,
    derive_co_mentions,
    ego_subgraph,
    load_metrics,
    persist_metrics,
    run_all,
)
from brain.core.index import BrainIndex
from brain.core.pipeline import RawDoc, ingest


def _seed_events(store: EntityStore) -> None:
    """3 people; small meeting (a,b) + big meeting (a,b,c) — Newman weights
    should favor the intimate tie."""
    for name in ("Ada", "Bob", "Cyd"):
        store.upsert_entity(Entity(kind="person", name=name))
    store.upsert_entity(Entity(kind="event", name="Small Sync"))
    store.upsert_entity(Entity(kind="event", name="Big Standup"))
    for p in ("ada", "bob"):
        store.add_edge(Edge(src=f"person:{p}", rel="attended", dst="event:small-sync"))
    for p in ("ada", "bob", "cyd"):
        store.add_edge(Edge(src=f"person:{p}", rel="attended", dst="event:big-standup"))


def test_co_attendance_newman_weights(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    _seed_events(store)
    written = derive_co_attendance(store)
    assert written == 3  # ada-bob, ada-cyd, bob-cyd
    g = build_nx_graph(store, rels=("co_attended",))
    # ada-bob: 1/(2-1) from Small Sync + 1/(3-1) from Big Standup = 1.5
    assert g["person:ada"]["person:bob"]["weight"] == pytest.approx(1.5)
    # ada-cyd: only the big meeting = 0.5 — intimate ties weigh more.
    assert g["person:ada"]["person:cyd"]["weight"] == pytest.approx(0.5)
    # Deterministic direction + upsert: re-derivation doesn't duplicate.
    assert derive_co_attendance(store) == 3
    assert g.number_of_edges() == 3


def test_co_mentions_pmi(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    index = BrainIndex(str(tmp_path / "lance"), FakeEmbedder())
    # 4 docs: jeff+acme together twice (always together), zoe alone twice.
    docs = []
    for i, tags_text in enumerate(
        ["Jeff Torres of Acme Robotics", "Jeff Torres visited Acme Robotics",
         "Zoe was here", "Zoe again"]
    ):
        docs.append(RawDoc(text=tags_text, source="t", source_id=f"d{i}"))
    ingest(index, docs)
    # Manually stamp canonical ids into the index via a second ingest pass
    # with a seeded store (canonicalization path).
    for name, kind in (("Jeff Torres", "person"), ("Acme Robotics", "org"),
                        ("Zoe", "person")):
        store.upsert_entity(Entity(kind=kind, name=name))
    ingest(index, [RawDoc(text=t, source="t", source_id=f"d{i}") for i, t in enumerate(
        ["Jeff Torres of Acme Robotics", "Jeff Torres visited Acme Robotics",
         "Zoe was here", "Zoe again"])], entity_store=store)

    written = derive_co_mentions(index, store, min_count=2)
    assert written == 1  # only jeff<->acme clears min_count with PMI>0
    g = build_nx_graph(store, rels=("co_mentioned",))
    w = g["person:jeff-torres"]["org:acme-robotics"]["weight"]
    assert w > 0  # they co-occur strictly more than chance
    edge_attrs = json.loads(
        store._db.execute(  # noqa: SLF001
            "SELECT attributes FROM edges WHERE rel='co_mentioned'"
        ).fetchone()["attributes"]
    )
    assert edge_attrs["count"] == 2 and edge_attrs["derived"] is True


def test_metrics_shapes_and_bridge_betweenness(tmp_path):
    """Barbell-ish graph: two triangles joined through a bridge node — the
    bridge must dominate betweenness; triangle members must have clustering 1."""
    store = EntityStore(str(tmp_path / "e.db"))
    for n in "abcdefg":
        store.upsert_entity(Entity(kind="person", name=n))
    tri1 = [("a", "b"), ("b", "c"), ("a", "c")]
    tri2 = [("e", "f"), ("f", "g"), ("e", "g")]
    bridge = [("c", "d"), ("d", "e")]
    for x, y in tri1 + tri2 + bridge:
        store.add_edge(Edge(src=f"person:{x}", rel="discussed_with", dst=f"person:{y}"))

    g = build_nx_graph(store)
    m = compute_metrics(g)
    assert set(m["person:a"].keys()) == {
        "degree", "eigenvector", "pagerank", "betweenness",
        "closeness", "clustering", "core", "community",
    }
    top_betweenness = max(m, key=lambda n: m[n]["betweenness"])
    assert top_betweenness == "person:d"           # the broker
    assert m["person:a"]["clustering"] == pytest.approx(1.0)  # closed triangle
    assert m["person:d"]["clustering"] == pytest.approx(0.0)
    assert m["person:a"]["core"] == 2               # triangle = 2-core
    # Louvain (seeded) separates the two triangles into distinct communities.
    assert m["person:a"]["community"] != m["person:f"]["community"]

    persist_metrics(store, m)
    loaded = load_metrics(store)
    assert loaded["person:d"]["betweenness"] == pytest.approx(
        m["person:d"]["betweenness"])
    assert "computed_at" in loaded["person:d"]


def test_metrics_empty_graph(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    assert compute_metrics(build_nx_graph(store)) == {}


def test_ego_subgraph_hops(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    _seed_events(store)
    derive_co_attendance(store)
    nodes1, edges1 = ego_subgraph(store, "person:ada", hops=1)
    assert "person:ada" in nodes1 and "person:bob" in nodes1
    nodes2, _ = ego_subgraph(store, "event:small-sync", hops=2)
    assert "person:cyd" in nodes2  # 2 hops: event -> ada/bob -> co_attended cyd
    assert ego_subgraph(store, "person:nobody") == ([], [])
    # rel filter: only 'attended' edges — co_attended neighbors excluded.
    nodes_att, _ = ego_subgraph(store, "person:ada", hops=1, rels=("attended",))
    assert all(not n.startswith("person:") or n == "person:ada" for n in nodes_att)


def test_run_all_summary(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    _seed_events(store)
    summary = run_all(store, None)
    assert summary["derived"]["co_attended"] == 3
    assert summary["nodes"] == 5
    assert summary["communities"] >= 1
    assert summary["top_eigenvector"]


def test_api_graph_metrics_and_ego(tmp_path, monkeypatch):
    import importlib

    from fastapi.testclient import TestClient

    monkeypatch.setenv("BRAIN_DB", str(tmp_path / "lance"))
    monkeypatch.setenv("BRAIN_ENTDB", str(tmp_path / "e.db"))
    monkeypatch.setenv("BRAIN_EMBEDDER", "fake")
    monkeypatch.delenv("BRAIN_BEARER_TOKEN", raising=False)
    store = EntityStore(str(tmp_path / "e.db"))
    BrainIndex(str(tmp_path / "lance"), FakeEmbedder())
    _seed_events(store)

    import brain.api as api
    importlib.reload(api)
    client = TestClient(api.app)

    # Before any run: metrics 404, /graph nodes carry None features.
    assert client.get("/graph/metrics").status_code == 404
    node = client.get("/graph").json()["nodes"][0]
    assert node["eigenvector"] is None and node["community"] is None

    run_all(store, None)
    m = client.get("/graph/metrics").json()
    assert m["nodes"] == 5 and m["top"]["eigenvector"]
    assert m["communities"][0]["size"] >= 1

    node = client.get("/graph").json()["nodes"][0]
    assert node["eigenvector"] is not None

    ego = client.get("/graph/ego/person:ada?hops=1").json()
    assert ego["center"] == "person:ada"
    assert any(n["id"] == "person:bob" for n in ego["nodes"])
    assert client.get("/graph/ego/person:nobody").status_code == 404
    assert client.get("/graph/ego/person:ada?rel=bogus").status_code == 422


# --- bookmarks adapter --------------------------------------------------------

CHROME_JSON = {
    "roots": {
        "bookmark_bar": {
            "type": "folder", "name": "Bookmarks Bar",
            "children": [
                {"type": "url", "name": "Newman 2001 paper",
                 "url": "https://arxiv.org/abs/cond-mat/0011144",
                 "guid": "g1", "date_added": "13320000000000000"},
                {"type": "folder", "name": "AI",
                 "children": [
                     {"type": "url", "name": "networkx docs",
                      "url": "https://networkx.org/", "guid": "g2",
                      "date_added": "13330000000000000"},
                     {"type": "url", "name": "local file", "url": "file:///etc/hosts",
                      "guid": "g3", "date_added": "13330000000000001"},
                 ]},
            ],
        },
        "other": {"type": "folder", "name": "Other", "children": []},
    }
}

NETSCAPE_HTML = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<DL><p>
  <DT><H3 ADD_DATE="1700000000">Reading</H3>
  <DL><p>
    <DT><A HREF="https://example.com/a" ADD_DATE="1700000100">Article A</A>
    <DT><H3>Deep</H3>
    <DL><p>
      <DT><A HREF="https://example.com/b" ADD_DATE="1700000200">Article B</A>
    </DL><p>
  </DL><p>
  <DT><A HREF="javascript:void(0)" ADD_DATE="1700000300">bookmarklet</A>
</DL><p>
"""


def test_bookmarks_chrome_json(tmp_path):
    src = tmp_path / "Bookmarks"
    src.write_text(json.dumps(CHROME_JSON), encoding="utf-8")
    cp_db = str(tmp_path / "e.db")
    a = BookmarksAdapter(str(src), checkpoint_db=cp_db)
    docs = list(a.fetch())
    # file:// scheme excluded; 2 http(s) bookmarks remain.
    assert len(docs) == 2
    by_id = {d.source_id: d for d in docs}
    nx_doc = by_id["g2"]
    assert nx_doc.url == "https://networkx.org/"
    assert "**Folder:** Bookmarks Bar/AI" in nx_doc.text
    assert nx_doc.created_at.tzinfo is not None
    assert nx_doc.created_at.year >= 2023  # WebKit epoch converted sanely
    # Watermark deferred until commit; then a second run yields nothing.
    assert CheckpointStore(cp_db).get("bookmarks", a.checkpoint_key) is None
    a.commit_checkpoint()
    assert list(BookmarksAdapter(str(src), checkpoint_db=cp_db).fetch()) == []


def test_bookmarks_netscape_html(tmp_path):
    src = tmp_path / "export.html"
    src.write_text(NETSCAPE_HTML, encoding="utf-8")
    docs = list(BookmarksAdapter(str(src)).fetch())
    assert len(docs) == 2  # javascript: link excluded
    b = next(d for d in docs if d.url.endswith("/b"))
    assert "**Folder:** Reading/Deep" in b.text
    assert b.created_at == datetime.fromtimestamp(1700000200, tz=timezone.utc)


def test_bookmarks_missing_source(tmp_path):
    with pytest.raises(FileNotFoundError):
        BookmarksAdapter(str(tmp_path / "nope"))
