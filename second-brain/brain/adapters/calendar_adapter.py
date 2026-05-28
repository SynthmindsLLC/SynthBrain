"""Calendar adapter — iCalendar (.ics) -> Event entities + 'attended' edges.

.ics is the universal calendar export (Google, Outlook, Apple). Each VEVENT
becomes an Event node; each ATTENDEE becomes an 'attended' edge from a Person to
that Event. This is what resolves "the party last fall" AND tells us who was
there — the two halves of the dossier join.

Attendee->Person linking here is by email/name (deterministic). Fuzzy linking
for messy real data is the resolve() step that comes next; this lays the edges.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from icalendar import Calendar

from ..core.entities import Edge, Entity, canonical_id
from .entity_base import EntityAdapter


def _clean(addr: str) -> str:
    return str(addr).replace("mailto:", "").replace("MAILTO:", "").strip()


class CalendarAdapter(EntityAdapter):
    name = "calendar"

    def __init__(self, source: str) -> None:
        self.source = Path(source)

    def fetch(self) -> Iterable[Entity | Edge]:
        if not self.source.exists():
            raise FileNotFoundError(
                f"iCalendar file not found: {self.source}. Export your calendar as "
                ".ics (Google: Settings > Export; Outlook: Save Calendar)."
            )
        cal = Calendar.from_ical(self.source.read_bytes())
        for ev in cal.walk("VEVENT"):
            summary = str(ev.get("summary", "")).strip()
            if not summary:
                continue
            dt = ev.get("dtstart")
            date_str = dt.dt.isoformat() if dt is not None else ""
            location = str(ev.get("location", "")).strip()

            event = Entity(
                kind="event",
                name=summary,
                attributes={"date": date_str, "location": location},
                source_refs=[f"calendar:{self.source.name}"],
            )
            yield event

            # Attendees -> people + 'attended' edges.
            attendees = ev.get("attendee")
            if attendees is None:
                continue
            if not isinstance(attendees, list):
                attendees = [attendees]
            for att in attendees:
                email = _clean(att)
                cn = str(att.params.get("CN", "")).strip() if hasattr(att, "params") else ""
                display = cn or email
                if not display:
                    continue
                # Lightweight person stub keyed on name; if a richer Person from
                # Contacts already exists under the same canonical id, upsert merges.
                person = Entity(
                    kind="person",
                    name=display,
                    aliases=[email] if email else [],
                    attributes={"emails": [email]} if email else {},
                    source_refs=[f"calendar:{self.source.name}"],
                )
                yield person
                yield Edge(
                    src=person.id,
                    rel="attended",
                    dst=event.id,
                    attributes={"via": "calendar"},
                )
