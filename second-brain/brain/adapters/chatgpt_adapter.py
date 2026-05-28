"""ChatGPT export adapter — conversations.json -> RawDocs.

Export from chatgpt.com → Settings → Data Controls → Export Data. You get a
zip with `conversations.json` at its root. Point --source at the unzipped
`conversations.json` file (or the dir containing it).

Each conversation becomes ONE RawDoc with the messages rendered as a
speakered transcript. Idempotent on the conversation id.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "chatgpt"


class ChatGPTAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(self, source: str) -> None:
        path = Path(source).expanduser()
        if path.is_dir():
            path = path / "conversations.json"
        if not path.exists():
            raise FileNotFoundError(
                f"ChatGPT export not found at {path}. Export from chatgpt.com -> "
                "Settings -> Data Controls -> Export Data, unzip, and point --source "
                "at the unzipped folder or conversations.json."
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
    convo_id = convo.get("id") or convo.get("conversation_id") or convo.get("uuid")
    if not convo_id:
        return None
    title = convo.get("title") or "Untitled ChatGPT conversation"
    mapping = convo.get("mapping") or {}
    messages = _flatten_mapping(mapping)
    if not messages:
        return None

    body_lines = [f"# {title}", ""]
    for role, text in messages:
        body_lines.append(f"**{role}:** {text}")
        body_lines.append("")

    created_ts = convo.get("create_time") or convo.get("created_at")
    created_dt = _epoch_or_iso(created_ts) or datetime.now(timezone.utc)

    return RawDoc(
        text="\n".join(body_lines).strip(),
        source=ADAPTER_NAME,
        source_id=str(convo_id),
        url=f"https://chatgpt.com/c/{convo_id}",
        created_at=created_dt,
        meta={"title": title, "message_count": len(messages)},
    )


def _flatten_mapping(mapping: dict) -> list[tuple[str, str]]:
    """ChatGPT's export is a tree: each node points at parent + children. We
    walk in chronological order using create_time so reply branches don't
    interleave."""
    nodes = []
    for node_id, node in mapping.items():
        msg = node.get("message") if isinstance(node, dict) else None
        if not msg:
            continue
        author = (msg.get("author") or {}).get("role") or "unknown"
        if author == "system":
            continue
        content = msg.get("content") or {}
        parts = content.get("parts") or []
        text_parts: list[str] = []
        for p in parts:
            if isinstance(p, str):
                text_parts.append(p)
            elif isinstance(p, dict) and isinstance(p.get("text"), str):
                text_parts.append(p["text"])
        text = "\n".join(t for t in text_parts if t).strip()
        if not text:
            continue
        ts = msg.get("create_time") or 0
        nodes.append((ts, author, text))
    nodes.sort(key=lambda x: x[0])
    return [(role, text) for _ts, role, text in nodes]


def _epoch_or_iso(v: Any) -> datetime | None:
    if v is None:
        return None
    try:
        if isinstance(v, (int, float)):
            return datetime.fromtimestamp(float(v), tz=timezone.utc)
        if isinstance(v, str):
            return datetime.fromisoformat(v.replace("Z", "+00:00"))
    except (ValueError, OSError):
        return None
    return None
