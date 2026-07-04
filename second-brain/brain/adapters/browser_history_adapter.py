"""Browser-history adapter — Chrome visit history -> daily digest chunks.

The promnesia insight (karlicoss): browsing history is the densest record of
what you were *investigating*. Chrome keeps ~90 days in a sqlite db per
profile; this adapter renders one RawDoc per day per profile:

  # Browsing — 2026-07-03 (Default)
  - 09:14 Newman 2001 fractional weighting — arxiv.org
    https://arxiv.org/abs/cond-mat/0011144
  ...

Grouping by day keeps the index sane (dozens of chunks/day, not thousands of
one-line docs) while queries like "what was I researching last Tuesday"
resolve naturally. Search-engine queries are kept — they ARE the intent.

Chrome locks the db while running, so it is copied to a temp file first
(standard practice; read-only on the copy). Noise filtered: chrome://,
about:, data:, localhost dev servers, auth/redirect URLs, sub-15-char
titles that equal the URL.

Watermark: newest visit_time (WebKit epoch), deferred via
commit_checkpoint(); namespaced per profile db path. The CURRENT day is
never emitted (it would produce an unstable half-day doc that a later run
must overwrite) — each day ships once it is over.
"""

from __future__ import annotations

import hashlib
import shutil
import sqlite3
import tempfile
import urllib.parse
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "browser-history"
DEFAULT_CHROME_DIR = "~/Library/Application Support/Google/Chrome"
_WEBKIT_TO_UNIX = 11_644_473_600
MAX_ENTRIES_PER_DAY = 400

_SKIP_SCHEMES = ("chrome://", "chrome-extension://", "about:", "data:",
                 "file://", "javascript:")
_SKIP_HOSTS = ("localhost", "127.0.0.1", "0.0.0.0")
_SKIP_URL_FRAGMENTS = ("/oauth", "accounts.google.com/o/", "/login?",
                        "/signin?", "/auth/callback", "/logout")


def _webkit_dt(micros: int) -> datetime | None:
    if not micros or micros <= 0:
        return None
    try:
        return datetime.fromtimestamp(micros / 1_000_000 - _WEBKIT_TO_UNIX,
                                      tz=timezone.utc)
    except (ValueError, OSError, OverflowError):
        return None


def _keep(url: str, title: str) -> bool:
    low = url.lower()
    if any(low.startswith(s) for s in _SKIP_SCHEMES):
        return False
    try:
        host = urllib.parse.urlsplit(url).hostname or ""
    except ValueError:
        return False
    if host in _SKIP_HOSTS:
        return False
    if any(f in low for f in _SKIP_URL_FRAGMENTS):
        return False
    return bool(title.strip()) or len(url) < 200


class BrowserHistoryAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source: str = "",
        *,
        checkpoint_db: str | None = None,
        since: str | None = None,
        max_entries_per_day: int = MAX_ENTRIES_PER_DAY,
    ) -> None:
        base = Path(source or DEFAULT_CHROME_DIR).expanduser()
        if not base.exists():
            raise FileNotFoundError(
                f"browser-history source not found: {base}. Point --source at "
                "a Chrome user-data dir (or one profile's History file)."
            )
        # Accept: a Chrome user-data dir (walk profiles), a profile dir, or a
        # History file directly.
        if base.is_file():
            self.history_files = [base]
        elif (base / "History").exists():
            self.history_files = [base / "History"]
        else:
            self.history_files = sorted(
                p / "History" for p in base.iterdir()
                if p.is_dir() and (p / "History").exists()
            )
        self.checkpoint_db = checkpoint_db
        self.since = since
        self.max_entries_per_day = max_entries_per_day
        src_hash = hashlib.sha1(str(base).encode("utf-8")).hexdigest()[:12]
        self.checkpoint_key = f"last_sync:{src_hash}"
        self._pending_watermark: str | None = None
        self.skip_report: dict[str, dict[str, Any]] = {}

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (cp.get(self.name, self.checkpoint_key) if cp else None)
        wm_dt = None
        if watermark:
            try:
                wm_dt = datetime.fromisoformat(watermark)
            except ValueError:
                wm_dt = None
        today = datetime.now(tz=timezone.utc).date().isoformat()
        newest: datetime | None = None

        for history in self.history_files:
            profile = history.parent.name
            try:
                rows = self._visits(history)
            except (sqlite3.Error, OSError):
                self._record_skip("unreadable", history)
                continue

            by_day: dict[str, list[tuple[datetime, str, str]]] = defaultdict(list)
            for visit_dt, url, title in rows:
                if wm_dt and visit_dt <= wm_dt:
                    continue
                day = visit_dt.date().isoformat()
                if day >= today:
                    continue  # current day ships once it's over
                by_day[day].append((visit_dt, url, title))
                if newest is None or visit_dt > newest:
                    newest = visit_dt

            for day, entries in sorted(by_day.items()):
                entries.sort(key=lambda e: e[0])
                if len(entries) > self.max_entries_per_day:
                    entries = entries[: self.max_entries_per_day]
                lines = [f"# Browsing — {day} ({profile})", ""]
                seen_urls: set[str] = set()
                for visit_dt, url, title in entries:
                    if url in seen_urls:
                        continue
                    seen_urls.add(url)
                    host = urllib.parse.urlsplit(url).hostname or ""
                    label = title.strip() or url
                    lines.append(f"- {visit_dt.strftime('%H:%M')} {label} — {host}")
                    lines.append(f"  {url}")
                yield RawDoc(
                    text="\n".join(lines),
                    source=self.name,
                    source_id=f"{profile}:{day}",
                    url="",
                    created_at=datetime.fromisoformat(day + "T23:59:59+00:00"),
                    meta={"profile": profile, "day": day, "visits": len(seen_urls)},
                )

        if cp and newest:
            self._pending_watermark = newest.isoformat()

    def commit_checkpoint(self) -> None:
        if self.checkpoint_db and self._pending_watermark:
            CheckpointStore(self.checkpoint_db).set(
                self.name, self._pending_watermark, key=self.checkpoint_key
            )
            self._pending_watermark = None

    # -- sqlite ---------------------------------------------------------------

    def _visits(self, history: Path) -> list[tuple[datetime, str, str]]:
        """Copy-then-read: Chrome holds the db locked while running."""
        with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=True) as tmp:
            shutil.copyfile(history, tmp.name)
            con = sqlite3.connect(f"file:{tmp.name}?mode=ro", uri=True)
            try:
                rows = con.execute(
                    """SELECT v.visit_time, u.url, COALESCE(u.title, '')
                       FROM visits v JOIN urls u ON u.id = v.url
                       ORDER BY v.visit_time""",
                ).fetchall()
            finally:
                con.close()
        out: list[tuple[datetime, str, str]] = []
        for visit_time, url, title in rows:
            dt = _webkit_dt(visit_time)
            if dt is None or not _keep(url, title):
                continue
            out.append((dt, url, title))
        return out

    def _record_skip(self, reason: str, path: Path) -> None:
        entry = self.skip_report.setdefault(reason, {"count": 0, "samples": []})
        entry["count"] += 1
        if len(entry["samples"]) < 20:
            entry["samples"].append(str(path))
