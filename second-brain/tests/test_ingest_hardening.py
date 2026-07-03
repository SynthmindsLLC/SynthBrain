"""PY1 hardening tests — batched ingest, dry-run, ledger, error isolation,
filesystem skip report / exclusions / per-dir checkpoints, API validation."""

from __future__ import annotations

from pathlib import Path

import pytest

from brain.adapters.filesystem_adapter import ExtractorMissing, FilesystemAdapter
from brain.core.checkpoint import CheckpointStore
from brain.core.embed import FakeEmbedder
from brain.core.index import BrainIndex
from brain.core.ledger import IngestLedger
from brain.core.pipeline import FLUSH_EVERY, IngestStats, RawDoc, ingest


class RecordingIndex:
    """Duck-typed stand-in for BrainIndex that records flush sizes."""

    def __init__(self) -> None:
        self.batches: list[int] = []

    def add_chunks(self, chunks) -> int:
        self.batches.append(len(chunks))
        return len(chunks)


class RecordingEmbedder(FakeEmbedder):
    """FakeEmbedder that records how many texts each embed() call got."""

    def __init__(self) -> None:
        super().__init__()
        self.batch_sizes: list[int] = []

    def embed(self, texts):
        self.batch_sizes.append(len(texts))
        return super().embed(texts)


class SpyTable:
    """Proxy around a LanceDB table that records delete filters."""

    def __init__(self, table) -> None:
        self._table = table
        self.delete_filters: list[str] = []

    def delete(self, where: str):
        self.delete_filters.append(where)
        return self._table.delete(where)

    def __getattr__(self, name):
        return getattr(self._table, name)


def _docs(n: int, source: str = "mem") -> list[RawDoc]:
    return [RawDoc(text=f"note number {i}", source=source, source_id=f"d{i}")
            for i in range(n)]


# --- B1: batched flush + embed/delete batching --------------------------------

def test_ingest_flushes_every_256_chunks():
    idx = RecordingIndex()
    total = ingest(idx, _docs(600))
    assert total == 600
    assert idx.batches == [FLUSH_EVERY, FLUSH_EVERY, 600 - 2 * FLUSH_EVERY]


def test_ingest_small_run_single_flush():
    idx = RecordingIndex()
    assert ingest(idx, _docs(3)) == 3
    assert idx.batches == [3]


def test_add_chunks_batches_embeds_and_deletes(tmp_path):
    emb = RecordingEmbedder()
    idx = BrainIndex(str(tmp_path / "lance"), emb)
    spy = SpyTable(idx._table)
    idx._table = spy

    n = ingest(idx, _docs(600))
    assert n == 600
    assert idx.count() == 600
    # Embeds arrive in <=128-text batches.
    assert all(s <= 128 for s in emb.batch_sizes)
    assert sum(emb.batch_sizes) == 600
    # Each delete filter names <=500 ids (flushes are 256 so all fit in one).
    assert spy.delete_filters
    assert all(f.count("',") < 500 for f in spy.delete_filters)

    # A single oversized add_chunks call splits its delete into 500-id groups.
    spy.delete_filters.clear()
    from brain.core.schema import MemoryChunk
    chunks = [MemoryChunk(text=f"t{i}", source="mem", source_id=f"big{i}")
              for i in range(600)]
    idx.add_chunks(chunks)
    assert len(spy.delete_filters) == 2
    assert spy.delete_filters[0].count("'") == 500 * 2
    assert spy.delete_filters[1].count("'") == 100 * 2


def test_reingest_is_still_idempotent(tmp_path):
    idx = BrainIndex(str(tmp_path / "lance"), FakeEmbedder())
    ingest(idx, _docs(300))
    ingest(idx, _docs(300))
    assert idx.count() == 300


# --- B2: dry-run writes nothing ------------------------------------------------

def test_dry_run_writes_nothing_but_counts_everything(tmp_path):
    idx = BrainIndex(str(tmp_path / "lance"), FakeEmbedder())
    stats = IngestStats()
    total = ingest(idx, _docs(10), dry_run=True, stats=stats)
    assert total == 10
    assert idx.count() == 0
    assert stats.docs == 10
    assert stats.chunks == 10
    assert stats.by_source == {"mem": 10}
    assert sum(stats.by_layer.values()) == 10


# --- B12: per-doc error isolation ----------------------------------------------

