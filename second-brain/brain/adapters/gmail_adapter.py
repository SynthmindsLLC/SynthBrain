"""Gmail adapter — personal/work mail through the triage filter into the brain.

Uses Gmail API v1 with two paths:
  - First run: messages.list (filtered to in:inbox -category:promotions
    -category:social -category:updates -category:forums) + messages.get.
    Captures the current historyId at the end.
  - Subsequent runs: history.list(startHistoryId) for true incremental sync.
    Falls back to a fresh full crawl if Google invalidates the historyId
    (HTTP 404 or "historyId too old").

Every fetched message goes through `email_filter.classify_email` with the
brain's Person-derived allowlist + owner's domains. KEPT messages become
RawDocs (one per message, header + body). DROPPED messages are silently
skipped; counts go into the checkpoint store for auditability.

Body extraction: prefers text/plain; falls back to text/html with tags
stripped. Quoted reply trailers and signature blocks are trimmed before
chunking so the chunker doesn't fixate on boilerplate.

Required env: GOOGLE_OAUTH_CLIENT_ID, GOOGLE_OAUTH_CLIENT_SECRET,
GOOGLE_OAUTH_REFRESH_TOKEN (with https://www.googleapis.com/auth/gmail.readonly
added to the existing client). Lazy-imports googleapiclient.
"""

from __future__ import annotations

import base64
import os
import re
from datetime import datetime, timezone
from email.utils import getaddresses, parseaddr
from typing import Iterable

from ..core.checkpoint import CheckpointStore
from ..core.email_filter import (
    Decision,
    EmailMeta,
    build_allowlist_from_store,
    classify_email,
)
from ..core.entities import EntityStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "gmail"
DEFAULT_LIST_QUERY = (
    "in:inbox -category:promotions -category:social "
    "-category:updates -category:forums"
)
DEFAULT_PAGE_SIZE = 100
HISTORY_INVALIDATED_CODES = (404, 400)


class GmailAdapter(Adapter):
    """Pulls Gmail messages, filters out marketing/newsletters, emits RawDocs."""

    name = ADAPTER_NAME

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        refresh_token: str | None = None,
        checkpoint_db: str | None = None,
        entdb: str | None = None,
        own_domains: Iterable[str] = ("synthminds.ai",),
        list_query: str = DEFAULT_LIST_QUERY,
        max_messages: int | None = None,
        page_size: int = DEFAULT_PAGE_SIZE,
        llm_tiebreaker: bool = True,
    ) -> None:
        self.client_id = client_id or os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
        self.refresh_token = refresh_token or os.environ.get("GOOGLE_OAUTH_REFRESH_TOKEN")
        if not all([self.client_id, self.client_secret, self.refresh_token]):
            raise RuntimeError(
                "Missing Google OAuth env. Set GOOGLE_OAUTH_CLIENT_ID, "
                "GOOGLE_OAUTH_CLIENT_SECRET, GOOGLE_OAUTH_REFRESH_TOKEN "
                "(add gmail.readonly scope)."
            )
        self.checkpoint_db = checkpoint_db
        self.entdb = entdb
        self.own_domains = list(own_domains)
        self.list_query = list_query
        self.max_messages = max_messages
        self.page_size = page_size
        self.llm_tiebreaker = llm_tiebreaker

    def fetch(self) -> Iterable[RawDoc]:
        from googleapiclient.errors import HttpError  # type: ignore[import-not-found]

        service = _gmail_service(self.client_id, self.client_secret, self.refresh_token)
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        history_id = cp.get(self.name, key="history_id") if cp else None

        allow = (
            build_allowlist_from_store(EntityStore(self.entdb))
            if self.entdb else set()
        )

        kept = dropped = 0
        latest_history: str | None = None

        try:
            if history_id:
                yield_iter = self._iter_via_history(service, history_id)
            else:
                yield_iter = self._iter_via_list(service)

            for msg in yield_iter:
                meta, doc = _message_to_meta_and_doc(msg)
                if meta is None or doc is None:
                    continue
                v = classify_email(meta, allowlist=allow,
                                   own_domains=self.own_domains,
                                   llm_tiebreaker=self.llm_tiebreaker)
                if v.decision is Decision.DROP:
                    dropped += 1
                    continue
                kept += 1
                yield doc
                # Track the most-recent message's historyId so we can resume.
                hid = msg.get("historyId")
                if hid and (latest_history is None or int(hid) > int(latest_history)):
                    latest_history = hid
                if self.max_messages and kept >= self.max_messages:
                    break

        except HttpError as e:
            code = getattr(getattr(e, "resp", None), "status", None)
            if history_id and code in HISTORY_INVALIDATED_CODES:
                if cp:
                    cp.clear(self.name, key="history_id")
                raise RuntimeError(
                    "Gmail historyId invalidated; checkpoint cleared. Re-run."
                ) from e
            raise

        if cp:
            # Always advance: if nothing kept, still capture profile.historyId
            # so next run starts after this point.
            new_hid = latest_history or _profile_history_id(service)
            if new_hid:
                cp.set(self.name, str(new_hid), key="history_id")
            cp.set(self.name, str(kept), key="last_kept")
            cp.set(self.name, str(dropped), key="last_dropped")

    def _iter_via_list(self, service) -> Iterable[dict]:
        page_token: str | None = None
        while True:
            resp = service.users().messages().list(
                userId="me",
                q=self.list_query,
                maxResults=self.page_size,
                pageToken=page_token,
            ).execute()
            for ref in resp.get("messages", []) or []:
                full = service.users().messages().get(
                    userId="me", id=ref["id"], format="full",
                ).execute()
                yield full
            page_token = resp.get("nextPageToken")
            if not page_token:
                return

    def _iter_via_history(self, service, history_id: str) -> Iterable[dict]:
        page_token: str | None = None
        while True:
            resp = service.users().history().list(
                userId="me",
                startHistoryId=history_id,
                historyTypes=["messageAdded"],
                pageToken=page_token,
            ).execute()
            for h in resp.get("history", []) or []:
                for m in h.get("messagesAdded", []) or []:
                    msg_id = (m.get("message") or {}).get("id")
                    if not msg_id:
                        continue
                    try:
                        yield service.users().messages().get(
                            userId="me", id=msg_id, format="full",
                        ).execute()
                    except Exception:
                        continue
            page_token = resp.get("nextPageToken")
            if not page_token:
                return


