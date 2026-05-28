"""Filesystem adapter — walk a directory tree, ingest text/markdown/docx/pdf.

The "past" wing of Phase 1. Points it at:
  - your Obsidian vault (.md files)
  - a Downloads folder of plain docs
  - the local mirror of a Drive folder

Idempotent: file hash determines source_id, so re-running on the same tree
is a no-op upsert. Checkpoint stores the max mtime seen, so subsequent runs
default to "files modified since last run" (override with --since).

Extractors auto-load only if the relevant package is installed:
  .md, .txt, .markdown          -> always (built in)
  .docx                          -> needs `docx2txt`
  .pdf                            -> needs `pypdf`
Missing extractors are skipped (logged), not fatal.
"""

from __future__ import annotations

import hashlib
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "filesystem"
DEFAULT_TEXT_EXTS = (".md", ".markdown", ".txt", ".text")
SKIP_DIRS = frozenset({".git", "node_modules", ".venv", "venv", "__pycache__",
                       ".pytest_cache", "brain_index", ".next", "dist"})


class FilesystemAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source_dir: str,
        *,
        checkpoint_db: str | None = None,
        since: str | None = None,
        max_bytes: int = 10 * 1024 * 1024,
        extra_extractors: dict[str, Callable[[Path], str]] | None = None,
    ) -> None:
        self.source_dir = Path(source_dir).expanduser().resolve()
        if not self.source_dir.exists():
            raise FileNotFoundError(f"source dir not found: {self.source_dir}")
        self.checkpoint_db = checkpoint_db
        self.since = _parse_iso(since) if since else None
        self.max_bytes = max_bytes
        self.extractors: dict[str, Callable[[Path], str]] = dict(DEFAULT_EXTRACTORS)
        if extra_extractors:
            self.extractors.update(extra_extractors)

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (_parse_iso(cp.get(self.name)) if cp else None)
        newest_seen: datetime | None = None

        for path in _walk(self.source_dir):
            try:
                stat = path.stat()
            except OSError:
                continue
            if stat.st_size > self.max_bytes:
                continue
            mtime = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
            if watermark and mtime <= watermark:
                continue
            ext = path.suffix.lower()
            extractor = self.extractors.get(ext)
            if not extractor:
                continue
            try:
                text = extractor(path).strip()
            except Exception:
                continue
            if not text:
                continue
            yield RawDoc(
                text=text,
                source=self.name,
                source_id=_content_hash(path, ext),
                url=path.as_uri(),
                created_at=mtime,
                meta={
                    "path": str(path),
                    "ext": ext,
                    "bytes": stat.st_size,
                },
            )
            if newest_seen is None or mtime > newest_seen:
                newest_seen = mtime

        if cp and newest_seen:
            cp.set(self.name, newest_seen.isoformat())


def _walk(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in filenames:
            if fn.startswith("."):
                continue
            yield Path(dirpath) / fn


def _content_hash(path: Path, ext: str) -> str:
    h = hashlib.sha1()
    h.update(str(path).encode("utf-8"))
    h.update(b":")
    h.update(ext.encode("utf-8"))
    try:
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
    except OSError:
        pass
    return h.hexdigest()


def _parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_docx(path: Path) -> str:
    try:
        import docx2txt
    except ImportError:
        return ""
    return docx2txt.process(str(path)) or ""


def _read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""
    reader = PdfReader(str(path))
    pages = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            pages.append("")
    return "\n\n".join(pages)


DEFAULT_EXTRACTORS: dict[str, Callable[[Path], str]] = {
    ext: _read_text for ext in DEFAULT_TEXT_EXTS
}
DEFAULT_EXTRACTORS[".docx"] = _read_docx
DEFAULT_EXTRACTORS[".pdf"] = _read_pdf