def test_bad_doc_is_isolated_not_fatal():
    idx = RecordingIndex()
    docs = [
        RawDoc(text="good one", source="mem", source_id="g1"),
        RawDoc(text=None, source="mem", source_id="bad"),  # type: ignore[arg-type]
        RawDoc(text="good two", source="mem", source_id="g2"),
    ]
    stats = IngestStats()
    total = ingest(idx, docs, stats=stats)
    assert total == 2
    assert stats.docs == 2
    assert stats.errors == 1
    assert len(stats.error_samples) == 1
    assert "mem:bad" in stats.error_samples[0]


def test_error_samples_capped_at_ten():
    stats = IngestStats()
    docs = [RawDoc(text=None, source="mem", source_id=f"b{i}")  # type: ignore[arg-type]
            for i in range(15)]
    ingest(RecordingIndex(), docs, stats=stats)
    assert stats.errors == 15
    assert len(stats.error_samples) == 10


# --- B3: llm vs heuristic classification counters ------------------------------

def test_classify_counters_llm_success():
    stats = IngestStats()
    ingest(RecordingIndex(), _docs(4), classify_fn=lambda _t: "decision", stats=stats)
    assert stats.llm_classified == 4
    assert stats.heuristic_classified == 0
    assert stats.by_layer == {"decision": 4}


def test_classify_counters_llm_failure_falls_back_to_heuristic():
    def boom(_t: str) -> str:
        raise RuntimeError("api down")

    stats = IngestStats()
    ingest(RecordingIndex(), _docs(4), classify_fn=boom, stats=stats)
    assert stats.llm_classified == 0
    assert stats.heuristic_classified == 4


def test_classify_counters_no_fn_is_heuristic():
    stats = IngestStats()
    ingest(RecordingIndex(), _docs(4), stats=stats)
    assert stats.llm_classified == 0
    assert stats.heuristic_classified == 4


# --- B3: ledger lifecycle -------------------------------------------------------

def test_ledger_running_then_completed(tmp_path):
    ledger = IngestLedger(str(tmp_path / "e.db"))
    run_id = ledger.start("filesystem", "/tmp/x")
    row = ledger.get(run_id)
    assert row["status"] == "running"
    assert row["finished_at"] is None
    assert row["started_at"].endswith("+00:00")

    ledger.finish(run_id, "completed", docs=5, chunks=12, errors=1, skipped=3,
                  llm_classified=2, heuristic_classified=10,
                  error_samples=["mem:bad: TypeError"], meta={"k": "v"})
    row = ledger.get(run_id)
    assert row["status"] == "completed"
    assert row["docs"] == 5 and row["chunks"] == 12
    assert row["errors"] == 1 and row["skipped"] == 3
    assert row["llm_classified"] == 2 and row["heuristic_classified"] == 10
    assert row["error_samples"] == ["mem:bad: TypeError"]
    assert row["meta"] == {"k": "v"}
    assert row["finished_at"] is not None


def test_ledger_failed_and_dry_run_statuses(tmp_path):
    ledger = IngestLedger(str(tmp_path / "e.db"))
    r1 = ledger.start("mem", "a")
    ledger.finish(r1, "failed", meta={"exception": "RuntimeError: boom"})
    assert ledger.get(r1)["status"] == "failed"

    r2 = ledger.start("mem", "b")
    ledger.finish(r2, "dry-run", chunks=7)
    assert ledger.get(r2)["status"] == "dry-run"

    with pytest.raises(ValueError):
        ledger.finish(r2, "nonsense")

    runs = ledger.runs(limit=10)
    assert len(runs) == 2
    assert {r["run_id"] for r in runs} == {r1, r2}


def test_ledger_caps_error_samples(tmp_path):
    ledger = IngestLedger(str(tmp_path / "e.db"))
    run_id = ledger.start("mem", "x")
    ledger.finish(run_id, "completed", error_samples=[f"s{i}" for i in range(25)])
    assert len(ledger.get(run_id)["error_samples"]) == 10


# --- B7: filesystem per-dir checkpoints, skip report, exclusions ---------------

