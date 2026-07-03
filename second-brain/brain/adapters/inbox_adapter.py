"""Inbox adapter — the universal drop folder.

Anything Wes can get into a folder feeds the brain: iPhone share-sheet saves
(point BRAIN_INBOX_DIR at an iCloud Drive folder), emails dragged out of
Mail.app (.eml), forwarded texts saved as .txt, PDFs, docs, or files written
by the API's POST /inbox. The folder IS the queue:

  BrainInbox/
    <anything supported>     <- pending intake
    processed/YYYY-MM/       <- moved here after a CLEAN ingest run
    failed/                  <- unparseable files, quarantined on commit

Move-on-commit contract (same as the filesystem/claude-code watermarks): the
adapter only RECORDS moves during fetch(); `commit_checkpoint()` executes
them, and the CLI calls it only after the pipeline — including its final
flush — succeeded with zero doc errors. A crashed run leaves every file in
place for a clean retry; chunk ids are content-hashed so retries upsert.

No checkpoint table: presence in the folder means "not yet ingested".
"""

from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable, Iterable

from ..core.pipeline import RawDoc
from .base import Adapter
from .filesystem_adapter import DEFAULT_EXTRACTORS, ExtractorMissing

ADAPTER_NAME = "inbox"
DEFAULT_INBOX_DIR = "~/BrainInbox"
PROCESSED_DIR = "processed"
FAILED_DIR = "failed"
MAX_SKIP_SAMPLES = 20
TEXT_EXTS = (".md", ".markdown", ".txt", ".text")


class _HTMLText(HTMLParser):
    """Minimal HTML -> text: keeps text nodes, breaks on block-ish tags."""

    _BREAKS = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "blockquote"}

    def __init__(self) -> None:
        super().__init__()
        self._out: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: object) -> None:
        if tag in ("script", "style"):
            self._skip_depth += 1
        elif tag in self._BREAKS:
            self._out.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style") and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self._skip_depth:
            self._out.append(data)

    def text(self) -> str:
        raw = "".join(self._out)
        lines = [ln.strip() for ln in raw.splitlines()]
        return "\n".join(ln for ln in lines if ln)


def html_to_text(html: str) -> str:
    p = _HTMLText()
    try:
        p.feed(html)
    except Exception:
        # Pathological markup: fall back to a crude tag strip.
        return re.sub(r"<[^>]+>", " ", html)
    return p.text()


def render_email(subject: str, sender: str, to: str, date: str, body: str) -> str:
    """Shared rendering for .eml files and polled mailbox messages."""
    header = [f"# {subject or '(no subject)'}", ""]
    meta_bits = [b for b in (
        f"**From:** {sender}" if sender else "",
        f"**To:** {to}" if to else "",
        f"**Date:** {date}" if date else "",
    ) if b]
    if meta_bits:
        header.append(" · ".join(meta_bits))
        header.append("")
    return "\n".join(header) + body.strip()


def _eml_to_doc_fields(raw: bytes) -> tuple[str, datetime | None, dict[str, Any]]:
    """Parse an RFC-822 message: (rendered text, sent datetime, meta)."""
    msg: EmailMessage = BytesParser(policy=policy.default).parsebytes(raw)
    subject = str(msg.get("subject", "") or "")
    sender = str(msg.get("from", "") or "")
    to = str(msg.get("to", "") or "")
    date_hdr = str(msg.get("date", "") or "")

    body_part = msg.get_body(preferencelist=("plain", "html"))
    body = ""
    if body_part is not None:
        content = body_part.get_content()
        body = html_to_text(content) if body_part.get_content_subtype() == "html" else str(content)

    sent_at: datetime | None = None
    if date_hdr:
        try:
            sent_at = parsedate_to_datetime(date_hdr)
            if sent_at.tzinfo is None:
                sent_at = sent_at.replace(tzinfo=timezone.utc)
        except (ValueError, TypeError):
            sent_at = None

    text = render_email(subject, sender, to, date_hdr, body)
    meta = {"kind": "eml", "subject": subject, "from": sender}
    return text, sent_at, meta


def _content_hash(path: Path) -> str:
    h = hashlib.sha1()
    try:
        with path.open("rb") as f:
            for block in iter(lambda: f.read(65536), b""):
                h.update(block)
    except OSError:
        h.update(str(path).encode("utf-8"))
    return h.hexdigest()


class InboxAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source_dir: str = "",
        *,
        max_bytes: int = 10 * 1024 * 1024,
        extra_extractors: dict[str, Callable[[Path], str]] | None = None,
    ) -> None:
        self.source_dir = Path(source_dir or DEFAULT_INBOX_DIR).expanduser().resolve()
        if not self.source_dir.exists():
            raise FileNotFoundError(
                f"inbox dir not found: {self.source_dir}. Create it (mkdir) or "
                "set BRAIN_INBOX_DIR / --source to your drop folder."
            )
        self.max_bytes = max_bytes
        self.extractors: dict[str, Callable[[Path], str]] = dict(DEFAULT_EXTRACTORS)
        if extra_extractors:
            self.extractors.update(extra_extractors)
        self.skip_report: dict[str, dict[str, Any]] = {}
        self._pending_processed: list[Path] = []
        self._pending_failed: list[Path] = []

    # -- intake -------------------------------------------------------------

    def fetch(self) -> Iterable[RawDoc]:
        self.skip_report = {}
        self._pending_processed = []
        self._pending_failed = []
        for path in self._pending_files():
            try:
                stat = path.stat()
            except OSError:
                self._record_skip("unreadable", path)
                continue
            if stat.st_size > self.max_bytes:
                self._record_skip("oversize", path)
                self._pending_failed.append(path)
                continue

            ext = path.suffix.lower()
            created = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
            meta: dict[str, Any] = {"path": str(path), "kind": "file", "ext": ext}
            try:
                if ext == ".eml":
                    text, sent_at, eml_meta = _eml_to_doc_fields(path.read_bytes())
                    meta.update(eml_meta)
                    if sent_at is not None:
                        created = sent_at
                elif ext in TEXT_EXTS:
                    text = path.read_text(encoding="utf-8", errors="replace")
                elif ext in self.extractors:
                    text = self.extractors[ext](path)
                else:
                    self._record_skip("unsupported_ext", path)
                    self._pending_failed.append(path)
                    continue
            except ExtractorMissing:
                # Dependency gap, not a bad file — leave in place, no quarantine.
                self._record_skip("extractor_missing", path)
                continue
            except Exception:
                self._record_skip("extractor_failed", path)
                self._pending_failed.append(path)
                continue

            text = text.strip()
            if not text:
                self._record_skip("empty", path)
                self._pending_failed.append(path)
                continue

            yield RawDoc(
                text=text,
                source=self.name,
                source_id=_content_hash(path),
                url=path.as_uri(),
                created_at=created,
                meta=meta,
            )
            self._pending_processed.append(path)

    def _pending_files(self) -> Iterable[Path]:
        skip_dirs = {PROCESSED_DIR, FAILED_DIR}
        for path in sorted(self.source_dir.rglob("*")):
            if not path.is_file() or path.name.startswith("."):
                continue
            rel_parts = path.relative_to(self.source_dir).parts
            if rel_parts and rel_parts[0] in skip_dirs:
                continue
            yield path

    def has_pending(self) -> bool:
        """Cheap pre-check so the watch loop can skip empty cycles."""
        return next(iter(self._pending_files()), None) is not None

    # -- commit -------------------------------------------------------------

    def commit_checkpoint(self) -> None:
        """Move ingested files to processed/ and broken ones to failed/.
        Called by the CLI only after a clean zero-error run — a failed run
        leaves everything in place so the next cycle retries."""
        month = datetime.now(tz=timezone.utc).strftime("%Y-%m")
        self._move_all(self._pending_processed, self.source_dir / PROCESSED_DIR / month)
        self._move_all(self._pending_failed, self.source_dir / FAILED_DIR)
        self._pending_processed = []
        self._pending_failed = []

    def _move_all(self, paths: list[Path], dest_dir: Path) -> None:
        if not paths:
            return
        dest_dir.mkdir(parents=True, exist_ok=True)
        for src in paths:
            dest = dest_dir / src.name
            n = 1
            while dest.exists():
                dest = dest_dir / f"{src.stem}-{n}{src.suffix}"
                n += 1
            try:
                src.rename(dest)
            except OSError:
                pass  # e.g. iCloud placeholder churn; retried next cycle

    def _record_skip(self, reason: str, path: Path) -> None:
        entry = self.skip_report.setdefault(reason, {"count": 0, "samples": []})
        entry["count"] += 1
        if len(entry["samples"]) < MAX_SKIP_SAMPLES:
            entry["samples"].append(str(path))
