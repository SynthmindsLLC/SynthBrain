"""Instagram adapter — Meta data export -> chunks (posts, saved, stories).

Meta killed the personal-content API (Basic Display, 2024), and scraping a
logged-in session risks account flags — so this adapter reads the OFFICIAL
data export: accountscenter.instagram.com -> Your information and
permissions -> Download your information -> JSON. Point --source at the
unzipped export root (or any folder containing the JSON files).

Handled files (all shapes are handled defensively — Meta renames these
between export generations):

  saved/saved_posts.json            saved_saved_media
  your_instagram_activity/saved/saved_posts.json
  content/posts_1.json              own posts (list or {media:[...]})
  your_instagram_activity/content/posts_1.json
  content/stories.json              ig_stories
  likes/liked_posts.json            likes_media_likes (title + href only)

One RawDoc per item; created_at from the item's unix timestamp. Instagram
exports encode text as latin-1-mangled UTF-8 — _fix_mojibake repairs it.

Re-export/re-ingest is idempotent (source ids derive from stable fields).
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "instagram"

# filename fragments -> item kind
_TARGETS = (
    ("saved_posts.json", "saved"),
    ("posts_1.json", "post"),
    ("stories.json", "story"),
    ("liked_posts.json", "liked"),
)


def _fix_mojibake(s: str) -> str:
    """Instagram exports serialize UTF-8 bytes as latin-1 code points
    (\\u00e2\\u0080\\u0099 for a right quote). Round-trip repairs it."""
    try:
        return s.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s


def _ts(value: Any) -> datetime | None:
    try:
        v = int(value)
    except (TypeError, ValueError):
        return None
    if v <= 0:
        return None
    try:
        return datetime.fromtimestamp(v, tz=timezone.utc)
    except (ValueError, OSError, OverflowError):
        return None


class InstagramAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(self, source: str) -> None:
        self.source = Path(source).expanduser()
        if not self.source.exists():
            raise FileNotFoundError(
                f"Instagram export not found: {self.source}. Download your "
                "information (JSON) from accountscenter.instagram.com and "
                "point --source at the unzipped folder."
            )

    def fetch(self) -> Iterable[RawDoc]:
        for path, kind in self._export_files():
            try:
                data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
            except json.JSONDecodeError:
                continue
            for item in self._items(data, kind):
                doc = self._to_doc(item, kind)
                if doc is not None:
                    yield doc

    def _export_files(self) -> Iterable[tuple[Path, str]]:
        if self.source.is_file():
            for fragment, kind in _TARGETS:
                if self.source.name == fragment:
                    yield self.source, kind
            return
        for fragment, kind in _TARGETS:
            for path in sorted(self.source.rglob(fragment)):
                yield path, kind

    @staticmethod
    def _items(data: Any, kind: str) -> list[dict]:
        """Export shapes vary by generation: bare list, {media:[...]},
        {ig_stories:[...]}, {saved_saved_media:[...]}, {likes_media_likes:[..]}."""
        if isinstance(data, list):
            return [d for d in data if isinstance(d, dict)]
        if isinstance(data, dict):
            for key in ("saved_saved_media", "media", "ig_stories",
                        "likes_media_likes", "posts"):
                if isinstance(data.get(key), list):
                    return [d for d in data[key] if isinstance(d, dict)]
        return []

    def _to_doc(self, item: dict, kind: str) -> RawDoc | None:
        title = _fix_mojibake(str(item.get("title", "") or ""))

        # Saved/liked items: {"title": author, "string_map_data" | "..._data":
        # {"Saved on": {"href", "timestamp"}}} — dig out href + timestamp.
        href = ""
        ts = _ts(item.get("creation_timestamp"))
        for map_key in ("string_map_data", "string_list_data"):
            payload = item.get(map_key)
            entries = (payload.values() if isinstance(payload, dict)
                       else payload if isinstance(payload, list) else [])
            for e in entries:
                if not isinstance(e, dict):
                    continue
                href = href or str(e.get("href", "") or "")
                ts = ts or _ts(e.get("timestamp"))

        # Own posts/stories: media list with uri + title + creation_timestamp.
        caption = ""
        media = item.get("media")
        if isinstance(media, list):
            for m in media:
                if isinstance(m, dict):
                    caption = caption or _fix_mojibake(str(m.get("title", "") or ""))
                    ts = ts or _ts(m.get("creation_timestamp"))
        body = _fix_mojibake(str(item.get("caption", "") or "")) or caption

        text_bits = [b for b in (title, body) if b]
        if not text_bits and not href:
            return None
        label = {"saved": "Saved post", "post": "Post", "story": "Story",
                 "liked": "Liked post"}[kind]
        lines = [f"# Instagram {label}: {title or '(untitled)'}", ""]
        if href:
            lines.append(f"**URL:** {href}")
            lines.append("")
        if body and body != title:
            lines.append(body)

        sid_basis = href or f"{kind}:{title}:{ts.isoformat() if ts else ''}"
        return RawDoc(
            text="\n".join(lines).strip(),
            source=self.name,
            source_id=hashlib.sha1(sid_basis.encode("utf-8")).hexdigest(),
            url=href,
            created_at=ts or datetime.now(tz=timezone.utc),
            meta={"kind": kind, "title": title},
        )
