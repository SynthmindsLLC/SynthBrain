"""Filesystem adapter — walk a directory tree, ingest text/markdown/docx/pdf.

The "past" wing of Phase 1. Points it at:
  - your Obsidian vault (.md files)
  - a Downloads folder of plain docs
  - the local mirror of a Drive folder

Idempotent: file hash determines source_id, so re-running on the same tree
is a no-op upsert. Checkpoint stores the max mtime seen — keyed per source
directory (hash of the resolved path) so two trees never share a watermark —
and subsequent runs default to "files modified since last run" (--since
overrides).

Every skipped file is counted (and sampled, up to 20 paths per reason) in
`skip_report` so bulk runs report what they left behind instead of silently
dropping it. Reasons: excluded, oversize, unsupported_ext, extractor_missing,
extractor_failed, empty.

Extractors auto-load only if the relevant package is installed:
  .md, .txt, .markdown          -> always (built in)
  .docx                          -> needs `docx2txt`
  .pdf                            -> needs `pypdf`
Missing extractors are skipped (reported), not fatal.
"""

from __future__ import annotations

import fnmatch
import hashlib
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "filesystem"
DEFAULT_TEXT_EXTS = (".md", ".markdown", ".txt", ".text")
SKIP_DIRS = frozenset({".git", "node_modules", ".venv", "venv", "__pycache__",
                       ".pytest_cache", "brain_index", ".next", "dist"})
MAX_SKIP_SAMPLES = 20
_GLOB_CHARS = ("*", "?", "[")


class ExtractorMissing(Exception):
    """Raised by an extractor whose optional dependency isn't installed."""


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
        exclude_patterns: list[str] | None = None,
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
        # Case-insensitive substrings or globs matched against the relative path.
        self.exclude_patterns = [p.lower() for p in (exclude_patterns or [])]
        # Namespace the watermark per source dir so two trees don't share one.
        dir_hash = hashlib.sha1(str(self.source_dir).encode("utf-8")).hexdigest()[:12]
        self.checkpoint_key = f"last_sync:{dir_hash}"
        self.skip_report: dict[str, dict[str, Any]] = {}

    def fetch(self) -> Iterable[RawDoc]:
        self.skip_report = {}
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (
            _parse_iso(cp.get(self.name, self.checkpoint_key)) if cp else None
        )
        newest_seen: datetime | None = None

        for path in _walk(self.source_dir):
            if self._is_excluded(path):
                self._record_skip("excluded", path)
                continue
            try:
                stat = path.stat()
            except OSError:
                continue
            if stat.st_size > self.max_bytes:
                self._record_skip("oversize", path)
                continue
            mtime = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
            if watermark and mtime <= watermark:
                continue
            ext = path.suffix.lower()
            extractor = self.extractors.get(ext)
            if not extractor:
                self._record_skip("unsupported_ext", path)
                continue
            try:
                text = extractor(path).strip()
            except ExtractorMissing:
                self._record_skip("extractor_missing", path)
                continue
            except Exception:
                self._record_skip("extractor_failed", path)
                continue
            if not text:
                self._record_skip("empty", path)
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
            cp.set(self.name, newest_seen.isoformat(), key=self.checkpoint_key)

    def _is_excluded(self, path: Path) -> bool:
        if not self.exclude_patterns:
            return False
        rel = path.relative_to(self.source_dir).as_posix().lower()
        for pat in self.exclude_patterns:
            if any(ch in pat for ch in _GLOB_CHARS):
                if fnmatch.fnmatch(rel, pat):
                    return True
            elif pat in rel:
                return True
        return False

    def _record_skip(self, reason: str, path: Path) -> None:
        entry = self.skip_report.setdefault(reason, {"count": 0, "samples": []})
        entry["count"] += 1
        if len(entry["samples"]) < MAX_SKIP_SAMPLES:
            entry["samples"].append(str(path))


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
    except ImportError as exc:
        raise ExtractorMissing("docx2txt not installed") from exc
    return docx2txt.process(str(path)) or ""


def _read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise ExtractorMissing("pypdf not installed") from exc
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
