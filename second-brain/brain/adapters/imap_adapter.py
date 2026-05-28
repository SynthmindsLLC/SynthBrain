"""IMAP adapter — works for iCloud Mail, Fastmail, generic IMAP servers.

iCloud Mail has no public REST API. The supported path is IMAP with an
**app-specific password** (Apple ID -> Sign-In and Security -> App-Specific
Passwords). Server: imap.mail.me.com:993 (TLS).

Same triage as the Gmail adapter — every fetched message goes through
`email_filter.classify_email` so marketing/newsletters never reach the
brain. KEPT messages become RawDocs.

Incremental sync uses UIDVALIDITY + UIDNEXT per folder, stored in the
checkpoint store. If UIDVALIDITY changes on the server (folder rebuilt),
we drop the checkpoint and re-walk.

Env vars (defaults shown for iCloud):
  IMAP_HOST       imap.mail.me.com
  IMAP_PORT       993
  IMAP_USERNAME   your Apple ID email
  IMAP_PASSWORD   app-specific password (NEVER your real password)
  IMAP_FOLDER     INBOX
  IMAP_OWN_DOMAINS comma-separated, e.g. "synthminds.ai,me.com"
"""

from __future__ import annotations

import email
import imaplib
import os
import re
from datetime import datetime, timezone
from email.message import Message
from email.utils import getaddresses, parseaddr, parsedate_to_datetime
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
from .gmail_adapter import _html_to_text, _strip_quoted_and_sig

ADAPTER_NAME = "imap"
ICLOUD_HOST = "imap.mail.me.com"
ICLOUD_PORT = 993


class IMAPAdapter(Adapter):
    """Pulls mail over IMAP, filters, emits RawDocs.

    Works against any IMAP server but tuned for iCloud Mail by default."""

    name = ADAPTER_NAME

    def __init__(
        self,
        *,
        host: str | None = None,
        port: int | None = None,
        username: str | None = None,
        password: str | None = None,
        folder: str = "INBOX",
        checkpoint_db: str | None = None,
        entdb: str | None = None,
        own_domains: Iterable[str] | None = None,
        max_messages: int | None = None,
        llm_tiebreaker: bool = True,
    ) -> None:
        self.host = host or os.environ.get("IMAP_HOST", ICLOUD_HOST)
        self.port = int(port or os.environ.get("IMAP_PORT", ICLOUD_PORT))
        self.username = username or os.environ.get("IMAP_USERNAME")
        self.password = password or os.environ.get("IMAP_PASSWORD")
        if not self.username or not self.password:
            raise RuntimeError(
                "IMAP_USERNAME + IMAP_PASSWORD must be set (use an "
                "app-specific password for iCloud)."
            )
        self.folder = folder or os.environ.get("IMAP_FOLDER", "INBOX")
        self.checkpoint_db = checkpoint_db
        self.entdb = entdb
        env_domains = os.environ.get("IMAP_OWN_DOMAINS", "")
        self.own_domains = list(own_domains or [d.strip() for d in env_domains.split(",") if d.strip()])
        self.max_messages = max_messages
        self.llm_tiebreaker = llm_tiebreaker

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        allow = (
            build_allowlist_from_store(EntityStore(self.entdb))
            if self.entdb else set()
        )

        conn = imaplib.IMAP4_SSL(self.host, self.port)
        try:
            conn.login(self.username, self.password)
            typ, _ = conn.select(self.folder, readonly=True)
            if typ != "OK":
                raise RuntimeError(f"IMAP SELECT {self.folder} failed: {typ}")

            uidvalidity = _get_uidvalidity(conn)
            ckey = f"uid::{self.folder}"
            saved = (cp.get(self.name, key=ckey) or "") if cp else ""
            prev_validity, prev_uid = _parse_checkpoint(saved)

            since_uid = (prev_uid + 1) if (prev_validity == uidvalidity and prev_uid) else 1
            search_arg = f"UID {since_uid}:*"
            typ, data = conn.uid("SEARCH", None, search_arg)
            if typ != "OK":
                raise RuntimeError(f"IMAP UID SEARCH failed: {typ}")

            uids = [u for u in (data[0] or b"").split() if u]
            kept = 0
            last_uid = prev_uid

            for raw_uid in uids:
                try:
                    uid_int = int(raw_uid)
                except ValueError:
                    continue
                if uid_int < since_uid:
                    continue
                typ, fetched = conn.uid("FETCH", raw_uid, "(BODY.PEEK[])")
                if typ != "OK" or not fetched or fetched[0] is None:
                    continue
                raw_bytes = fetched[0][1] if isinstance(fetched[0], tuple) else b""
                if not raw_bytes:
                    continue
                msg = email.message_from_bytes(raw_bytes)
                meta, doc = _email_to_meta_and_doc(msg, uid_int, self.folder)
                last_uid = uid_int
                if meta is None or doc is None:
                    continue
                v = classify_email(meta, allowlist=allow,
                                   own_domains=self.own_domains,
                                   llm_tiebreaker=self.llm_tiebreaker)
                if v.decision is Decision.DROP:
                    continue
                kept += 1
                yield doc
                if self.max_messages and kept >= self.max_messages:
                    break

            if cp:
                cp.set(self.name, f"{uidvalidity}:{last_uid}", key=ckey)
        finally:
            try:
                conn.logout()
            except Exception:
                pass


