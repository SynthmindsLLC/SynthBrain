"""Live Google Calendar entity adapter — events + 'attended' edges, incremental.

Uses Google Calendar v3 (`events.list` with `syncToken`) to fetch only new or
changed events on each run. First run does an initial sync (no syncToken,
optionally bounded by `time_min`); subsequent runs use the syncToken stored in
CheckpointStore. If Google invalidates the token (HTTP 410), we drop the
checkpoint and do a fresh initial sync — same idempotent merge into the entity
store, so worst case is a re-write of unchanged rows.

Auth: OAuth2 refresh-token flow against the existing Google client used for
Drive. Add the `https://www.googleapis.com/auth/calendar.readonly` scope to
that client (one re-consent click in OAuth Playground) and we're done.

Why this isn't `.ics`: an .ics export is a one-shot dump. Live sync needs an
API that supports "give me what's changed since token X." That's only Calendar v3.

This adapter requires `google-api-python-client` and `google-auth-oauthlib`,
which are intentionally optional deps. We import lazily so the rest of the
brain still works without them.
"""

from __future__ import annotations

import os
from typing import Iterable

from ..core.checkpoint import CheckpointStore
from ..core.entities import Edge, Entity
from .entity_base import EntityAdapter

ADAPTER_NAME = "gcal-live"
DEFAULT_CALENDAR = "primary"
DEFAULT_PAGE_SIZE = 250
SYNC_TOKEN_INVALID_HTTP = 410


def _clean(addr: str) -> str:
    return str(addr).replace("mailto:", "").replace("MAILTO:", "").strip()


class GoogleCalendarLiveAdapter(EntityAdapter):
    """Pulls events from Google Calendar v3 incrementally.

    Each event -> Event entity; each attendee -> Person stub + 'attended' edge.
    Contacts adapter (.vcf) writes the rich Person attributes; this adapter just
    keeps the graph current. upsert_entity does the merge so the rich attributes
    survive."""

    name = ADAPTER_NAME

    def __init__(
        self,
        *,
        calendar_id: str = DEFAULT_CALENDAR,
        client_id: str | None = None,
        client_secret: str | None = None,
        refresh_token: str | None = None,
        checkpoint_db: str | None = None,
        time_min: str | None = None,
        page_size: int = DEFAULT_PAGE_SIZE,
    ) -> None:
        self.calendar_id = calendar_id
        self.client_id = client_id or os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
        self.refresh_token = refresh_token or os.environ.get("GOOGLE_OAUTH_REFRESH_TOKEN")
        if not all([self.client_id, self.client_secret, self.refresh_token]):
            raise RuntimeError(
                "Missing Google OAuth env. Set GOOGLE_OAUTH_CLIENT_ID, "
                "GOOGLE_OAUTH_CLIENT_SECRET, GOOGLE_OAUTH_REFRESH_TOKEN (see "
                "docs/setup/google-oauth.md; add calendar.readonly scope to your client)."
            )
        self.checkpoint_db = checkpoint_db
        self.time_min = time_min
        self.page_size = page_size

    def fetch(self) -> Iterable[Entity | Edge]:
        from googleapiclient.errors import HttpError  # type: ignore[import-not-found]

        service = _calendar_service(self.client_id, self.client_secret, self.refresh_token)
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        ckey = self._checkpoint_key()
        sync_token = cp.get(self.name, key=ckey) if cp else None

        page_token: str | None = None
        next_sync_token: str | None = None
        try:
            while True:
                req: dict = {
                    "calendarId": self.calendar_id,
                    "maxResults": self.page_size,
                    "singleEvents": True,
                }
                if sync_token:
                    req["syncToken"] = sync_token
                else:
                    if self.time_min:
                        req["timeMin"] = self.time_min
                    req["orderBy"] = "startTime"
                if page_token:
                    req["pageToken"] = page_token

                resp = service.events().list(**req).execute()
                for ev in resp.get("items", []):
                    yield from _event_to_graph(ev, self.calendar_id)

                next_sync_token = resp.get("nextSyncToken") or next_sync_token
                page_token = resp.get("nextPageToken")
                if not page_token:
                    break
        except HttpError as e:
            status = getattr(e, "resp", None)
            code = getattr(status, "status", None) if status else None
            if code == SYNC_TOKEN_INVALID_HTTP and sync_token:
                if cp:
                    cp.clear(self.name, key=ckey)
                # Caller can retry; we don't auto-recurse to keep the call simple.
                raise RuntimeError(
                    "Google syncToken invalidated; checkpoint cleared. Re-run."
                ) from e
            raise

        if cp and next_sync_token:
            cp.set(self.name, next_sync_token, key=ckey)

    def _checkpoint_key(self) -> str:
        # One token per calendar; let the user sync multiple calendars later.
        return f"sync_token::{self.calendar_id}"


def _event_to_graph(ev: dict, calendar_id: str) -> Iterable[Entity | Edge]:
    if ev.get("status") == "cancelled":
        return
    summary = (ev.get("summary") or "").strip()
    if not summary:
        return
    start = ev.get("start", {}) or {}
    date_str = start.get("dateTime") or start.get("date") or ""
    location = (ev.get("location") or "").strip()

    event = Entity(
        kind="event",
        name=summary,
        attributes={
            "date": date_str,
            "location": location,
            "google_event_id": ev.get("id", ""),
            "calendar_id": calendar_id,
        },
        source_refs=[f"gcal:{calendar_id}:{ev.get('id', '')}"],
    )
    yield event

    for att in ev.get("attendees", []) or []:
        if att.get("resource"):
            continue
        email = _clean(att.get("email", ""))
        display = (att.get("displayName") or "").strip() or email
        if not display:
            continue
        person = Entity(
            kind="person",
            name=display,
            aliases=[email] if email else [],
            attributes={"emails": [email]} if email else {},
            source_refs=[f"gcal:{calendar_id}"],
        )
        yield person
        yield Edge(
            src=person.id,
            rel="attended",
            dst=event.id,
            attributes={
                "via": "gcal",
                "response": att.get("responseStatus", ""),
            },
        )


def _calendar_service(client_id: str, client_secret: str, refresh_token: str):
    """Lazy import + build the Google API service so the rest of the brain
    keeps working when google-api-python-client isn't installed."""
    from google.oauth2.credentials import Credentials  # type: ignore[import-not-found]
    from googleapiclient.discovery import build  # type: ignore[import-not-found]

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=["https://www.googleapis.com/auth/calendar.readonly"],
    )
    return build("calendar", "v3", credentials=creds, cache_discovery=False)
