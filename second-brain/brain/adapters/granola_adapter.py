"""Granola adapter — meeting transcripts -> chunks.

Granola hasn't published a public REST API at the time of writing, but it
exposes two paths the brain can ingest from today:

  1. JSON export (preferred): Granola lets you export individual meetings
     as `.json` (see Settings -> Privacy & Data). Each export contains
     `id`, `title`, `created_at`, optional `summary`, and a `transcript`
     array of {speaker, text, ts} segments. Point --source at the file or
     the folder of exports.

  2. Folder of markdown summaries: Granola also writes a markdown summary
     per meeting if you have local-sync on. Each .md file's name is the
     stable id. This is treated the same way the filesystem adapter
     handles markdown — included here so meetings stream through a single
     `--adapter granola` invocation regardless of export shape.

Idempotent on meeting id. Checkpoints the newest `created_at` seen.

When Granola ships an official API, swap the body of `_iter_files` for a
live HTTP path; the transform stays put.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "granola"
SUPPORTED_EXTS = (".json", ".md", ".markdown", ".txt")


class GranolaAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source: str,
        *,
        checkpoint_db: str | None = None,
        since: str | None = None,
    ) -> None:
        p = Path(source).expanduser()
        if not p.exists():
            raise FileNotFoundError(
                f"Granola source not found: {p}. Export meetings from Granola "
                "(Settings -> Privacy & Data) and point --source at the .json "
                "file or the folder of exports."
            )
        self.source = p
        self.checkpoint_db = checkpoint_db
        self.since = since

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (cp.get(self.name) if cp else None)
        newest: str | None = None
        for path in self._iter_files():
            payload = _load_payload(path)
            if not payload:
                continue
            doc = self._payload_to_doc(payload, path)
            if doc is None:
                continue
            created_iso = doc.created_at.astimezone(timezone.utc).isoformat()
            if watermark and created_iso <= watermark:
                continue
            yield doc
            if newest is None or created_iso > newest:
                newest = created_iso
        if cp and newest:
            cp.set(self.name, newest)

    def _iter_files(self) -> Iterable[Path]:
        if self.source.is_file():
            yield self.source
            return
        for path in sorted(self.source.rglob("*")):
            if path.is_file() and path.suffix.lower() in SUPPORTED_EXTS:
                yield path

    def _payload_to_doc(self, payload: dict | str, path: Path) -> RawDoc | None:
        if isinstance(payload, str):
            return _markdown_to_doc(payload, path)
        return _json_to_doc(payload, path)


def _load_payload(path: Path) -> dict | str | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    if path.suffix.lower() == ".json":
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return None
    return text


def _json_to_doc(p: dict, path: Path) -> RawDoc | None:
    meeting_id = (
        p.get("id") or p.get("meeting_id") or p.get("uuid") or path.stem
    )
    title = (p.get("title") or p.get("name") or "Granola meeting").strip()
    created = p.get("created_at") or p.get("start_time") or ""
    ts = _parse_ts(created) or datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)

    summary = (p.get("summary") or p.get("ai_summary") or "").strip()
    transcript = _render_transcript(p.get("transcript") or p.get("segments") or [])
    if not summary and not transcript:
        return None

    body_lines = [f"# {title}"]
    if summary:
        body_lines.append("\n## Summary\n")
        body_lines.append(summary)
    if transcript:
        body_lines.append("\n## Transcript\n")
        body_lines.append(transcript)

    attendees = p.get("attendees") or p.get("participants") or []
    attendee_names = _attendee_names(attendees)

    return RawDoc(
        text="\n".join(body_lines).strip(),
        source=ADAPTER_NAME,
        source_id=str(meeting_id),
        url=p.get("url") or p.get("share_url") or "",
        created_at=ts,
        meta={
            "title": title,
            "attendees": attendee_names,
            "has_summary": bool(summary),
            "has_transcript": bool(transcript),
        },
    )


def _markdown_to_doc(text: str, path: Path) -> RawDoc | None:
    text = text.strip()
    if not text:
        return None
    ts = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return RawDoc(
        text=text,
        source=ADAPTER_NAME,
        source_id=path.stem,
        url="",
        created_at=ts,
        meta={"path": str(path), "format": "markdown"},
    )


def _render_transcript(segments: list) -> str:
    if not isinstance(segments, list):
        return ""
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


def _attendee_names(attendees: list) -> list[str]:
    out: list[str] = []
    for a in attendees or []:
        if isinstance(a, str):
            out.append(a)
        elif isinstance(a, dict):
            name = a.get("name") or a.get("display_name") or a.get("email")
            if name:
                out.append(str(name))
    return out


def _parse_ts(value: Any) -> datetime | None:
    if not value:
        return None
    if isinstance(value, (int, float)):
        try:
            return datetime.fromtimestamp(float(value), tz=timezone.utc)
        except (ValueError, OSError):
            return None
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None
