"""Microsoft 365 adapter — Outlook mail + Outlook calendar (Graph API).

Two sub-paths behind one CLI surface (`--adapter m365 --source mail` or
`--source calendar`):

  - mail:     /me/messages with `delta` link for incremental sync.
              Every message goes through brain/core/email_filter to keep
              marketing/newsletters out.
  - calendar: /me/calendarView (events expanded for series), keyed on
              event id; emits Event entities + 'attended' edges into the
              entity graph. Returned as RawDocs of kind "entity" because
              the chunk pipeline accepts mixed streams via the adapter
              contract — see ingest_entities for the entity-only path.
              For now this adapter yields chunk-shaped RawDocs (one per
              event description) so it slots in with the other chunk
              adapters cleanly.

Auth: OAuth2 device-code or auth-code-with-PKCE against the Microsoft
identity platform. Required scopes:
  - Mail.Read
  - Calendars.Read
  - User.Read

Set:
  MS_TENANT_ID                  default "common" (works for personal MS accounts)
  MS_CLIENT_ID                  the Azure App Registration's client id
  MS_REFRESH_TOKEN              long-lived refresh token (offline_access scope)

Run the one-time auth dance via Microsoft's OAuth2 endpoints to mint the
refresh token; instructions in docs/setup/m365.md.

Like the Google adapters, msal / msgraph SDK imports are lazy — adapter
won't break the rest of the brain when those packages are absent.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from email.utils import parseaddr
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

ADAPTER_NAME = "m365"
GRAPH = "https://graph.microsoft.com/v1.0"
TOKEN_URL_TMPL = "https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
DEFAULT_TENANT = "common"
DEFAULT_PAGE_SIZE = 50
DEFAULT_SCOPES = ("Mail.Read", "Calendars.Read", "User.Read", "offline_access")


class M365AuthError(RuntimeError):
    pass


class M365APIError(RuntimeError):
    pass


class M365Adapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source: str = "mail",
        *,
        tenant_id: str | None = None,
        client_id: str | None = None,
        refresh_token: str | None = None,
        checkpoint_db: str | None = None,
        entdb: str | None = None,
        own_domains: Iterable[str] = (),
        max_items: int | None = None,
        page_size: int = DEFAULT_PAGE_SIZE,
        llm_tiebreaker: bool = True,
    ) -> None:
        kind = (source or "mail").lower().strip()
        if kind not in ("mail", "calendar", "teams"):
            raise ValueError(
                f"m365 source must be 'mail', 'calendar' or 'teams', got {source!r}"
            )
        self.kind = kind
        self.tenant_id = tenant_id or os.environ.get("MS_TENANT_ID", DEFAULT_TENANT)
        self.client_id = client_id or os.environ.get("MS_CLIENT_ID")
        self.refresh_token = refresh_token or os.environ.get("MS_REFRESH_TOKEN")
        if not all([self.client_id, self.refresh_token]):
            raise M365AuthError(
                "Missing MS_CLIENT_ID / MS_REFRESH_TOKEN. Register an app "
                "at portal.azure.com (Azure AD -> App registrations), mint "
                "a refresh token (see docs/setup/m365.md), and put both in .env.local."
            )
        self.checkpoint_db = checkpoint_db
        self.entdb = entdb
        self.own_domains = list(own_domains) or _own_domains_from_env()
        self.max_items = max_items
        self.page_size = max(1, min(page_size, 100))
        self.llm_tiebreaker = llm_tiebreaker
        self._access_token: str | None = None
        # Teams watermarks are recorded during fetch and committed only via
        # commit_checkpoint() after a clean run — the filesystem/claude-code
        # tail-flush lesson. (mail/calendar keep their pre-existing in-fetch
        # delta-link behavior.)
        self._pending_teams_marks: dict[str, str] = {}

    def fetch(self) -> Iterable[RawDoc]:
        self._access_token = self._mint_access_token()
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None

        if self.kind == "mail":
            allow = (
                build_allowlist_from_store(EntityStore(self.entdb))
                if self.entdb else set()
            )
            yield from self._fetch_mail(cp, allow)
        elif self.kind == "teams":
            yield from self._fetch_teams(cp)
        else:
            yield from self._fetch_calendar(cp)

    def commit_checkpoint(self) -> None:
        if self.checkpoint_db and self._pending_teams_marks:
            cp = CheckpointStore(self.checkpoint_db)
            for key, value in self._pending_teams_marks.items():
                cp.set(self.name, value, key=key)
            self._pending_teams_marks = {}

    # ---- teams --------------------------------------------------------

    def _fetch_teams(self, cp: CheckpointStore | None) -> Iterable[RawDoc]:
        """Teams 1:1 and group chats via Graph /me/chats (+Chat.Read scope).
        One RawDoc per chat per batch of NEW messages; source_id keys on the
        newest message id so incremental runs never collide (the
        imessage/slack group-index lesson). Channel messages need admin
        consent scopes and are out of scope for a personal token."""
        self._pending_teams_marks = {}
        chats: list[dict] = []
        url: str | None = f"{GRAPH}/me/chats"
        params: dict = {"$top": str(self.page_size), "$expand": "members"}
        while url:
            payload = self._get_url(url, params)
            params = {}
            chats.extend(v for v in payload.get("value", []) if isinstance(v, dict))
            url = payload.get("@odata.nextLink")

        emitted = 0
        for chat in chats:
            chat_id = chat.get("id")
            if not chat_id:
                continue
            wm_key = f"teams_chat:{chat_id}"
            watermark = cp.get(self.name, key=wm_key) if cp else None

            msgs: list[dict] = []
            murl: str | None = f"{GRAPH}/me/chats/{chat_id}/messages"
            mparams: dict = {"$top": "50"}
            while murl:
                payload = self._get_url(murl, mparams)
                mparams = {}
                batch = [v for v in payload.get("value", []) if isinstance(v, dict)]
                msgs.extend(batch)
                # Messages page newest-first: stop once a page crosses the
                # watermark instead of walking years of history.
                if watermark and any(
                    (m.get("createdDateTime") or "") <= watermark for m in batch
                ):
                    break
                murl = payload.get("@odata.nextLink")

            fresh = [
                m for m in msgs
                if (m.get("createdDateTime") or "") > (watermark or "")
                and (m.get("messageType") or "message") == "message"
            ]
            if not fresh:
                continue
            fresh.sort(key=lambda m: m.get("createdDateTime") or "")

            lines: list[str] = []
            for m in fresh:
                sender = (((m.get("from") or {}).get("user") or {})
                          .get("displayName")) or "unknown"
                body = m.get("body") or {}
                text = str(body.get("content") or "")
                if (body.get("contentType") or "").lower() == "html":
                    text = _html_to_text(text)
                text = text.strip()
                if text:
                    lines.append(f"**{sender}:** {text}")
            newest = fresh[-1]
            newest_ts = newest.get("createdDateTime") or ""
            if not lines:
                # All-system batch: advance the mark so it isn't refetched.
                if newest_ts:
                    self._pending_teams_marks[wm_key] = newest_ts
                continue

            topic = (chat.get("topic") or ", ".join(
                str(mm.get("displayName") or "")
                for mm in (chat.get("members") or [])[:4]
                if isinstance(mm, dict) and mm.get("displayName")
            ) or chat_id)
            yield RawDoc(
                text=f"# Teams: {topic}\n\n" + "\n\n".join(lines),
                source=self.name,
                source_id=f"teams:{chat_id}:{newest.get('id') or newest_ts}",
                url=str(chat.get("webUrl") or ""),
                created_at=_parse_iso(newest_ts) or datetime.now(tz=timezone.utc),
                meta={"kind": "teams", "chat_id": chat_id, "topic": topic,
                       "messages": len(lines)},
            )
            if newest_ts:
                self._pending_teams_marks[wm_key] = newest_ts
            emitted += 1
            if self.max_items and emitted >= self.max_items:
                return

    # ---- mail ---------------------------------------------------------

    def _fetch_mail(self, cp: CheckpointStore | None, allow: set[str]) -> Iterable[RawDoc]:
        delta_link = cp.get(self.name, key="mail_delta") if cp else None
        emitted = 0

        if delta_link:
            url = delta_link
            params: dict = {}
        else:
            url = f"{GRAPH}/me/mailFolders/Inbox/messages/delta"
            params = {
                "$top": str(self.page_size),
                "$select": ("from,sender,toRecipients,ccRecipients,subject,"
                            "body,receivedDateTime,internetMessageHeaders,id"),
            }

        while True:
            payload = self._get_url(url, params)
            params = {}  # only first call carries the bootstrapping params
            for msg in payload.get("value", []):
                meta, doc = _msg_to_meta_and_doc(msg)
                if meta is None or doc is None:
                    continue
                v = classify_email(meta, allowlist=allow,
                                   own_domains=self.own_domains,
                                   llm_tiebreaker=self.llm_tiebreaker)
                if v.decision is Decision.DROP:
                    continue
                yield doc
                emitted += 1
                if self.max_items and emitted >= self.max_items:
                    return
            next_link = payload.get("@odata.nextLink")
            new_delta = payload.get("@odata.deltaLink")
            if next_link:
                url = next_link
                continue
            if cp and new_delta:
                cp.set(self.name, new_delta, key="mail_delta")
            return

    # ---- calendar -----------------------------------------------------

    def _fetch_calendar(self, cp: CheckpointStore | None) -> Iterable[RawDoc]:
        watermark = cp.get(self.name, key="calendar_watermark") if cp else None
        params = {
            "$top": str(self.page_size),
            "$orderby": "lastModifiedDateTime asc",
        }
        if watermark:
            params["$filter"] = f"lastModifiedDateTime gt {watermark}"
        url = f"{GRAPH}/me/events"
        emitted = 0
        newest = watermark

        while True:
            payload = self._get_url(url, params)
            params = {}
            for ev in payload.get("value", []):
                doc = _event_to_doc(ev)
                if doc is None:
                    continue
                yield doc
                emitted += 1
                last = ev.get("lastModifiedDateTime")
                if last and (newest is None or last > newest):
                    newest = last
                if self.max_items and emitted >= self.max_items:
                    if cp and newest:
                        cp.set(self.name, newest, key="calendar_watermark")
                    return
            next_link = payload.get("@odata.nextLink")
            if next_link:
                url = next_link
                continue
            if cp and newest:
                cp.set(self.name, newest, key="calendar_watermark")
            return

    # ---- HTTP ---------------------------------------------------------

    def _mint_access_token(self) -> str:
        url = TOKEN_URL_TMPL.format(tenant=self.tenant_id)
        data = urllib.parse.urlencode({
            "client_id": self.client_id,
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "scope": " ".join(DEFAULT_SCOPES),
        }).encode("ascii")
        req = urllib.request.Request(url, data=data, headers={
            "Content-Type": "application/x-www-form-urlencoded",
        })
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raise M365AuthError(
                f"Microsoft token endpoint -> HTTP {e.code}: "
                f"{e.read().decode('utf-8', 'replace')[:200]}"
            ) from e
        token = payload.get("access_token")
        if not token:
            raise M365AuthError(f"no access_token in response: {payload}")
        return token

    def _get_url(self, url: str, params: dict) -> dict:
        if params:
            qs = urllib.parse.urlencode(params, safe="$:")
            url = url + ("&" if "?" in url else "?") + qs
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {self._access_token}",
            "Accept": "application/json",
            "User-Agent": "synthbrain-m365/0.1",
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                raise M365AuthError(f"Graph auth failed ({e.code})") from e
            raise M365APIError(f"Graph -> HTTP {e.code} for {url}") from e
        except urllib.error.URLError as e:
            raise M365APIError(f"Graph network error: {e.reason}") from e


# ---- message + event parsers ------------------------------------------

def _msg_to_meta_and_doc(msg: dict) -> tuple[EmailMeta | None, RawDoc | None]:
    from_obj = (msg.get("from") or {}).get("emailAddress") or {}
    from_addr = (from_obj.get("address") or "").strip()
    from_name = (from_obj.get("name") or "").strip()

    to_addrs = [
        ((t or {}).get("emailAddress") or {}).get("address", "")
        for t in (msg.get("toRecipients") or [])
    ]
    cc_addrs = [
        ((t or {}).get("emailAddress") or {}).get("address", "")
        for t in (msg.get("ccRecipients") or [])
    ]
    subject = (msg.get("subject") or "").strip()

    body_obj = msg.get("body") or {}
    body_raw = body_obj.get("content") or ""
    if body_obj.get("contentType", "").lower() == "html":
        body_raw = _html_to_text(body_raw)
    body_clean = _strip_quoted_and_sig(body_raw.strip())

    headers = {}
    for h in msg.get("internetMessageHeaders") or []:
        name = (h.get("name") or "").lower()
        if name:
            headers[name] = h.get("value", "")

    meta = EmailMeta(
        from_addr=from_addr,
        from_name=from_name,
        to_addrs=[a for a in to_addrs + cc_addrs if a],
        subject=subject,
        body=body_clean,
        headers=headers,
    )

    if not meta.from_addr or (not body_clean and not subject):
        return meta, None

    msg_id = msg.get("id") or ""
    if not msg_id:
        return meta, None
    received = _parse_iso(msg.get("receivedDateTime"))

    body_lines = [
        f"# {subject or '(no subject)'}",
        "",
        f"_From:_ {from_name or from_addr} <{from_addr}>",
    ]
    if to_addrs:
        body_lines.append(f"_To:_ {', '.join(a for a in to_addrs if a)}")
    body_lines.append("")
    body_lines.append(body_clean)
    text = "\n".join(body_lines).strip()

    doc = RawDoc(
        text=text,
        source=ADAPTER_NAME,
        source_id=str(msg_id),
        url=f"https://outlook.office.com/mail/inbox/id/{urllib.parse.quote(msg_id, safe='')}",
        created_at=received or datetime.now(timezone.utc),
        meta={
            "from": from_addr,
            "to": [a for a in to_addrs if a],
            "subject": subject,
            "sub_source": "mail",
        },
    )
    return meta, doc


def _event_to_doc(ev: dict) -> RawDoc | None:
    subject = (ev.get("subject") or "").strip()
    if not subject:
        return None
    event_id = ev.get("id")
    if not event_id:
        return None
    start = ((ev.get("start") or {}).get("dateTime") or "")
    end = ((ev.get("end") or {}).get("dateTime") or "")
    location = ((ev.get("location") or {}).get("displayName") or "")
    body_obj = ev.get("body") or {}
    body_raw = body_obj.get("content") or ""
    if body_obj.get("contentType", "").lower() == "html":
        body_raw = _html_to_text(body_raw)
    attendees = [
        ((a.get("emailAddress") or {}).get("name")
         or (a.get("emailAddress") or {}).get("address") or "")
        for a in (ev.get("attendees") or [])
    ]
    attendees = [a for a in attendees if a]

    body_lines = [
        f"# {subject}",
        f"_When:_ {start} -> {end}",
    ]
    if location:
        body_lines.append(f"_Where:_ {location}")
    if attendees:
        body_lines.append(f"_Attendees:_ {', '.join(attendees)}")
    body_lines.append("")
    if body_raw.strip():
        body_lines.append(body_raw.strip())

    created = _parse_iso(start) or datetime.now(timezone.utc)
    return RawDoc(
        text="\n".join(body_lines).strip(),
        source=ADAPTER_NAME,
        source_id=str(event_id),
        url=ev.get("webLink") or "",
        created_at=created,
        meta={
            "subject": subject,
            "location": location,
            "attendees": attendees,
            "sub_source": "calendar",
        },
    )


def _parse_iso(value) -> datetime | None:
    if not value:
        return None
    try:
        v = value.replace("Z", "+00:00") if isinstance(value, str) else value
        dt = datetime.fromisoformat(v) if isinstance(v, str) else None
        if dt and dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (TypeError, ValueError):
        return None


def _own_domains_from_env() -> list[str]:
    raw = os.environ.get("M365_OWN_DOMAINS") or os.environ.get("OWN_DOMAINS") or ""
    return [d.strip() for d in raw.split(",") if d.strip()]