def test_two_dirs_do_not_share_a_watermark(tmp_path):
    cp_db = str(tmp_path / "e.db")
    dir_a, dir_b = tmp_path / "a", tmp_path / "b"
    dir_a.mkdir(); dir_b.mkdir()
    (dir_a / "a.md").write_text("alpha", encoding="utf-8")
    (dir_b / "b.md").write_text("beta", encoding="utf-8")

    a = FilesystemAdapter(str(dir_a), checkpoint_db=cp_db)
    assert len(list(a.fetch())) == 1
    a.commit_checkpoint()
    # Dir B must still see its file even though A advanced a watermark.
    b = FilesystemAdapter(str(dir_b), checkpoint_db=cp_db)
    assert len(list(b.fetch())) == 1
    b.commit_checkpoint()
    assert a.checkpoint_key != b.checkpoint_key
    cp = CheckpointStore(cp_db)
    assert cp.get("filesystem", a.checkpoint_key) is not None
    assert cp.get("filesystem", b.checkpoint_key) is not None


def test_skip_report_counts_and_samples(tmp_path):
    root = tmp_path / "src"
    root.mkdir()
    (root / "keep.md").write_text("keep", encoding="utf-8")
    (root / "big.md").write_text("x" * 2048, encoding="utf-8")
    (root / "weird.xyz").write_text("?", encoding="utf-8")
    (root / "blank.md").write_text("   \n", encoding="utf-8")
    (root / "boom.fail").write_text("f", encoding="utf-8")
    (root / "nodep.dep").write_text("d", encoding="utf-8")

    def _boom(_p: Path) -> str:
        raise RuntimeError("parse error")

    def _missing(_p: Path) -> str:
        raise ExtractorMissing("optional dep absent")

    adapter = FilesystemAdapter(
        str(root), max_bytes=1024,
        extra_extractors={".fail": _boom, ".dep": _missing},
    )
    docs = list(adapter.fetch())
    assert [Path(d.meta["path"]).name for d in docs] == ["keep.md"]
    rep = adapter.skip_report
    assert rep["oversize"]["count"] == 1
    assert rep["unsupported_ext"]["count"] == 1
    assert rep["empty"]["count"] == 1
    assert rep["extractor_failed"]["count"] == 1
    assert rep["extractor_missing"]["count"] == 1
    assert rep["oversize"]["samples"] == [str(root / "big.md")]


def test_skip_report_samples_capped_at_twenty(tmp_path):
    root = tmp_path / "src"
    root.mkdir()
    for i in range(25):
        (root / f"f{i:02d}.xyz").write_text("?", encoding="utf-8")
    adapter = FilesystemAdapter(str(root))
    list(adapter.fetch())
    rep = adapter.skip_report["unsupported_ext"]
    assert rep["count"] == 25
    assert len(rep["samples"]) == 20


def test_exclude_patterns_substring_and_glob(tmp_path):
    root = tmp_path / "src"
    (root / "Taxes").mkdir(parents=True)
    (root / "Taxes" / "w2.md").write_text("secret", encoding="utf-8")
    (root / "keep.md").write_text("keep", encoding="utf-8")
    (root / "statement_2024.md").write_text("bank", encoding="utf-8")

    adapter = FilesystemAdapter(
        str(root), exclude_patterns=["taxes", "statement_*.md"]
    )
    docs = list(adapter.fetch())
    assert [Path(d.meta["path"]).name for d in docs] == ["keep.md"]
    assert adapter.skip_report["excluded"]["count"] == 2


# --- B2 end-to-end: CLI dry-run writes nothing, real run then ingests ----------

def test_cli_dry_run_then_real_run(tmp_path, capsys):
    from brain.cli import main

    src = tmp_path / "vault"
    src.mkdir()
    (src / "note.md").write_text("# Note\n\nhello world", encoding="utf-8")
    (src / "junk.xyz").write_text("?", encoding="utf-8")
    db = str(tmp_path / "lance")
    entdb = str(tmp_path / "e.db")
    base = ["--db", db, "--entdb", entdb, "ingest",
            "--adapter", "filesystem", "--source", str(src)]

    assert main(base + ["--dry-run"]) == 0
    out = capsys.readouterr().out
    assert "DRY RUN" in out
    assert "docs seen:          1" in out
    assert "chunks (would add): 1" in out
    assert "unsupported_ext: 1" in out

    # Nothing written, watermark rolled back, ledger row is dry-run.
    assert BrainIndex(db, FakeEmbedder()).count() == 0
    assert CheckpointStore(entdb).all() == []
    runs = IngestLedger(entdb).runs()
    assert len(runs) == 1
    assert runs[0]["status"] == "dry-run"
    assert runs[0]["chunks"] == 1
    assert runs[0]["skipped"] == 1
    assert runs[0]["meta"]["skip_report"]["unsupported_ext"]["count"] == 1

    # The real run still sees the file (dry-run didn't consume the watermark).
    assert main(base) == 0
    assert BrainIndex(db, FakeEmbedder()).count() == 1
    runs = IngestLedger(entdb).runs()
    assert len(runs) == 2
    assert runs[0]["status"] == "completed"
    assert runs[0]["chunks"] == 1
    assert CheckpointStore(entdb).all() != []


