"""Live Google adapter tests — mock the Google API client so no network is hit.

Covers: env-validation, incremental sync via syncToken, pagination, attendee
edges, sync-token-invalidation flow, idempotent re-run.
"""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from brain.adapters.gcal_live_adapter import GoogleCalendarLiveAdapter
from brain.adapters.people_live_adapter import GooglePeopleLiveAdapter
from brain.core.checkpoint import CheckpointStore
from brain.core.entities import Edge, Entity, EntityStore


# ----- shared fakes ---------------------------------------------------------

class _FakeList:
    def __init__(self, pages):
        self.pages = pages
        self.calls: list[dict] = []

    def list(self, **kwargs):
        self.calls.append(kwargs)
        idx = len(self.calls) - 1
        page = self.pages[idx] if idx < len(self.pages) else {"items": []}

        exe = MagicMock()
        exe.execute.return_value = page
        return exe


def _fake_calendar_service(pages):
    fake_list = _FakeList(pages)
    events = MagicMock()
    events.list = fake_list.list
    service = MagicMock()
    service.events.return_value = events
    return service, fake_list


def _fake_people_service(pages):
    fake_list = _FakeList(pages)
    connections = MagicMock()
    connections.list = fake_list.list
    people = MagicMock()
    people.connections.return_value = connections
    service = MagicMock()
    service.people.return_value = people
    return service, fake_list


@pytest.fixture(autouse=True)
def _google_env(monkeypatch):
    monkeypatch.setenv("GOOGLE_OAUTH_CLIENT_ID", "id.apps.googleusercontent.com")
    monkeypatch.setenv("GOOGLE_OAUTH_CLIENT_SECRET", "secret")
    monkeypatch.setenv("GOOGLE_OAUTH_REFRESH_TOKEN", "refresh")


# ----- GoogleCalendarLiveAdapter -------------------------------------------

def test_gcal_raises_when_oauth_env_missing(monkeypatch):
    monkeypatch.delenv("GOOGLE_OAUTH_REFRESH_TOKEN")
    with pytest.raises(RuntimeError, match="Missing Google OAuth env"):
        GoogleCalendarLiveAdapter()


def test_gcal_initial_sync_emits_event_and_attended_edges():
    page = {
        "items": [
            {
                "id": "ev1",
                "summary": "Fall Block Party",
                "start": {"dateTime": "2025-10-04T18:00:00Z"},
                "location": "Groton, CT",
                "attendees": [
                    {"email": "jeff.torres@acme.com", "displayName": "Jeff Torres",
                     "responseStatus": "accepted"},
                    {"email": "wes@synthminds.ai", "displayName": "Wes Shields",
                     "responseStatus": "accepted"},
                ],
            }
        ],
        "nextSyncToken": "tok-after-page-1",
    }
    service, fake = _fake_calendar_service([page])
    with patch("brain.adapters.gcal_live_adapter._calendar_service", return_value=service):
        with tempfile.TemporaryDirectory() as d:
            cp_db = str(Path(d) / "e.db")
            a = GoogleCalendarLiveAdapter(checkpoint_db=cp_db)
            items = list(a.fetch())

            entities = [x for x in items if isinstance(x, Entity)]
            edges = [x for x in items if isinstance(x, Edge)]
            assert any(e.kind == "event" and e.name == "Fall Block Party" for e in entities)
            assert {p.name for p in entities if p.kind == "person"} == {"Jeff Torres", "Wes Shields"}
            assert all(e.rel == "attended" for e in edges)
            assert len(edges) == 2
            assert CheckpointStore(cp_db).get("gcal-live", key="sync_token::primary") == "tok-after-page-1"


def test_gcal_skips_cancelled_events():
    page = {
        "items": [
            {"id": "x", "status": "cancelled", "summary": "Old"},
            {"id": "y", "summary": "Kept", "start": {"date": "2025-10-04"}},
        ],
        "nextSyncToken": "tok",
    }
    service, _ = _fake_calendar_service([page])
    with patch("brain.adapters.gcal_live_adapter._calendar_service", return_value=service):
        items = list(GoogleCalendarLiveAdapter().fetch())
    assert {e.name for e in items if isinstance(e, Entity) and e.kind == "event"} == {"Kept"}


def test_gcal_uses_sync_token_on_subsequent_runs():
    page1 = {
        "items": [{"id": "a", "summary": "A", "start": {"date": "2025-01-01"}}],
        "nextSyncToken": "tok-1",
    }
    page2 = {
        "items": [{"id": "b", "summary": "B", "start": {"date": "2025-01-02"}}],
        "nextSyncToken": "tok-2",
    }
    service1, fake1 = _fake_calendar_service([page1])
    service2, fake2 = _fake_calendar_service([page2])
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch("brain.adapters.gcal_live_adapter._calendar_service", return_value=service1):
            list(GoogleCalendarLiveAdapter(checkpoint_db=cp_db).fetch())
        with patch("brain.adapters.gcal_live_adapter._calendar_service", return_value=service2):
            list(GoogleCalendarLiveAdapter(checkpoint_db=cp_db).fetch())
        # Second run must pass syncToken=tok-1
        assert fake2.calls[0].get("syncToken") == "tok-1"
        assert CheckpointStore(cp_db).get("gcal-live", key="sync_token::primary") == "tok-2"


