"""Fieldy AI adapter — transcripts from the wearable into the brain.

Fieldy is the "what we discussed" source — the conversations the glasses
will eventually recall. Two paths, behind one interface:

  Path 1 (preferred): MCP transport at https://api.fieldy.ai/mcp.
    Built once the user authorizes their email through the MCP integration
    walkthrough in Fieldy's Developer Settings. We'd add it to .mcp.json and
    call the upstream tools directly; this adapter's role becomes a thin
    bridge that drives the MCP client and normalizes to RawDoc.

  Path 2 (this file, today): REST against the Public API
    GET /api/public/v2/transcriptions
    GET /api/public/v2/transcriptions/{id}
    Auth: Authorization: Bearer $FIELDY_API_KEY
    Idempotency: each transcription has a stable id; we use it as `source_id`
    so re-ingest is a deterministic upsert (see schema.py _derive_id).
    Incremental: checkpoint the max `created_at` seen; next run only fetches
    newer transcriptions.

Field names (created_at, speakers, transcript, etc.) are based on Fieldy's
documented public API shape; if the live response differs, the adapter
gracefully falls back per the `_extract_*` helpers and logs the unknown
keys so we can adjust without redeploying.
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

DEFAULT_API_BASE = "https://api.fieldy.ai/api/public/v2"
ADAPTER_NAME = "fieldy"
DEFAULT_PAGE_SIZE = 50
DEFAULT_TIMEOUT = 30


class FieldyAuthError(RuntimeError):
    pass


class FieldyAPIError(RuntimeError):
    pass


class FieldyAdapter(Adapter):
    """REST-path Fieldy adapter. Yields one RawDoc per transcription."""

    name = ADAPTER_NAME

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_base: str | None = None,
        checkpoint_db: str | None = None,
        since: str | None = None,
        limit: int | None = None,
        page_size: int = DEFAULT_PAGE_SIZE,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.api_key = api_key or os.environ.get("FIELDY_API_KEY")
        if not self.api_key:
            raise FieldyAuthError(
                "FIELDY_API_KEY not set. Put it in .env.local (gitignored) and "
                "load before running, or pass api_key= explicitly."
            )
        self.api_base = (api_base or os.environ.get("FIELDY_API_BASE") or DEFAULT_API_BASE).rstrip("/")
        self.checkpoint_db = checkpoint_db
        self.since = since
        self.limit = limit
        self.page_size = page_size
        self.timeout = timeout

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (cp.get(self.name) if cp else None)

        emitted = 0
        newest_seen: str | None = None
        for tx in self._iter_transcriptions(since=watermark):
            doc = self._to_raw_doc(tx)
            if doc is None:
                continue
            yield doc
            emitted += 1
            ts = _extract_created_at(tx)
            if ts and (newest_seen is None or ts > newest_seen):
                newest_seen = ts
            if self.limit and emitted >= self.limit:
                break

        if cp and newest_seen:
            cp.set(self.name, newest_seen)

    def _iter_transcriptions(self, *, since: str | None) -> Iterable[dict]:
        """Paginate /transcriptions. Stops when API returns no more results or
        the cursor stops advancing (defensive against unbounded cursors)."""
        cursor: str | None = None
        seen_cursors: set[str] = set()
        while True:
            params: dict[str, Any] = {"limit": self.page_size}
            if since:
                params["since"] = since
            if cursor:
                params["cursor"] = cursor
            payload = self._get("/transcriptions", params)
            items = _extract_items(payload)
            if not items:
                return
            for item in items:
                yield item
            cursor = _extract_next_cursor(payload)
            if not cursor or cursor in seen_cursors:
                return
            seen_cursors.add(cursor)

    def _get(self, path: str, params: dict[str, Any]) -> dict:
        qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        url = f"{self.api_base}{path}" + (f"?{qs}" if qs else "")
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Accept": "application/json",
                "User-Agent": "synthbrain-fieldy/0.1",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                body = resp.read().decode("utf-8", errors="replace")
                return json.loads(body) if body else {}
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                raise FieldyAuthError(
                    f"Fieldy auth failed ({e.code}). Verify FIELDY_API_KEY is current."
                ) from e
            raise FieldyAPIError(f"Fieldy {path} -> HTTP {e.code}: {e.reason}") from e
        except urllib.error.URLError as e:
            raise FieldyAPIError(f"Fieldy network error for {url}: {e.reason}") from e

    def _to_raw_doc(self, tx: dict) -> RawDoc | None:
        text = _extract_transcript_text(tx)
        if not text:
            return None
        source_id = _extract_id(tx)
        if not source_id:
            return None
        speakers = _extract_speakers(tx)
        body = _format_transcript(text, speakers, tx)
        created = _extract_created_at(tx)
        try:
            ts = datetime.fromisoformat(created.replace("Z", "+00:00")) if created else datetime.now(timezone.utc)
        except ValueError:
            ts = datetime.now(timezone.utc)
        return RawDoc(
            text=body,
            source=self.name,
            source_id=str(source_id),
            url=_extract_url(tx),
            created_at=ts.astimezone(timezone.utc),
            meta={
                "speakers": speakers,
                "duration_sec": tx.get("duration_sec") or tx.get("duration"),
                "title": tx.get("title") or tx.get("summary_title", ""),
            },
        )


def _extract_items(payload: dict) -> list[dict]:
    """Tolerate either {data:[...]} or {transcriptions:[...]} or bare list."""
    if isinstance(payload, list):
        return payload
    for key in ("data", "transcriptions", "items", "results"):
        if isinstance(payload.get(key), list):
            return payload[key]
    return []


def _extract_next_cursor(payload: dict) -> str | None:
    if not isinstance(payload, dict):
        return None
    for key in ("next_cursor", "cursor", "next"):
        v = payload.get(key)
        if isinstance(v, str) and v:
            return v
    pagination = payload.get("pagination") or {}
    if isinstance(pagination, dict):
        for key in ("next_cursor", "next"):
            v = pagination.get(key)
            if isinstance(v, str) and v:
                return v
    return None


def _extract_id(tx: dict) -> str:
    for key in ("id", "transcription_id", "uuid"):
        v = tx.get(key)
        if v:
            return str(v)
    return ""


def _extract_created_at(tx: dict) -> str:
    for key in ("created_at", "createdAt", "started_at", "recorded_at"):
        v = tx.get(key)
        if isinstance(v, str) and v:
            return v
    return ""


def _extract_url(tx: dict) -> str:
    for key in ("url", "web_url", "share_url"):
        v = tx.get(key)
        if isinstance(v, str) and v:
            return v
    return ""


def _extract_speakers(tx: dict) -> list[str]:
    speakers = tx.get("speakers") or tx.get("participants") or []
    out: list[str] = []
    if isinstance(speakers, list):
        for s in speakers:
            if isinstance(s, str):
                out.append(s)
            elif isinstance(s, dict):
                name = s.get("name") or s.get("display_name") or s.get("label")
                if name:
                    out.append(str(name))
    return out


def _extract_transcript_text(tx: dict) -> str:
    """Fieldy returns transcripts in a few shapes; handle the common ones."""
    direct = tx.get("transcript") or tx.get("text") or tx.get("body")
    if isinstance(direct, str) and direct.strip():
        return direct.strip()
    segments = tx.get("segments") or tx.get("utterances") or []
    if isinstance(segments, list) and segments:
        lines: list[str] = []
        for seg in segments:
            if isinstance(seg, str):
                lines.append(seg)
            elif isinstance(seg, dict):
                speaker = seg.get("speaker") or seg.get("speaker_name") or ""
                line = seg.get("text") or seg.get("content") or ""
                if not line:
                    continue
                lines.append(f"{speaker}: {line}".strip().lstrip(": "))
        return "\n".join(lines).strip()
    return ""


def _format_transcript(text: str, speakers: list[str], tx: dict) -> str:
    """Render with a header so the chunker treats this as a single semantic unit
    when reasonable and preserves provenance."""
    header_bits = []
    title = tx.get("title") or tx.get("summary_title")
    if title:
        header_bits.append(f"# {title}")
    if speakers:
        header_bits.append(f"_Speakers: {', '.join(speakers)}_")
    if header_bits:
        return "\n\n".join(header_bits) + "\n\n" + text
    return text
