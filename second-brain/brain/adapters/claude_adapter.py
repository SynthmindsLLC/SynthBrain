"""Claude.ai export adapter — conversations.json -> RawDocs.

Export from claude.ai → Settings → Data Privacy → Export your data. You
get a zip containing `conversations.json` (and optionally `projects.json`).
Point --source at the unzipped folder or at the conversations.json file.

Shape differs from ChatGPT:
  [
    {
      "uuid": "...",
      "name": "Conversation title",
      "created_at": "2026-05-28T...Z",
      "chat_messages": [
        {"sender": "human", "text": "...", "created_at": "..."},
        {"sender": "assistant", "text": "...", "created_at": "..."},
        ...
      ]
    }
  ]
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "claude"


class ClaudeAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(self, source: str) -> None:
        path = Path(source).expanduser()
        if path.is_dir():
            for cand in ("conversations.json", "conversations.json.json"):
                if (path / cand).exists():
                    path = path / cand
                    break
            else:
                raise FileNotFoundError(
                    f"conversations.json not found in {path}. Did you unzip "
                    "the Claude export here?"
                )
        if not path.exists():
            raise FileNotFoundError(
                f"Claude export not found at {path}. Export from claude.ai -> "
                "Settings -> Data Privacy -> Export your data, unzip, and point "
                "--source at the unzipped folder."
            )
        self.source_path = path

    def fetch(self) -> Iterable[RawDoc]:
        data = json.loads(self.source_path.read_text(encoding="utf-8", errors="replace"))
        if not isinstance(data, list):
            return
        for convo in data:
            doc = _convo_to_doc(convo)
            if doc is not None:
                yield doc


def _convo_to_doc(convo: dict) -> RawDoc | None:
    convo_id = convo.get("uuid") or convo.get("id")
    if not convo_id:
        return None
    title = convo.get("name") or "Untitled Claude conversation"
    messages = convo.get("chat_messages") or []
    if not isinstance(messages, list) or not messages:
        return None

    body_lines = [f"# {title}", ""]
    rendered = 0
    for msg in messages:
        sender = msg.get("sender") or "unknown"
        text = _extract_text(msg)
        if not text:
            continue
        body_lines.append(f"**{sender}:** {text}")
        body_lines.append("")
        rendered += 1
    if rendered == 0:
        return None

    created = _parse_ts(convo.get("created_at")) or datetime.now(timezone.utc)
    return RawDoc(
        text="\n".join(body_lines).strip(),
        source=ADAPTER_NAME,
        source_id=str(convo_id),
        url=f"https://claude.ai/chat/{convo_id}",
        created_at=created,
        meta={"title": title, "message_count": rendered},
    )


def _extract_text(msg: dict) -> str:
    direct = msg.get("text")
    if isinstance(direct, str) and direct.strip():
        return direct.strip()
    content = msg.get("content")
    if isinstance(content, list):
        parts = []
        for c in content:
            if isinstance(c, dict) and isinstance(c.get("text"), str):
                parts.append(c["text"])
        return "\n".join(p for p in parts if p).strip()
    if isinstance(content, str):
        return content.strip()
    return ""


def _parse_ts(v: Any) -> datetime | None:
    if not v:
        return None
    if isinstance(v, (int, float)):
        try:
            return datetime.fromtimestamp(float(v), tz=timezone.utc)
        except (ValueError, OSError):
            return None
    if isinstance(v, str):
        try:
            return datetime.fromisoformat(v.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None
