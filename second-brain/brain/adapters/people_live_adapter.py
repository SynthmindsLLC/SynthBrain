"""Live Google People (Contacts) adapter — Person entities, incremental.

Uses Google People API v1 `people.connections.list` with `syncToken` to fetch
only new/changed contacts. Same merge-on-conflict story as the .vcf adapter:
re-running enriches Person nodes rather than clobbering them.

Auth: OAuth2 refresh-token flow against the existing Google client. Add
`https://www.googleapis.com/auth/contacts.readonly` scope to that client.

Required env: GOOGLE_OAUTH_CLIENT_ID, GOOGLE_OAUTH_CLIENT_SECRET,
GOOGLE_OAUTH_REFRESH_TOKEN.
"""

from __future__ import annotations

import os
from typing import Iterable

from ..core.checkpoint import CheckpointStore
from ..core.entities import Entity
from .entity_base import EntityAdapter

ADAPTER_NAME = "people-live"
DEFAULT_PAGE_SIZE = 1000
PERSON_FIELDS = (
    "names,emailAddresses,phoneNumbers,organizations,addresses,biographies,birthdays,memberships"
)
SYNC_TOKEN_INVALID_HTTP = 410


class GooglePeopleLiveAdapter(EntityAdapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        refresh_token: str | None = None,
        checkpoint_db: str | None = None,
        page_size: int = DEFAULT_PAGE_SIZE,
    ) -> None:
        self.client_id = client_id or os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
        self.refresh_token = refresh_token or os.environ.get("GOOGLE_OAUTH_REFRESH_TOKEN")
        if not all([self.client_id, self.client_secret, self.refresh_token]):
            raise RuntimeError(
                "Missing Google OAuth env. Set GOOGLE_OAUTH_CLIENT_ID, "
                "GOOGLE_OAUTH_CLIENT_SECRET, GOOGLE_OAUTH_REFRESH_TOKEN (see "
                "docs/setup/google-oauth.md; add contacts.readonly scope)."
            )
        self.checkpoint_db = checkpoint_db
        self.page_size = page_size

    def fetch(self) -> Iterable[Entity]:
        from googleapiclient.errors import HttpError  # type: ignore[import-not-found]

        service = _people_service(self.client_id, self.client_secret, self.refresh_token)
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        ckey = "sync_token::contacts"
        sync_token = cp.get(self.name, key=ckey) if cp else None

        page_token: str | None = None
        next_sync_token: str | None = None

        try:
            while True:
                req: dict = {
                    "resourceName": "people/me",
                    "personFields": PERSON_FIELDS,
                    "pageSize": self.page_size,
                    "requestSyncToken": True,
                }
                if sync_token:
                    req["syncToken"] = sync_token
                if page_token:
                    req["pageToken"] = page_token

                resp = service.people().connections().list(**req).execute()
                for person in resp.get("connections", []):
                    e = _person_to_entity(person)
                    if e is not None:
                        yield e

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
                raise RuntimeError(
                    "Google People syncToken invalidated; checkpoint cleared. Re-run."
                ) from e
            raise

        if cp and next_sync_token:
            cp.set(self.name, next_sync_token, key=ckey)


def _person_to_entity(person: dict) -> Entity | None:
    names = person.get("names", []) or []
    primary = next((n for n in names if (n.get("metadata") or {}).get("primary")), None)
    primary = primary or (names[0] if names else None)
    full_name = (primary or {}).get("displayName") or ""
    if not full_name.strip():
        return None
    given = (primary or {}).get("givenName") or ""
    family = (primary or {}).get("familyName") or ""

    emails = [e.get("value") for e in (person.get("emailAddresses") or []) if e.get("value")]
    phones = [p.get("value") for p in (person.get("phoneNumbers") or []) if p.get("value")]
    orgs = person.get("organizations") or []
    primary_org = next((o for o in orgs if (o.get("metadata") or {}).get("primary")), None) or (orgs[0] if orgs else None)
    bios = person.get("biographies") or []
    note = (bios[0].get("value") if bios else "") or ""
    bdays = person.get("birthdays") or []
    bday = (bdays[0].get("text") if bdays else "") or ""

    attrs: dict = {"family_name": family, "given_name": given}
    if emails:
        attrs["emails"] = emails
    if phones:
        attrs["phones"] = phones
    if primary_org:
        if primary_org.get("name"):
            attrs["org"] = primary_org["name"]
        if primary_org.get("title"):
            attrs["title"] = primary_org["title"]
    if note:
        attrs["note"] = note
    if bday:
        attrs["birthday"] = bday

    aliases = [full_name]
    if given:
        aliases.append(given)
    aliases += emails

    return Entity(
        kind="person",
        name=full_name,
        aliases=aliases,
        attributes=attrs,
        source_refs=["people-live"],
    )


def _people_service(client_id: str, client_secret: str, refresh_token: str):
    from google.oauth2.credentials import Credentials  # type: ignore[import-not-found]
    from googleapiclient.discovery import build  # type: ignore[import-not-found]

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=["https://www.googleapis.com/auth/contacts.readonly"],
    )
    return build("people", "v1", credentials=creds, cache_discovery=False)
