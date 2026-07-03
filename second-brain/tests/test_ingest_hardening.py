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
    # Dir B must still see its file even though A advanced a watermark.
    b = FilesystemAdapter(str(dir_b), checkpoint_db=cp_db)
    assert len(list(b.fetch())) == 1
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
