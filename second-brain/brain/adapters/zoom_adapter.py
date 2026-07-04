"""Zoom adapter — cloud recording transcripts -> chunks.

Auth: Zoom Server-to-Server OAuth (marketplace.zoom.us -> Develop -> Build
App -> Server-to-Server OAuth; scopes: cloud_recording:read:list_user_recordings
or the classic recording:read). One-time setup, no user consent dance:

  ZOOM_ACCOUNT_ID
  ZOOM_CLIENT_ID
  ZOOM_CLIENT_SECRET

One RawDoc per recorded meeting: topic + date + the audio TRANSCRIPT (VTT,
parsed to speaker lines); falls back to the in-meeting CHAT file when no
transcript exists. Requires cloud recording with audio transcript enabled in
Zoom settings. Watermark: newest meeting start_time, deferred via
commit_checkpoint(). Note: Zoom's list API returns at most ~6 months back
per window; the adapter walks month windows from the watermark (or
--since) to now.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from typing import Any, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "zoom"
API = "https://api.zoom.us/v2"
TOKEN_URL = "https://zoom.us/oauth/token"
TIMEOUT = 30
WINDOW_DAYS = 30
MAX_WINDOWS = 24  # backstop: two years
MAX_TRANSCRIPT_CHARS = 400_000


class ZoomAuthError(RuntimeError):
    pass


def _parse_ts(value: str) -> datetime | None:
    try:
        dt = datetime.fromisoformat((value or "").replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def vtt_to_text(vtt: str) -> str:
    """WEBVTT -> speaker lines: drop the header, cue indices, and timestamp
    lines; keep payload text (Zoom emits 'Name: words' payloads)."""
    out: list[str] = []
    for raw in vtt.splitlines():
        line = raw.strip()
        if (not line or line.upper().startswith("WEBVTT") or "-->" in line
                or line.isdigit()):
            continue
        out.append(line)
    # Collapse consecutive duplicate lines (VTT rolling captions).
    deduped: list[str] = []
    for line in out:
        if not deduped or deduped[-1] != line:
            deduped.append(line)
    return "\n".join(deduped)


class ZoomAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source: str = "",
        *,
        checkpoint_db: str | None = None,
        since: str | None = None,
    ) -> None:
        self.user = source or "me"
        self.account_id = os.environ.get("ZOOM_ACCOUNT_ID", "")
        self.client_id = os.environ.get("ZOOM_CLIENT_ID", "")
        self.client_secret = os.environ.get("ZOOM_CLIENT_SECRET", "")
        if not all([self.account_id, self.client_id, self.client_secret]):
            raise ZoomAuthError(
                "Missing ZOOM_ACCOUNT_ID / ZOOM_CLIENT_ID / ZOOM_CLIENT_SECRET. "
                "Create a Server-to-Server OAuth app at marketplace.zoom.us "
                "with recording read scope and export all three."
            )
        self.checkpoint_db = checkpoint_db
        self.since = since
        user_hash = hashlib.sha1(self.user.encode("utf-8")).hexdigest()[:12]
        self.checkpoint_key = f"last_sync:{user_hash}"
        self._pending_watermark: str | None = None
        self._token: str | None = None

    # -- intake ---------------------------------------------------------------

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (cp.get(self.name, self.checkpoint_key) if cp else None)
        self._token = self._mint_token()
        newest: str | None = None

        start = _parse_ts(watermark) if watermark else None
        window_from = start or (datetime.now(tz=timezone.utc) - timedelta(days=WINDOW_DAYS * 6))
        now = datetime.now(tz=timezone.utc)
        seen: set[str] = set()  # windows share boundary DATES — dedupe by uuid

        for _ in range(MAX_WINDOWS):
            if window_from >= now:
                break
            window_to = min(window_from + timedelta(days=WINDOW_DAYS), now)
            for meeting in self._recordings(window_from, window_to):
                muid = str(meeting.get("uuid") or meeting.get("id") or "")
                if muid in seen:
                    continue
                seen.add(muid)
                started_iso = meeting.get("start_time", "")
                if watermark and started_iso and started_iso <= watermark:
                    continue
                doc = self._meeting_to_doc(meeting)
                if doc is None:
                    continue
                yield doc
                if started_iso and (newest is None or started_iso > newest):
                    newest = started_iso
            window_from = window_to

        if cp and newest:
            self._pending_watermark = newest

    def commit_checkpoint(self) -> None:
        if self.checkpoint_db and self._pending_watermark:
            CheckpointStore(self.checkpoint_db).set(
                self.name, self._pending_watermark, key=self.checkpoint_key
            )
            self._pending_watermark = None

    def _meeting_to_doc(self, meeting: dict) -> RawDoc | None:
        files = [f for f in meeting.get("recording_files", []) if isinstance(f, dict)]
        transcript = next((f for f in files if f.get("file_type") == "TRANSCRIPT"), None)
        chat = next((f for f in files if f.get("file_type") == "CHAT"), None)
        body = ""
        kind = ""
        for candidate, label in ((transcript, "transcript"), (chat, "chat")):
            if candidate and candidate.get("download_url"):
                try:
                    raw = self._download(candidate["download_url"])
                except Exception:
                    continue
                body = vtt_to_text(raw) if label == "transcript" else raw
                kind = label
                break
        if not body.strip():
            return None
        body = body[:MAX_TRANSCRIPT_CHARS]

        topic = str(meeting.get("topic") or "Zoom meeting")
        started_iso = str(meeting.get("start_time") or "")
        started = _parse_ts(started_iso) or datetime.now(tz=timezone.utc)
        text = (f"# {topic}\n\n**Date:** {started_iso} · "
                f"**Duration:** {meeting.get('duration', '?')} min\n\n"
                f"## {'Transcript' if kind == 'transcript' else 'In-meeting chat'}\n\n{body}")
        return RawDoc(
            text=text,
            source=self.name,
            source_id=str(meeting.get("uuid") or meeting.get("id") or started_iso),
            url=str(meeting.get("share_url") or ""),
            created_at=started,
            meta={"topic": topic, "kind": kind,
                   "duration_min": meeting.get("duration")},
        )

    # -- HTTP -----------------------------------------------------------------

    def _mint_token(self) -> str:
        basic = base64.b64encode(
            f"{self.client_id}:{self.client_secret}".encode()).decode()
        req = urllib.request.Request(
            f"{TOKEN_URL}?grant_type=account_credentials&account_id="
            f"{urllib.parse.quote(self.account_id)}",
            method="POST",
            headers={"Authorization": f"Basic {basic}"},
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:  # noqa: S310 — fixed https host
            payload = json.loads(resp.read().decode("utf-8"))
        token = payload.get("access_token")
        if not token:
            raise ZoomAuthError(f"Zoom token mint failed: {payload}")
        return str(token)

    def _recordings(self, dt_from: datetime, dt_to: datetime) -> Iterable[dict]:
        token: str = ""
        seen_tokens: set[str] = set()
        while True:
            params = {
                "from": dt_from.strftime("%Y-%m-%d"),
                "to": dt_to.strftime("%Y-%m-%d"),
                "page_size": "30",
            }
            if token:
                params["next_page_token"] = token
            data = self._get(f"/users/{urllib.parse.quote(self.user)}/recordings", params)
            for m in data.get("meetings", []):
                if isinstance(m, dict):
                    yield m
            token = str(data.get("next_page_token") or "")
            if not token or token in seen_tokens:
                return
            seen_tokens.add(token)

    def _get(self, path: str, params: dict[str, str]) -> dict:
        qs = urllib.parse.urlencode(params)
        req = urllib.request.Request(
            f"{API}{path}?{qs}",
            headers={"Authorization": f"Bearer {self._token}"},
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:  # noqa: S310 — fixed https host
            return json.loads(resp.read().decode("utf-8"))

    def _download(self, url: str) -> str:
        req = urllib.request.Request(
            url, headers={"Authorization": f"Bearer {self._token}"})
        with urllib.request.urlopen(req, timeout=TIMEOUT * 2) as resp:  # noqa: S310 — zoom-issued download url
            return resp.read().decode("utf-8", errors="replace")
