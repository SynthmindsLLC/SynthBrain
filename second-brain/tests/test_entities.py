"""Entity-layer tests: ingest, cross-source merge, the disambiguation gap, traversal.

    pytest -q
"""

import tempfile
from pathlib import Path

from brain.adapters.calendar_adapter import CalendarAdapter
from brain.adapters.contacts_adapter import ContactsAdapter
from brain.adapters.entity_base import ingest_entities
from brain.core.entities import EntityStore

VCF = """BEGIN:VCARD
VERSION:3.0
FN:Jeff Torres
N:Torres;Jeff;;;
ORG:Acme Robotics;Engineering
TITLE:VP of Engineering
EMAIL:jeff.torres@acme.com
NOTE:Married to Dana\\; two kids.
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:Jeff Brennan
N:Brennan;Jeff;;;
ORG:Mystic Seaport Museum
EMAIL:jeff.b@mysticseaport.org
END:VCARD
"""

ICS = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//t//EN
BEGIN:VEVENT
UID:e1@t
SUMMARY:Fall Block Party
DTSTART:20251004T180000Z
LOCATION:Groton, CT
ATTENDEE;CN=Jeff Torres:mailto:jeff.torres@acme.com
ATTENDEE;CN=Wes Shields:mailto:wes@synthminds.ai
END:VEVENT
END:VCALENDAR
"""


def _load(tmp: Path) -> EntityStore:
    (tmp / "c.vcf").write_text(VCF, encoding="utf-8")
    (tmp / "c.ics").write_text(ICS, encoding="utf-8")
    store = EntityStore(str(tmp / "e.db"))
    ingest_entities(store, ContactsAdapter(str(tmp / "c.vcf")))
    ingest_entities(store, CalendarAdapter(str(tmp / "c.ics")))
    return store


def test_contacts_become_person_entities():
    with tempfile.TemporaryDirectory() as d:
        store = _load(Path(d))
        jeff = store.get_entity("person:jeff-torres")
        assert jeff is not None
        assert jeff.attributes["org"] == "Acme Robotics"
        assert "Married to Dana" in jeff.attributes["note"]


def test_cross_source_merge_is_one_node():
    # Jeff Torres appears in BOTH contacts and the calendar; must be ONE entity.
    with tempfile.TemporaryDirectory() as d:
        store = _load(Path(d))
        jeffs = [e for e in store.all_entities("person") if e.name == "Jeff Torres"]
        assert len(jeffs) == 1
        # contact attributes survived the calendar-stub merge
        assert jeffs[0].attributes.get("title") == "VP of Engineering"


def test_attended_edge_and_traversal():
    with tempfile.TemporaryDirectory() as d:
        store = _load(Path(d))
        events = store.neighbors("person:jeff-torres", "attended")
        names = {ev.name for _e, ev in events if ev}
        assert "Fall Block Party" in names


def test_disambiguation_gap_is_real():
    # The reason resolve() needs context: bare "Jeff" matches two distinct people.
    with tempfile.TemporaryDirectory() as d:
        store = _load(Path(d))
        matches = store.find_by_name("Jeff", "person")
        ids = {m.id for m in matches}
        assert {"person:jeff-torres", "person:jeff-brennan"} <= ids
