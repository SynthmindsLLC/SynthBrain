"""Slack adapter — DMs + private channels you're in -> conversation chunks.

The "what we discussed at work" pipeline for Slack, mirroring the iMessage
adapter's shape: per-channel thread aggregated into ~250-word chunks,
emitted as one RawDoc per chunk, with speaker prefixes.

Uses Slack Web API with a **user token** (xoxp-...) because DMs and most
private channels aren't visible to a bot token.

  conversations.list             list all channels (DMs, group DMs, private)
  conversations.history          paged messages per channel, oldest=watermark
  conversations.replies          thread replies (one extra call per thread)
  users.info                     resolve user IDs to display names (cached)

Required scopes on the user token:
  channels:history, groups:history, im:history, mpim:history,
  users:read, channels:read, groups:read, im:read, mpim:read

Incremental sync via per-channel `latest_ts` checkpoint.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "slack"
SLACK_API = "https://slack.com/api"

DEFAULT_WORDS_PER_GROUP = 250
DEFAULT_TIMEOUT = 25
DEFAULT_PAGE_SIZE = 200
EXCLUDED_CHANNEL_TYPES: tuple[str, ...] = ()   # caller can override


class SlackAuthError(RuntimeError):
    pass


class SlackAPIError(RuntimeError):
    pass


class SlackAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        *,
        token: str | None = None,
        types: str = "im,mpim,private_channel",
        checkpoint_db: str | None = None,
        words_per_group: int = DEFAULT_WORDS_PER_GROUP,
        include_threads: bool = True,
        max_channels: int | None = None,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.token = token or os.environ.get("SLACK_USER_TOKEN") or os.environ.get("SLACK_TOKEN")
        if not self.token:
            raise SlackAuthError(
                "SLACK_USER_TOKEN not set. Create a user token (xoxp-...) at "
                "api.slack.com/apps and put it in .env.local."
            )
        self.types = types
        self.checkpoint_db = checkpoint_db
        self.words_per_group = max(50, words_per_group)
        self.include_threads = include_threads
        self.max_channels = max_channels
        self.timeout = timeout
        self._user_cache: dict[str, str] = {}

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        seen = 0
        for channel in self._list_channels():
            channel_id = channel.get("id")
            if not channel_id:
                continue
            display = self._channel_display(channel)
            ckey = f"latest_ts::{channel_id}"
            watermark = cp.get(self.name, key=ckey) if cp else None
            newest_ts: str | None = watermark

            messages = list(self._iter_history(channel_id, watermark))
            if self.include_threads:
                messages = self._expand_threads(channel_id, messages)
            if not messages:
                continue

            for doc in self._messages_to_docs(channel_id, display, messages):
                yield doc
                ts = doc.meta.get("max_ts")
                if ts and (newest_ts is None or float(ts) > float(newest_ts or 0)):
                    newest_ts = ts

            if cp and newest_ts:
                cp.set(self.name, newest_ts, key=ckey)

            seen += 1
            if self.max_channels and seen >= self.max_channels:
                return

    # ---- conversation enumeration ------------------------------------

    def _list_channels(self) -> Iterable[dict]:
        cursor = ""
        while True:
            payload = self._get("conversations.list", {
                "types": self.types,
                "exclude_archived": "true",
                "limit": DEFAULT_PAGE_SIZE,
                "cursor": cursor,
            })
            for c in payload.get("channels") or []:
                yield c
            cursor = (payload.get("response_metadata") or {}).get("next_cursor", "")
            if not cursor:
                return

    def _channel_display(self, channel: dict) -> str:
        if channel.get("is_im"):
            user_id = channel.get("user")
            return f"DM with {self._user_name(user_id)}" if user_id else "DM"
        if channel.get("is_mpim") or channel.get("is_group"):
            name = channel.get("name") or channel.get("name_normalized") or ""
            return f"#{name}" if name else "Group conversation"
        name = channel.get("name") or channel.get("name_normalized") or ""
        return f"#{name}"

    def _iter_history(self, channel_id: str, watermark: str | None) -> Iterable[dict]:
        cursor = ""
        oldest = watermark or "0"
        while True:
            payload = self._get("conversations.history", {
                "channel": channel_id,
                "oldest": oldest,
                "limit": DEFAULT_PAGE_SIZE,
                "cursor": cursor,
                "inclusive": "false",
            })
            for m in reversed(payload.get("messages") or []):
                yield m
            cursor = (payload.get("response_metadata") or {}).get("next_cursor", "")
            if not cursor:
                return

    def _expand_threads(self, channel_id: str, messages: list[dict]) -> list[dict]:
        out: list[dict] = []
        for m in messages:
            out.append(m)
            if (m.get("reply_count") or 0) > 0 and m.get("thread_ts"):
                payload = self._get("conversations.replies", {
                    "channel": channel_id,
                    "ts": m["thread_ts"],
                    "limit": DEFAULT_PAGE_SIZE,
                })
                # First reply IS the parent; skip it to avoid dup.
                for r in (payload.get("messages") or [])[1:]:
                    out.append(r)
        return out

    # ---- shaping ------------------------------------------------------

    def _messages_to_docs(
        self, channel_id: str, display: str, messages: list[dict]
    ) -> Iterable[RawDoc]:
        # Sort by ts ascending so chunks read chronologically.
        messages.sort(key=lambda m: float(m.get("ts") or 0))
        lines: list[tuple[str, str, str]] = []  # (ts, speaker, text)
        participants: set[str] = set()
        for m in messages:
            text = (m.get("text") or "").strip()
            if not text:
                continue
            user_id = m.get("user") or m.get("bot_id")
            speaker = self._user_name(user_id)
            participants.add(speaker)
            ts = m.get("ts") or "0"
            lines.append((ts, speaker, text))
        if not lines:
            return

        buf: list[tuple[str, str, str]] = []
        buf_words = 0
        group_idx = 0
        for entry in lines:
            buf.append(entry)
            buf_words += len(entry[2].split())
            if buf_words >= self.words_per_group:
                yield _emit_group(channel_id, display, sorted(participants), buf, group_idx)
                group_idx += 1
                buf = []
                buf_words = 0
        if buf:
            yield _emit_group(channel_id, display, sorted(participants), buf, group_idx)

    def _user_name(self, user_id: str | None) -> str:
        if not user_id:
            return "unknown"
        if user_id in self._user_cache:
            return self._user_cache[user_id]
        try:
            payload = self._get("users.info", {"user": user_id})
        except SlackAPIError:
            self._user_cache[user_id] = user_id
            return user_id
        user = payload.get("user") or {}
        profile = user.get("profile") or {}
        name = (
            profile.get("real_name") or profile.get("display_name")
            or user.get("name") or user_id
        )
        self._user_cache[user_id] = name
        return name

    # ---- HTTP ---------------------------------------------------------

    def _get(self, method: str, params: dict[str, Any]) -> dict:
        qs = urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, "")})
        url = f"{SLACK_API}/{method}" + (f"?{qs}" if qs else "")
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "User-Agent": "synthbrain-slack/0.1",
        })
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                body = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                raise SlackAuthError(f"Slack auth failed ({e.code})") from e
            raise SlackAPIError(f"Slack {method} -> HTTP {e.code}") from e
        except urllib.error.URLError as e:
            raise SlackAPIError(f"Slack network error: {e.reason}") from e
        if not body.get("ok", False):
            err = body.get("error", "unknown")
            if err in ("invalid_auth", "not_authed", "token_revoked"):
                raise SlackAuthError(f"Slack auth: {err}")
            raise SlackAPIError(f"Slack {method} -> {err}")
        return body


def _emit_group(
    channel_id: str, display: str, participants: list[str],
    buf: list[tuple[str, str, str]], group_idx: int,
) -> RawDoc:
    first_ts = buf[0][0]
    last_ts = buf[-1][0]
    created = datetime.fromtimestamp(float(last_ts), tz=timezone.utc)
    body_lines = [
        f"# {display}",
        f"_Participants:_ {', '.join(participants) or '(unknown)'}",
        f"_When:_ {datetime.fromtimestamp(float(first_ts), tz=timezone.utc).isoformat()} -> "
        f"{created.isoformat()}",
        "",
    ]
    for _ts, speaker, text in buf:
        body_lines.append(f"{speaker}: {text}")
    return RawDoc(
        text="\n".join(body_lines).strip(),
        source=ADAPTER_NAME,
        source_id=f"channel:{channel_id}:{group_idx}",
        url=f"slack://channel?team=&id={channel_id}",
        created_at=created,
        meta={
            "channel_id": channel_id,
            "display": display,
            "participants": participants,
            "min_ts": first_ts,
            "max_ts": last_ts,
            "message_count": len(buf),
        },
    )
