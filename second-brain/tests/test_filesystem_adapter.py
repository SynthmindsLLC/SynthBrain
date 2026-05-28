"""Filesystem adapter tests — walk, idempotent hash, checkpoint, skip dirs."""

from __future__ import annotations

import tempfile
import time
from pathlib import Path

from brain.adapters.filesystem_adapter import FilesystemAdapter, SKIP_DIRS
from brain.core.checkpoint import CheckpointStore


def test_walks_md_and_txt():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "a.md").write_text("# Hello\n\nworld", encoding="utf-8")
        (root / "b.txt").write_text("plain text", encoding="utf-8")
        (root / "c.bin").write_bytes(b"\x00\x01\x02")
        docs = list(FilesystemAdapter(str(root)).fetch())
        names = {Path(d.meta["path"]).name for d in docs}
        assert names == {"a.md", "b.txt"}


def test_skips_known_dirs():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        for skip in list(SKIP_DIRS)[:3]:
            (root / skip).mkdir(parents=True, exist_ok=True)
            (root / skip / "should_be_skipped.md").write_text("hidden", encoding="utf-8")
        (root / "kept.md").write_text("kept", encoding="utf-8")
        docs = list(FilesystemAdapter(str(root)).fetch())
        names = {Path(d.meta["path"]).name for d in docs}
        assert names == {"kept.md"}


def test_id_is_stable_across_runs():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "a.md").write_text("# X", encoding="utf-8")
        ids_first = [d.source_id for d in FilesystemAdapter(str(root)).fetch()]
        ids_second = [d.source_id for d in FilesystemAdapter(str(root)).fetch()]
        assert ids_first == ids_second


def test_checkpoint_skips_unchanged_files_on_second_run():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        cp = str(root / "e.db")
        (root / "first.md").write_text("first", encoding="utf-8")
        first = list(FilesystemAdapter(str(root), checkpoint_db=cp).fetch())
        assert len(first) == 1

        # Second run with no changes: should yield nothing.
        second = list(FilesystemAdapter(str(root), checkpoint_db=cp).fetch())
        assert len(second) == 0

        # Add a new, newer file -> should pick it up.
        time.sleep(1.0)
        (root / "later.md").write_text("later", encoding="utf-8")
        third = list(FilesystemAdapter(str(root), checkpoint_db=cp).fetch())
        names = {Path(d.meta["path"]).name for d in third}
        assert "later.md" in names
        assert "first.md" not in names


def test_oversize_files_skipped():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "small.md").write_text("hi", encoding="utf-8")
        (root / "big.md").write_text("x" * 4096, encoding="utf-8")
        docs = list(FilesystemAdapter(str(root), max_bytes=1024).fetch())
        names = {Path(d.meta["path"]).name for d in docs}
        assert names == {"small.md"}


def test_checkpoint_persists_via_store():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        cp_db = str(root / "e.db")
        (root / "a.md").write_text("a", encoding="utf-8")
        list(FilesystemAdapter(str(root), checkpoint_db=cp_db).fetch())
        cp = CheckpointStore(cp_db)
        assert cp.get("filesystem") is not None
