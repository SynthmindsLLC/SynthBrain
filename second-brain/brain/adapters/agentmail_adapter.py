"""AgentMail adapter — the forward-an-email intake channel.

Wes forwards any email to the dedicated intake inbox
(synthbrain@agentmail.to, created 2026-07-03) and this adapter polls it via
the AgentMail REST API. One RawDoc per message, rendered like a saved .eml.

Auth: AGENTMAIL_API_KEY (one-time setup — grab it from the AgentMail console
and export it in the watch daemon's environment). Field names are handled
defensively (snake_case REST / camelCase variants) the same way the Fieldy
adapter treats its API.

Watermark: newest message timestamp, deferred via commit_checkpoint() (the
CLI commits only after a clean zero-error run) and namespaced per inbox so
two intake inboxes never share one.
"""

from __future__ import annotations

import hashlib
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter
from .inbox_adapter import html_to_text, render_email

ADAPTER_NAME = "agentmail"
API_BASE = "https://api.agentmail.to/v0"
DEFAULT_INBOX = "synthbrain@agentmail.to"
PAGE_LIMIT = 50
MAX_PAGES = 40  # backstop against cursor loops
TIMEOUT = 30


def _pick(d: dict, *keys: str, default: Any = "") -> Any:
    for k in keys:
        if k in d and d[k] is not None:
            return d[k]
    return default


def _parse_ts(value: Any) -> datetime | None:
    if isinstance(value, (int, float)):
        try:
            return datetime.fromtimestamp(float(value), tz=timezone.utc)
        except (ValueError, OSError):
            return None
    if isinstance(value, str) and value:
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            return None
    return None


class AgentMailAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source: str = "",
        *,
        checkpoint_db: str | None = None,
        since: str | None = None,
    ) -> None:
        self.inbox_id = source or DEFAULT_INBOX
        api_key = os.environ.get("AGENTMAIL_API_KEY", "")
        if not api_key:
            raise RuntimeError(
                "AGENTMAIL_API_KEY is not set. Create an API key in the "
                "AgentMail console and export it for the watch daemon."
            )
        self._api_key = api_key
        self.checkpoint_db = checkpoint_db
        self.since = since
        inbox_hash = hashlib.sha1(self.inbox_id.encode("utf-8")).hexdigest()[:12]
        self.checkpoint_key = f"last_sync:{inbox_hash}"
        self._pending_watermark: str | None = None

    # -- intake -------------------------------------------------------------

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (cp.get(self.name, self.checkpoint_key) if cp else None)
        newest: str | None = None

        for msg in self._iter_messages():
            message_id = str(_pick(msg, "message_id", "messageId", "id"))
            if not message_id:
                continue
            ts = _parse_ts(_pick(msg, "timestamp", "created_at", "createdAt", default=None))
            ts_iso = ts.astimezone(timezone.utc).isoformat() if ts else ""
            if watermark and ts_iso and ts_iso <= watermark:
                continue

            full = self._get_message(message_id) or msg
            body = str(_pick(full, "text", "plain", default="")).strip()
            if not body:
                html = str(_pick(full, "html", default=""))
                body = html_to_text(html) if html else ""
            subject = str(_pick(full, "subject"))
            sender = str(_pick(full, "from", "from_", "sender"))
            to = ", ".join(full["to"]) if isinstance(full.get("to"), list) else str(_pick(full, "to"))
            if not body and not subject:
                continue

            yield RawDoc(
                text=render_email(subject, sender, to, ts_iso, body),
                source=self.name,
                source_id=message_id,
                url="",
                created_at=ts or datetime.now(tz=timezone.utc),
                meta={"inbox": self.inbox_id, "subject": subject, "from": sender,
                       "thread_id": str(_pick(full, "thread_id", "threadId"))},
            )
            if ts_iso and (newest is None or ts_iso > newest):
                newest = ts_iso

        if cp and newest:
            self._pending_watermark = newest

    def commit_checkpoint(self) -> None:
        if self.checkpoint_db and self._pending_watermark:
            CheckpointStore(self.checkpoint_db).set(
                self.name, self._pending_watermark, key=self.checkpoint_key
            )
            self._pending_watermark = None

    # -- HTTP ---------------------------------------------------------------

    def _iter_messages(self) -> Iterable[dict]:
        token: str | None = None
        seen_tokens: set[str] = set()
        for _ in range(MAX_PAGES):
            params: dict[str, str] = {"limit": str(PAGE_LIMIT)}
            if token:
                params["page_token"] = token
            data = self._get(f"/inboxes/{urllib.parse.quote(self.inbox_id)}/messages", params)
            for item in data.get("messages") or []:
                if isinstance(item, dict):
                    yield item
            token = _pick(data, "next_page_token", "nextPageToken", "page_token", default=None)
            if not token or token in seen_tokens:
                return
            seen_tokens.add(token)

    def _get_message(self, message_id: str) -> dict | None:
        try:
            return self._get(
                f"/inboxes/{urllib.parse.quote(self.inbox_id)}/messages/"
                f"{urllib.parse.quote(message_id)}", {})
        except Exception:
            return None  # fall back to the list-item fields

    def _get(self, path: str, params: dict[str, str]) -> dict:
        qs = f"?{urllib.parse.urlencode(params)}" if params else ""
        req = urllib.request.Request(
            f"{API_BASE}{path}{qs}",
            headers={"Authorization": f"Bearer {self._api_key}",
                     "Accept": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:  # noqa: S310 — fixed https host
            return json.loads(resp.read().decode("utf-8"))