def test_cli_exclude_flag_wires_through(tmp_path, capsys):
    from brain.cli import main

    src = tmp_path / "vault"
    src.mkdir()
    (src / "keep.md").write_text("keep", encoding="utf-8")
    (src / "tax_return.md").write_text("secret", encoding="utf-8")
    db = str(tmp_path / "lance")
    entdb = str(tmp_path / "e.db")

    assert main(["--db", db, "--entdb", entdb, "ingest", "--adapter", "filesystem",
                 "--source", str(src), "--exclude", "tax_"]) == 0
    capsys.readouterr()
    assert BrainIndex(db, FakeEmbedder()).count() == 1
    runs = IngestLedger(entdb).runs()
    assert runs[0]["skipped"] == 1
    assert runs[0]["meta"]["skip_report"]["excluded"]["count"] == 1


def test_cli_ledger_failed_on_raise(tmp_path, monkeypatch):
    from brain import cli as brain_cli

    src = tmp_path / "vault"
    src.mkdir()
    (src / "a.md").write_text("a", encoding="utf-8")
    entdb = str(tmp_path / "e.db")

    def _boom(*_a, **_kw):
        raise RuntimeError("index exploded")

    monkeypatch.setattr(brain_cli, "ingest", _boom)
    with pytest.raises(RuntimeError):
        brain_cli.main(["--db", str(tmp_path / "lance"), "--entdb", entdb,
                        "ingest", "--adapter", "filesystem", "--source", str(src)])
    runs = IngestLedger(entdb).runs()
    assert len(runs) == 1
    assert runs[0]["status"] == "failed"
    assert "RuntimeError" in runs[0]["meta"]["exception"]


# --- QA-review regression tests (2026-07-03) -------------------------------


def test_failed_run_does_not_advance_watermark(tmp_path, monkeypatch):
    """A failed run (e.g. final-flush error) must not strand files behind an
    already-committed watermark — the retry has to re-see them."""
    from brain import cli as brain_cli

    src = tmp_path / "vault"
    src.mkdir()
    (src / "a.md").write_text("alpha", encoding="utf-8")
    db, entdb = str(tmp_path / "lance"), str(tmp_path / "e.db")

    def _boom(*_a, **_kw):
        raise RuntimeError("flush exploded")

    monkeypatch.setattr(brain_cli, "ingest", _boom)
    with pytest.raises(RuntimeError):
        brain_cli.main(["--db", db, "--entdb", entdb, "ingest",
                        "--adapter", "filesystem", "--source", str(src)])
    assert all(r["adapter"] != "filesystem" for r in CheckpointStore(entdb).all())

    monkeypatch.undo()
    assert brain_cli.main(["--db", db, "--entdb", entdb, "ingest",
                           "--adapter", "filesystem", "--source", str(src)]) == 0
    assert BrainIndex(db, FakeEmbedder()).count() == 1


def test_watermark_held_when_docs_error(tmp_path, monkeypatch, capsys):
    """errors > 0 in a completed run keeps the watermark so errored docs are
    retried next run; the ledger records watermark_held."""
    from brain import cli as brain_cli

    src = tmp_path / "vault"
    src.mkdir()
    (src / "a.md").write_text("alpha", encoding="utf-8")
    db, entdb = str(tmp_path / "lance"), str(tmp_path / "e.db")

    def _fake_ingest(index, docs, *, classify_fn=None, dry_run=False,
                     stats=None, entity_store=None):
        list(docs)  # exhaust so the adapter records a pending watermark
        stats.docs = 1
        stats.errors = 1
        stats.error_samples.append("filesystem:x: Boom: nope")
        return 0

    monkeypatch.setattr(brain_cli, "ingest", _fake_ingest)
    assert brain_cli.main(["--db", db, "--entdb", entdb, "ingest",
                           "--adapter", "filesystem", "--source", str(src)]) == 0
    capsys.readouterr()
    assert all(r["adapter"] != "filesystem" for r in CheckpointStore(entdb).all())
    run = IngestLedger(entdb).runs()[0]
    assert run["status"] == "completed"
    assert run["meta"]["watermark_held"] is True