def _get_uidvalidity(conn: imaplib.IMAP4_SSL) -> str:
    typ, data = conn.response("UIDVALIDITY")
    if typ == "OK" and data:
        for d in data:
            if isinstance(d, bytes):
                return d.decode("ascii", errors="replace")
            if isinstance(d, str):
                return d
    # Fallback: STATUS-based lookup
    typ, status = conn.status(conn.state and "INBOX" or "INBOX", "(UIDVALIDITY)")
    if typ == "OK" and status:
        m = re.search(r"UIDVALIDITY\s+(\d+)", status[0].decode("ascii", errors="replace"))
        if m:
            return m.group(1)
    return ""


def _parse_checkpoint(saved: str) -> tuple[str, int]:
    if not saved or ":" not in saved:
        return "", 0
    validity, _, uid = saved.partition(":")
    try:
        return validity, int(uid)
    except ValueError:
        return validity, 0


def _email_to_meta_and_doc(msg: Message, uid: int, folder: str) -> tuple[EmailMeta | None, RawDoc | None]:
    from_raw = msg.get("From", "")
    from_name, from_addr = parseaddr(from_raw)
    to_addrs = [a for _, a in getaddresses([msg.get("To", "")]) if a]
    cc_addrs = [a for _, a in getaddresses([msg.get("Cc", "")]) if a]
    subject = msg.get("Subject", "") or ""

    headers = {k.lower(): v for k, v in msg.items()}

    body_text = _walk_imap_parts(msg)
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

    msg_id = msg.get("Message-ID", "") or f"imap-{folder}-{uid}"
    try:
        created = parsedate_to_datetime(msg.get("Date", "")) or datetime.now(timezone.utc)
        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)
        created = created.astimezone(timezone.utc)
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
        source_id=str(msg_id).strip("<>"),
        url="",
        created_at=created,
        meta={
            "from": from_addr,
            "to": to_addrs,
            "subject": subject,
            "folder": folder,
            "uid": uid,
        },
    )
    return meta, doc


def _walk_imap_parts(msg: Message) -> str:
    plain = ""
    html = ""
    for part in msg.walk() if msg.is_multipart() else [msg]:
        ctype = part.get_content_type()
        if ctype not in ("text/plain", "text/html"):
            continue
        try:
            payload = part.get_payload(decode=True) or b""
            charset = part.get_content_charset() or "utf-8"
            text = payload.decode(charset, errors="replace")
        except Exception:
            text = ""
        if not text:
            continue
        if ctype == "text/plain" and not plain:
            plain = text
        elif ctype == "text/html" and not html:
            html = _html_to_text(text)
    return plain or html or ""