# ---- message parsing -----------------------------------------------------

def _profile_history_id(service) -> str | None:
    try:
        prof = service.users().getProfile(userId="me").execute()
        return prof.get("historyId")
    except Exception:
        return None


def _message_to_meta_and_doc(msg: dict) -> tuple[EmailMeta | None, RawDoc | None]:
    payload = msg.get("payload") or {}
    headers = _flatten_headers(payload.get("headers", []))
    from_raw = headers.get("from", "")
    from_name, from_addr = parseaddr(from_raw)
    to_addrs = [a for _, a in getaddresses([headers.get("to", "")]) if a]
    cc_addrs = [a for _, a in getaddresses([headers.get("cc", "")]) if a]
    subject = headers.get("subject", "")

    body_text = _extract_body(payload)
    body_clean = _strip_quoted_and_sig(body_text)

    meta = EmailMeta(
        from_addr=from_addr,
        from_name=from_name,
        to_addrs=to_addrs + cc_addrs,
        subject=subject,
        body=body_clean,
        headers=headers,
    )

    if not meta.from_addr or (not body_clean and not subject):
        return meta, None

    msg_id = msg.get("id") or headers.get("message-id", "")
    if not msg_id:
        return meta, None

    ts_ms = msg.get("internalDate")
    try:
        created = (
            datetime.fromtimestamp(int(ts_ms) / 1000.0, tz=timezone.utc)
            if ts_ms else datetime.now(timezone.utc)
        )
    except (TypeError, ValueError):
        created = datetime.now(timezone.utc)

    body_lines = [
        f"# {subject or '(no subject)'}",
        "",
        f"_From:_ {from_name or from_addr} <{from_addr}>",
    ]
    if to_addrs:
        body_lines.append(f"_To:_ {', '.join(to_addrs)}")
    body_lines.append("")
    body_lines.append(body_clean)
    text = "\n".join(body_lines).strip()

    doc = RawDoc(
        text=text,
        source=ADAPTER_NAME,
        source_id=str(msg_id),
        url=f"https://mail.google.com/mail/u/0/#all/{msg_id}",
        created_at=created,
        meta={
            "from": from_addr,
            "to": to_addrs,
            "subject": subject,
            "thread_id": msg.get("threadId", ""),
            "label_ids": msg.get("labelIds", []),
        },
    )
    return meta, doc


def _flatten_headers(headers: list[dict]) -> dict[str, str]:
    return {h.get("name", "").lower(): h.get("value", "") for h in headers}


def _extract_body(payload: dict) -> str:
    """Walk MIME parts; prefer text/plain, fall back to text/html."""
    if not payload:
        return ""
    mime = payload.get("mimeType", "")
    body = (payload.get("body") or {})
    data = body.get("data")

    if mime == "text/plain" and data:
        return _b64url_decode(data)
    if mime == "text/html" and data:
        return _html_to_text(_b64url_decode(data))

    parts = payload.get("parts") or []
    plain = ""
    html = ""
    for part in parts:
        sub = _extract_body(part)
        if not sub:
            continue
        if part.get("mimeType") == "text/plain" and not plain:
            plain = sub
        elif part.get("mimeType") == "text/html" and not html:
            html = sub
        elif not plain and not html:
            plain = sub
    return plain or html or ""


def _b64url_decode(data: str) -> str:
    try:
        return base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
    except Exception:
        return ""


_HTML_TAG_RE = re.compile(r"<[^>]+>")
_HTML_ENTITY_RE = re.compile(r"&(amp|lt|gt|nbsp|quot|#39);")
_HTML_REPL = {"amp": "&", "lt": "<", "gt": ">", "nbsp": " ", "quot": '"', "#39": "'"}


def _html_to_text(html: str) -> str:
    text = _HTML_TAG_RE.sub(" ", html)
    text = _HTML_ENTITY_RE.sub(lambda m: _HTML_REPL.get(m.group(1), m.group(0)), text)
    return re.sub(r"\s+", " ", text).strip()


_QUOTED_RE = re.compile(
    r"(\n\s*On\s.+wrote:\s*\n)|(\n\s*From:.+\nSent:.+\nTo:.+\nSubject:.+\n)",
    re.IGNORECASE,
)
_SIG_RE = re.compile(r"\n-- ?\n.*", re.DOTALL)


def _strip_quoted_and_sig(text: str) -> str:
    if not text:
        return ""
    m = _QUOTED_RE.search(text)
    if m:
        text = text[: m.start()]
    text = _SIG_RE.sub("", text)
    return text.strip()


def _gmail_service(client_id: str, client_secret: str, refresh_token: str):
    from google.oauth2.credentials import Credentials  # type: ignore[import-not-found]
    from googleapiclient.discovery import build  # type: ignore[import-not-found]

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=["https://www.googleapis.com/auth/gmail.readonly"],
    )
    return build("gmail", "v1", credentials=creds, cache_discovery=False)
