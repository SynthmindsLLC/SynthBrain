"""Browser-history adapter, meta->entity emission, and split-identity
merge/suggest tooling."""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import pytest

from brain.adapters.browser_history_adapter import BrowserHistoryAdapter
from brain.core.checkpoint import CheckpointStore
from brain.core.embed import FakeEmbedder
from brain.core.entities import Edge, Entity, EntityStore
from brain.core.graphlab import suggest_merges
from brain.core.index import BrainIndex
from brain.core.pipeline import IngestStats, RawDoc, ingest

_WEBKIT = 11_644_473_600


def _wk(iso: str) -> int:
    dt = datetime.fromisoformat(iso)
    return int((dt.timestamp() + _WEBKIT) * 1_000_000)


def _make_history(path: Path, rows: list[tuple[str, str, str]]) -> None:
    con = sqlite3.connect(path)
    con.execute("CREATE TABLE urls (id INTEGER PRIMARY KEY, url TEXT, title TEXT)")
    con.execute("CREATE TABLE visits (id INTEGER PRIMARY KEY, url INTEGER, visit_time INTEGER)")
    for i, (url, title, ts) in enumerate(rows, start=1):
        con.execute("INSERT INTO urls VALUES (?,?,?)", (i, url, title))
        con.execute("INSERT INTO visits VALUES (?,?,?)", (i, i, _wk(ts)))
    con.commit()
    con.close()


def test_browser_history_daily_digests(tmp_path):
    profile = tmp_path / "Default"
    profile.mkdir()
    _make_history(profile / "History", [
        ("https://arxiv.org/abs/cond-mat/0011144", "Newman 2001",
         "2026-07-01T09:14:00+00:00"),
        ("https://networkx.org/", "NetworkX docs", "2026-07-01T09:20:00+00:00"),
        ("chrome://settings/", "Settings", "2026-07-01T09:21:00+00:00"),
        ("http://localhost:3000/dashboard", "Dash", "2026-07-01T09:22:00+00:00"),
        ("https://example.com/late", "Different day", "2026-07-02T08:00:00+00:00"),
    ])
    entdb = str(tmp_path / "e.db")
    a = BrowserHistoryAdapter(str(tmp_path), checkpoint_db=entdb)
    docs = list(a.fetch())
    assert [d.source_id for d in docs] == ["Default:2026-07-01", "Default:2026-07-02"]
    day1 = docs[0]
    assert "Newman 2001 — arxiv.org" in day1.text
    assert "chrome://" not in day1.text and "localhost" not in day1.text
    assert day1.meta["visits"] == 2
    # Deferred watermark; committed -> second run silent.
    assert CheckpointStore(entdb).get("browser-history", a.checkpoint_key) is None
    a.commit_checkpoint()
    b = BrowserHistoryAdapter(str(tmp_path), checkpoint_db=entdb)
    assert list(b.fetch()) == []


def test_browser_history_skips_today(tmp_path):
    profile = tmp_path / "Default"
    profile.mkdir()
    now = datetime.now(tz=timezone.utc).isoformat()
    _make_history(profile / "History", [
        ("https://example.com/now", "In progress", now),
    ])
    assert list(BrowserHistoryAdapter(str(tmp_path)).fetch()) == []


def test_browser_history_missing_source(tmp_path):
    with pytest.raises(FileNotFoundError):
        BrowserHistoryAdapter(str(tmp_path / "nope"))


# --- meta -> entity emission ---------------------------------------------------


class _Idx:
    def add_chunks(self, chunks):
        return len(chunks)


def test_meeting_meta_becomes_event_and_attendees(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    doc = RawDoc(
        text="# Standup\n\nnotes", source="granola", source_id="g1",
        meta={"title": "SynthOS Standup", "attendees": ["Wes Shields", "Joseph Rosenbaum"]},
    )
    ingest(_Idx(), [doc], entity_store=store)
    ev = store.get_entity("event:synthos-standup")
    assert ev is not None and ev.attributes["source"] == "granola"
    wes = store.get_entity("person:wes-shields")
    assert wes is not None
    rels = [(e.rel, e.dst) for e, _ in store.neighbors("person:wes-shields")]
    assert ("attended", "event:synthos-standup") in rels


def test_email_from_meta_becomes_person_with_alias(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    doc = RawDoc(
        text="body", source="agentmail", source_id="m1",
        meta={"subject": "hi", "from": "Nick Cosgrove <nick@upwork.com>"},
    )
    ingest(_Idx(), [doc], entity_store=store)
    p = store.get_entity("person:nick-cosgrove")
    assert p is not None
    assert "nick@upwork.com" in p.aliases
    assert p.attributes["emails"] == ["nick@upwork.com"]
    # No attendees + title -> no event node.
    assert not [e for e in store.all_entities(kind="event")]


def test_entity_emit_failure_is_isolated(tmp_path, monkeypatch):
    from brain.core import pipeline as pl

    store = EntityStore(str(tmp_path / "e.db"))
    monkeypatch.setattr(pl, "_emit_entities",
                        lambda doc, s: (_ for _ in ()).throw(RuntimeError("graph down")))
    stats = IngestStats()
    n = ingest(_Idx(), [RawDoc(text="hello", source="t", source_id="a",
                               meta={"from": "x@y.z"})],
               entity_store=store, stats=stats)
    assert n == 1                       # chunks still landed
    assert stats.errors == 1
    assert any("entity-emit" in s for s in stats.error_samples)


def test_dry_run_emits_no_entities(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    ingest(_Idx(), [RawDoc(text="x", source="g", source_id="1",
                            meta={"title": "M", "attendees": ["A B"]})],
           entity_store=store, dry_run=True)
    assert store.counts()["entities"] == 0


# --- merge + suggest -------------------------------------------------------------


def _seed_split(store: EntityStore) -> None:
    store.upsert_entity(Entity(kind="person", name="Wes Shields",
                                aliases=["Wes"], attributes={"org": "Synthminds"}))
    store.upsert_entity(Entity(kind="person", name="wes.shields@qwoted.com",
                                attributes={"emails": ["wes.shields@qwoted.com"]}))
    store.upsert_entity(Entity(kind="event", name="Sync"))
    store.add_edge(Edge(src="person:wes-shields", rel="attended", dst="event:sync"))
    store.add_edge(Edge(src="person:wes-shields-qwoted-com", rel="attended", dst="event:sync"))


def test_suggest_merges_finds_name_in_email(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    _seed_split(store)
    (s,) = suggest_merges(store)
    assert s["keep"] == "person:wes-shields"
    assert s["merge"] == "person:wes-shields-qwoted-com"
    assert s["confidence"] == "strong"


def test_merge_entities_unions_and_repoints(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    _seed_split(store)
    merged = store.merge_entities("person:wes-shields-qwoted-com", "person:wes-shields")
    assert merged.name == "Wes Shields"
    assert "wes.shields@qwoted.com" in merged.aliases
    assert merged.attributes["emails"] == ["wes.shields@qwoted.com"]
    assert store.get_entity("person:wes-shields-qwoted-com") is None
    # Duplicate attended edges collapsed to one.
    edges = [e for e, _ in store.neighbors("person:wes-shields", rel="attended")]
    assert len(edges) == 1
    # Alias lookup now resolves the email to the canonical person.
    assert [e.id for e in store.find_by_name("wes.shields@qwoted.com")] == ["person:wes-shields"]


def test_merge_entities_guards(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    _seed_split(store)
    with pytest.raises(ValueError):
        store.merge_entities("person:wes-shields", "person:wes-shields")
    with pytest.raises(KeyError):
        store.merge_entities("person:nobody", "person:wes-shields")