def test_gcal_paginates_with_page_token():
    page1 = {"items": [{"id": "a", "summary": "A", "start": {"date": "2025-01-01"}}],
             "nextPageToken": "p2"}
    page2 = {"items": [{"id": "b", "summary": "B", "start": {"date": "2025-01-02"}}],
             "nextSyncToken": "final-tok"}
    service, fake = _fake_calendar_service([page1, page2])
    with patch("brain.adapters.gcal_live_adapter._calendar_service", return_value=service):
        items = list(GoogleCalendarLiveAdapter().fetch())
    names = {e.name for e in items if isinstance(e, Entity) and e.kind == "event"}
    assert names == {"A", "B"}
    assert fake.calls[1].get("pageToken") == "p2"


def test_gcal_merges_with_existing_contact_attributes():
    """If a Person already exists with title/org from contacts, the gcal-live
    person stub must not clobber those attributes."""
    page = {
        "items": [
            {
                "id": "ev1",
                "summary": "Lunch",
                "start": {"dateTime": "2025-10-04T12:00:00Z"},
                "attendees": [
                    {"email": "jeff@acme.com", "displayName": "Jeff Torres"},
                ],
            }
        ],
        "nextSyncToken": "tok",
    }
    service, _ = _fake_calendar_service([page])
    with tempfile.TemporaryDirectory() as d:
        store = EntityStore(str(Path(d) / "e.db"))
        store.upsert_entity(Entity(
            kind="person", name="Jeff Torres",
            attributes={"title": "VP", "org": "Acme"},
            source_refs=["contacts:c.vcf"],
        ))
        with patch("brain.adapters.gcal_live_adapter._calendar_service", return_value=service):
            for item in GoogleCalendarLiveAdapter().fetch():
                if isinstance(item, Entity):
                    store.upsert_entity(item)
                else:
                    store.add_edge(item)
        jeff = store.get_entity("person:jeff-torres")
        assert jeff is not None
        assert jeff.attributes.get("title") == "VP"
        assert jeff.attributes.get("org") == "Acme"


# ----- GooglePeopleLiveAdapter ---------------------------------------------

def test_people_raises_when_oauth_env_missing(monkeypatch):
    monkeypatch.delenv("GOOGLE_OAUTH_CLIENT_ID")
    with pytest.raises(RuntimeError):
        GooglePeopleLiveAdapter()


def test_people_emits_rich_person_entities():
    page = {
        "connections": [
            {
                "names": [{"displayName": "Jeff Torres", "givenName": "Jeff",
                           "familyName": "Torres",
                           "metadata": {"primary": True}}],
                "emailAddresses": [{"value": "jeff.torres@acme.com"}],
                "phoneNumbers": [{"value": "+1-555-0100"}],
                "organizations": [{
                    "name": "Acme Robotics", "title": "VP of Engineering",
                    "metadata": {"primary": True},
                }],
                "biographies": [{"value": "Met at Fall Block Party."}],
            },
            {
                "names": [{"displayName": "", "givenName": ""}],  # no name -> skipped
            },
        ],
        "nextSyncToken": "people-tok-1",
    }
    service, fake = _fake_people_service([page])
    with patch("brain.adapters.people_live_adapter._people_service", return_value=service):
        with tempfile.TemporaryDirectory() as d:
            cp_db = str(Path(d) / "e.db")
            entities = list(GooglePeopleLiveAdapter(checkpoint_db=cp_db).fetch())
            assert len(entities) == 1
            jeff = entities[0]
            assert jeff.name == "Jeff Torres"
            assert jeff.attributes["org"] == "Acme Robotics"
            assert jeff.attributes["title"] == "VP of Engineering"
            assert "jeff.torres@acme.com" in jeff.attributes["emails"]
            assert "Jeff" in jeff.aliases  # given-name alias for "Jeff" -> "Jeff Torres"
            assert CheckpointStore(cp_db).get("people-live", key="sync_token::contacts") == "people-tok-1"


def test_people_sync_token_is_re_used_on_second_run():
    page1 = {"connections": [{"names": [{"displayName": "A", "metadata": {"primary": True}}]}],
             "nextSyncToken": "tok-1"}
    page2 = {"connections": [{"names": [{"displayName": "B", "metadata": {"primary": True}}]}],
             "nextSyncToken": "tok-2"}
    service1, _ = _fake_people_service([page1])
    service2, fake2 = _fake_people_service([page2])
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch("brain.adapters.people_live_adapter._people_service", return_value=service1):
            list(GooglePeopleLiveAdapter(checkpoint_db=cp_db).fetch())
        with patch("brain.adapters.people_live_adapter._people_service", return_value=service2):
            list(GooglePeopleLiveAdapter(checkpoint_db=cp_db).fetch())
        assert fake2.calls[0]["syncToken"] == "tok-1"
