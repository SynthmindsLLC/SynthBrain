"""Reddit adapter — saved posts via the account's private RSS feed.

Reddit's 2025 Responsible Builder Policy gates the JSON API behind manual
pre-approval, but every account still gets sanctioned private RSS feeds
(reddit.com/prefs/feeds). The "saved links" feed exposes saved posts and
comments as Atom without OAuth or approval:

  https://old.reddit.com/user/<name>/saved.rss?feed=<token>&user=<name>

One-time setup: copy that URL from reddit.com/prefs/feeds and export it as
REDDIT_FEED_URL (or pass --source). The watch daemon polls it alongside
AgentMail, so saving a post on Reddit is all it takes to feed the brain.

Watermark: newest entry <updated>, deferred via commit_checkpoint().
The feed carries ~25 most-recent items — a poll cadence of minutes-to-hours
never misses; the historical backlog comes from Reddit's GDPR data export
(saved_posts.csv) if ever wanted.
"""

from __future__ import annotations

import hashlib
import os
import urllib.request
from datetime import datetime, timezone

# defusedxml: network-fetched XML must be parsed with entity expansion and
# DTD processing disabled (billion-laughs / XXE hardening).
from defusedxml import ElementTree as ET
from typing import Any, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter
from .inbox_adapter import html_to_text

ADAPTER_NAME = "reddit"
ATOM = "{http://www.w3.org/2005/Atom}"
TIMEOUT = 30
MAX_BODY_CHARS = 20_000


def _parse_ts(value: str) -> datetime | None:
    try:
        dt = datetime.fromisoformat((value or "").replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


class RedditAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source: str = "",
        *,
        checkpoint_db: str | None = None,
        since: str | None = None,
    ) -> None:
        self.feed_url = source or os.environ.get("REDDIT_FEED_URL", "")
        if not self.feed_url:
            raise RuntimeError(
                "REDDIT_FEED_URL is not set. Copy your private 'saved links' "
                "feed URL from https://www.reddit.com/prefs/feeds and export "
                "it (or pass --source)."
            )
        self.checkpoint_db = checkpoint_db
        self.since = since
        url_hash = hashlib.sha1(self.feed_url.encode("utf-8")).hexdigest()[:12]
        self.checkpoint_key = f"last_sync:{url_hash}"
        self._pending_watermark: str | None = None

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (cp.get(self.name, self.checkpoint_key) if cp else None)
        newest: str | None = None

        for entry in self._entries():
            updated = entry.get("updated_iso", "")
            if watermark and updated and updated <= watermark:
                continue
            yield RawDoc(
                text=entry["text"],
                source=self.name,
                source_id=entry["id"],
                url=entry["link"],
                created_at=entry["updated"] or datetime.now(tz=timezone.utc),
                meta={"subreddit": entry["subreddit"], "kind": "saved",
                       "title": entry["title"]},
            )
            if updated and (newest is None or updated > newest):
                newest = updated

        if cp and newest:
            self._pending_watermark = newest

    def commit_checkpoint(self) -> None:
        if self.checkpoint_db and self._pending_watermark:
            CheckpointStore(self.checkpoint_db).set(
                self.name, self._pending_watermark, key=self.checkpoint_key
            )
            self._pending_watermark = None

    # -- feed parsing ---------------------------------------------------------

    def _entries(self) -> Iterable[dict[str, Any]]:
        req = urllib.request.Request(
            self.feed_url,
            # Reddit rejects the default urllib UA; a descriptive one is
            # exactly what their API guidelines ask for.
            headers={"User-Agent": "synthbrain-second-brain/0.1 (personal RSS sync)"},
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:  # noqa: S310 — user-configured feed URL
            root = ET.fromstring(resp.read())

        for e in root.findall(f"{ATOM}entry"):
            entry_id = (e.findtext(f"{ATOM}id") or "").strip()
            title = (e.findtext(f"{ATOM}title") or "").strip()
            updated_raw = (e.findtext(f"{ATOM}updated") or "").strip()
            updated = _parse_ts(updated_raw)
            link_el = e.find(f"{ATOM}link")
            link = link_el.get("href", "") if link_el is not None else ""
            cat_el = e.find(f"{ATOM}category")
            subreddit = cat_el.get("term", "") if cat_el is not None else ""
            body_html = e.findtext(f"{ATOM}content") or ""
            body = html_to_text(body_html)[:MAX_BODY_CHARS]

            if not entry_id or not (title or body):
                continue
            lines = [f"# {title or '(untitled)'}", ""]
            if subreddit:
                lines.append(f"**Subreddit:** r/{subreddit}")
            if link:
                lines.append(f"**URL:** {link}")
            lines.append("")
            if body:
                lines.append(body)
            yield {
                "id": entry_id,
                "title": title,
                "link": link,
                "subreddit": subreddit,
                "updated": updated,
                "updated_iso": updated.astimezone(timezone.utc).isoformat() if updated else "",
                "text": "\n".join(lines).strip(),
            }
