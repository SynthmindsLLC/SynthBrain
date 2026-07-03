"""B9 entity canonicalization tests — extracted names matched against the
graph at ingest, canonical ids appended to entity_tags alongside raw names."""

from __future__ import annotations

from brain.core.entities import Entity, EntityStore
from brain.core.pipeline import RawDoc, ingest
from brain.core.tag import tag_entities


class CapturingIndex:
    """Duck-typed stand-in for BrainIndex that keeps every chunk."""

    def __init__(self) -> None:
        self.chunks = []

    def add_chunks(self, chunks) -> int:
        self.chunks.extend(chunks)
        return len(chunks)


def _seeded_store(path: str) -> EntityStore:
    store = EntityStore(path)
    store.upsert_entity(Entity(kind="person", name="Jeff Torres", aliases=["Jeff"]))
    store.upsert_entity(Entity(kind="org", name="Acme Robotics"))
    return store


def test_seeded_store_appends_canonical_ids(tmp_path):
    store = _seeded_store(str(tmp_path / "e.db"))
    idx = CapturingIndex()
    ingest(idx, [RawDoc(
        text="We met with Jeff Torres over at Acme Robotics yesterday.",
        source="mem", source_id="n1",
    )], entity_store=store)
    tags = idx.chunks[0].entity_tags
    assert "Jeff Torres" in tags            # raw name kept
    assert "person:jeff-torres" in tags     # canonical id appended
    assert "org:acme-robotics" in tags


def test_alias_match_appends_canonical_id(tmp_path):
    store = _seeded_store(str(tmp_path / "e.db"))
    idx = CapturingIndex()
    ingest(idx, [RawDoc(text="Talked with Jeff today.", source="mem", source_id="n2")],
           entity_store=store)
    tags = idx.chunks[0].entity_tags
    assert "Jeff" in tags
    assert "person:jeff-torres" in tags


def test_canonical_ids_are_deduped(tmp_path):
    store = _seeded_store(str(tmp_path / "e.db"))
    idx = CapturingIndex()
    # "Jeff Torres" (name) and "Jeff" (alias) both resolve to the same entity.
    ingest(idx, [RawDoc(
        text="Jeff Torres said hello, and later Jeff waved.",
        source="mem", source_id="n3",
    )], entity_store=store)
    tags = idx.chunks[0].entity_tags
    assert tags.count("person:jeff-torres") == 1


def test_empty_store_leaves_tags_unchanged(tmp_path):
    store = EntityStore(str(tmp_path / "e.db"))
    text = "We met with Jeff Torres over at Acme Robotics yesterday."
    idx = CapturingIndex()
    ingest(idx, [RawDoc(text=text, source="mem", source_id="n4")], entity_store=store)
    assert idx.chunks[0].entity_tags == tag_entities(text)


def test_no_store_leaves_tags_unchanged():
    text = "We met with Jeff Torres over at Acme Robotics yesterday."
    idx = CapturingIndex()
    ingest(idx, [RawDoc(text=text, source="mem", source_id="n5")])
    assert idx.chunks[0].entity_tags == tag_entities(text)


def test_cli_ingest_wires_the_entity_store(tmp_path, capsys):
    from brain.cli import main
    from brain.core.embed import FakeEmbedder
    from brain.core.index import BrainIndex

    entdb = str(tmp_path / "e.db")
    _seeded_store(entdb)
    src = tmp_path / "vault"
    src.mkdir()
    (src / "note.md").write_text("Jeff Torres shipped the adapter.", encoding="utf-8")
    db = str(tmp_path / "lance")

    assert main(["--db", db, "--entdb", entdb, "ingest",
                 "--adapter", "filesystem", "--source", str(src)]) == 0
    capsys.readouterr()
    idx = BrainIndex(db, FakeEmbedder())
    rows = idx.query("Jeff Torres shipped the adapter", k=1)
    assert rows
    assert "person:jeff-torres" in list(rows[0]["entity_tags"])