def test_missing_source_writes_failed_ledger_row(tmp_path):
    """An unmounted/missing source dir must show up in the Intake panel as a
    failed run, not vanish with only a traceback."""
    from brain.cli import main

    entdb = str(tmp_path / "e.db")
    with pytest.raises(FileNotFoundError):
        main(["--db", str(tmp_path / "lance"), "--entdb", entdb, "ingest",
              "--adapter", "filesystem", "--source", str(tmp_path / "nope")])
    runs = IngestLedger(entdb).runs()
    assert len(runs) == 1
    assert runs[0]["status"] == "failed"
    assert "FileNotFoundError" in runs[0]["meta"]["exception"]


def test_dim_guard_rejects_mismatched_embedder(tmp_path):
    """Opening a 64-dim index with a different-dim embedder fails loud
    instead of silently returning garbage recall."""
    db = str(tmp_path / "lance")
    BrainIndex(db, FakeEmbedder())  # creates the 64-dim table

    class Skinny:
        dim = 32

        def embed(self, texts):
            return [[0.0] * 32 for _ in texts]

    with pytest.raises(ValueError, match="64-dim"):
        BrainIndex(db, Skinny())


def test_bracket_exclude_is_literal(tmp_path):
    """'[old]' is a substring exclude, not a dead fnmatch char-class."""
    src = tmp_path / "vault"
    src.mkdir()
    (src / "notes [old].md").write_text("stale", encoding="utf-8")
    (src / "keep.md").write_text("keep", encoding="utf-8")
    a = FilesystemAdapter(str(src), exclude_patterns=["[old]"])
    docs = list(a.fetch())
    assert len(docs) == 1
    assert docs[0].meta["path"].endswith("keep.md")
    assert a.skip_report["excluded"]["count"] == 1


def test_dry_run_restore_is_scoped_to_adapter(tmp_path):
    """Dry-run rollback must not revert or delete checkpoints that OTHER
    adapters wrote concurrently in the shared entdb."""
    from brain.cli import _restore_checkpoints, _snapshot_checkpoints

    entdb = str(tmp_path / "e.db")
    cp = CheckpointStore(entdb)
    cp.set("gmail", "hist-1", key="history_id")
    before = _snapshot_checkpoints(entdb, "filesystem")
    # Concurrent real runs move gmail + mint a drive token mid-dry-run,
    # while the dry-run itself moves a filesystem watermark.
    cp.set("gmail", "hist-2", key="history_id")
    cp.set("drive", "tok-9", key="page_token")
    cp.set("filesystem", "2026-01-01T00:00:00+00:00", key="last_sync:abc")
    _restore_checkpoints(entdb, "filesystem", before)
    assert cp.get("gmail", "history_id") == "hist-2"
    assert cp.get("drive", "page_token") == "tok-9"
    assert cp.get("filesystem", "last_sync:abc") is None


def test_classification_counters_skip_failed_docs(monkeypatch):
    """A doc failing mid-chunking contributes one error and ZERO phantom
    classification counts."""
    from brain.core import pipeline as pl

    calls = {"n": 0}

    def flaky_tag_project(piece):
        calls["n"] += 1
        if calls["n"] == 3:  # second chunk of the second doc
            raise RuntimeError("tagger died")
        return []

    monkeypatch.setattr(pl, "tag_project", flaky_tag_project)

    class _Idx:
        def add_chunks(self, chunks):
            return len(chunks)

    body = ("# a\n" + "x" * 1700) + "\n\n# b\n" + ("y" * 1700)  # 2 chunks
    docs = [RawDoc(text="one", source="t", source_id="a"),
            RawDoc(text=body, source="t", source_id="b")]
    stats = IngestStats()
    total = pl.ingest(_Idx(), iter(docs), stats=stats)
    assert total == 1                      # only doc a landed
    assert stats.errors == 1
    assert stats.heuristic_classified == 1  # doc b's partial chunk not counted
