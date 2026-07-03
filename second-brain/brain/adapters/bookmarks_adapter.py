"""Bookmarks adapter — browser bookmarks -> chunks.

Two input shapes:

  1. Chrome/Brave/Edge `Bookmarks` JSON (default: Chrome's Default profile).
     Read directly — no export step, no Full Disk Access needed.
  2. The universal Netscape `bookmarks.html` export (Safari: File -> Export
     Bookmarks; Firefox: Manage Bookmarks -> Export). Point --source at it.

One RawDoc per bookmark: title + folder path + URL, with the bookmark's own
added-date as created_at (Chrome stores WebKit timestamps — microseconds
since 1601-01-01). Folder paths carry real signal ("Reading/AI/Agents" tells
the tagger more than the URL does).

Watermark: newest added-date, deferred via commit_checkpoint() (the CLI
commits only after a clean zero-error run), namespaced per source file so a
Chrome profile and an exported .html never share one.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "bookmarks"
DEFAULT_CHROME_PATH = (
    "~/Library/Application Support/Google/Chrome/Default/Bookmarks"
)
# WebKit epoch (1601-01-01) to Unix epoch (1970-01-01), in seconds.
_WEBKIT_TO_UNIX = 11_644_473_600


def _webkit_ts(value: Any) -> datetime | None:
    try:
        micros = int(value)
    except (TypeError, ValueError):
        return None
    if micros <= 0:
        return None
    try:
        return datetime.fromtimestamp(micros / 1_000_000 - _WEBKIT_TO_UNIX,
                                      tz=timezone.utc)
    except (ValueError, OSError, OverflowError):
        return None


def _render(title: str, folder: str, url: str) -> str:
    lines = [f"# {title or url}", ""]
    if folder:
        lines.append(f"**Folder:** {folder}")
    lines.append(f"**URL:** {url}")
    return "\n".join(lines)


class _NetscapeParser(HTMLParser):
    """Parses the Netscape bookmark-file format every browser exports:
    <H3> opens a folder, <A HREF ADD_DATE> is a bookmark, </DL> closes."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._stack: list[str] = []
        self._pending: dict[str, Any] | None = None
        self._capture: str | None = None  # 'folder' | 'link'
        self.bookmarks: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        tag = tag.lower()
        if tag == "h3":
            self._capture = "folder"
            self._pending = {"text": ""}
        elif tag == "a":
            d = dict((k.lower(), v) for k, v in attrs)
            self._pending = {"text": "", "url": d.get("href", ""),
                             "add_date": d.get("add_date", "")}
            self._capture = "link"

    def handle_data(self, data: str) -> None:
        if self._capture and self._pending is not None:
            self._pending["text"] += data

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "h3" and self._capture == "folder" and self._pending:
            self._stack.append(self._pending["text"].strip())
            self._capture = None
        elif tag == "a" and self._capture == "link" and self._pending:
            if self._pending.get("url", "").startswith(("http://", "https://")):
                self.bookmarks.append({
                    "name": self._pending["text"].strip(),
                    "url": self._pending["url"],
                    "folder": "/".join(self._stack),
                    "add_date": self._pending.get("add_date", ""),
                })
            self._capture = None
        elif tag == "dl" and self._stack:
            self._stack.pop()


class BookmarksAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source: str = "",
        *,
        checkpoint_db: str | None = None,
        since: str | None = None,
    ) -> None:
        self.source = Path(source or DEFAULT_CHROME_PATH).expanduser()
        if not self.source.exists():
            raise FileNotFoundError(
                f"bookmarks source not found: {self.source}. Point --source at "
                "a Chrome profile's Bookmarks file or an exported bookmarks.html "
                "(Safari/Firefox: export from the bookmarks manager)."
            )
        self.checkpoint_db = checkpoint_db
        self.since = since
        src_hash = hashlib.sha1(str(self.source).encode("utf-8")).hexdigest()[:12]
        self.checkpoint_key = f"last_sync:{src_hash}"
        self._pending_watermark: str | None = None

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (cp.get(self.name, self.checkpoint_key) if cp else None)
        newest: str | None = None
        fallback = datetime.fromtimestamp(self.source.stat().st_mtime, tz=timezone.utc)

        for bm in self._iter_bookmarks():
            added = bm.get("added") or fallback
            added_iso = added.astimezone(timezone.utc).isoformat()
            if watermark and added_iso <= watermark:
                continue
            url = bm["url"]
            yield RawDoc(
                text=_render(bm.get("name", ""), bm.get("folder", ""), url),
                source=self.name,
                source_id=bm.get("guid") or hashlib.sha1(url.encode()).hexdigest(),
                url=url,
                created_at=added,
                meta={"folder": bm.get("folder", ""), "title": bm.get("name", "")},
            )
            if newest is None or added_iso > newest:
                newest = added_iso

        if cp and newest:
            self._pending_watermark = newest

    def commit_checkpoint(self) -> None:
        if self.checkpoint_db and self._pending_watermark:
            CheckpointStore(self.checkpoint_db).set(
                self.name, self._pending_watermark, key=self.checkpoint_key
            )
            self._pending_watermark = None

    # -- parsers ------------------------------------------------------------

    def _iter_bookmarks(self) -> Iterable[dict[str, Any]]:
        if self.source.suffix.lower() in (".html", ".htm"):
            parser = _NetscapeParser()
            parser.feed(self.source.read_text(encoding="utf-8", errors="replace"))
            for bm in parser.bookmarks:
                added = None
                if bm.get("add_date"):
                    try:  # Netscape ADD_DATE is unix seconds
                        added = datetime.fromtimestamp(int(bm["add_date"]), tz=timezone.utc)
                    except (ValueError, OSError, OverflowError):
                        added = None
                yield {**bm, "added": added}
            return

        data = json.loads(self.source.read_text(encoding="utf-8", errors="replace"))
        roots = data.get("roots", {})
        for root in roots.values():
            if isinstance(root, dict):
                yield from self._walk_chrome(root, [])

    def _walk_chrome(self, node: dict, path: list[str]) -> Iterable[dict[str, Any]]:
        ntype = node.get("type")
        if ntype == "url":
            url = node.get("url", "")
            if url.startswith(("http://", "https://")):
                yield {
                    "name": node.get("name", ""),
                    "url": url,
                    "folder": "/".join(path),
                    "guid": node.get("guid", ""),
                    "added": _webkit_ts(node.get("date_added")),
                }
            return
        children = node.get("children")
        if isinstance(children, list):
            name = node.get("name", "")
            sub = path + [name] if name and path is not None else path
            for child in children:
                if isinstance(child, dict):
                    yield from self._walk_chrome(child, sub)
