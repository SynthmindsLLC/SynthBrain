"""resolve() tests — the make-or-break disambiguation logic.

Covers the algorithm tiers + the AMBIGUOUS-below-threshold contract that keeps
the wrong dossier off the lens.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from brain.adapters.calendar_adapter import CalendarAdapter
from brain.adapters.contacts_adapter import ContactsAdapter
from brain.adapters.entity_base import ingest_entities
from brain.core.entities import EntityStore
from brain.core.embed import FakeEmbedder
from brain.core.resolve import (
    CONFIDENCE_THRESHOLD,
    Status,
    resolve,
)


VCF_TWO_JEFFS = """BEGIN:VCARD
VERSION:3.0
FN:Jeff Torres
N:Torres;Jeff;;;
ORG:Acme Robotics;Engineering
TITLE:VP of Engineering
EMAIL:jeff.torres@acme.com
NOTE:Met at Fall Block Party in Groton.
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:Jeff Brennan
N:Brennan;Jeff;;;
ORG:Mystic Seaport Museum
TITLE:Curator
EMAIL:jeff.b@mysticseaport.org
NOTE:Boat conservation lead.
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:Sarah Lin
N:Lin;Sarah;;;
ORG:Acme Robotics
TITLE:CTO
EMAIL:sarah@acme.com
END:VCARD
"""

ICS = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//t//EN
BEGIN:VEVENT
UID:party@t
SUMMARY:Fall Block Party
DTSTART:20251004T180000Z
LOCATION:Groton, CT
ATTENDEE;CN=Jeff Torres:mailto:jeff.torres@acme.com
ATTENDEE;CN=Wes Shields:mailto:wes@synthminds.ai
END:VEVENT
BEGIN:VEVENT
UID:gala@t
SUMMARY:Maritime Gala
DTSTART:20250912T190000Z
LOCATION:Mystic, CT
ATTENDEE;CN=Jeff Brennan:mailto:jeff.b@mysticseaport.org
END:VEVENT
END:VCALENDAR
"""


def _store(tmp: Path) -> EntityStore:
    (tmp / "c.vcf").write_text(VCF_TWO_JEFFS, encoding="utf-8")
    (tmp / "c.ics").write_text(ICS, encoding="utf-8")
    s = EntityStore(str(tmp / "e.db"))
    ingest_entities(s, ContactsAdapter(str(tmp / "c.vcf")))
    ingest_entities(s, CalendarAdapter(str(tmp / "c.ics")))
    return s


def test_unique_alias_match_is_high_confidence():
    with tempfile.TemporaryDirectory() as d:
        store = _store(Path(d))
        r = resolve(store, "Sarah Lin")
        assert r.status is Status.RESOLVED
        assert r.entity is not None
        assert r.entity.name == "Sarah Lin"
        assert r.confidence >= 0.9


def test_two_jeffs_disambiguated_by_event_in_context():
    with tempfile.TemporaryDirectory() as d:
        store = _store(Path(d))
        r = resolve(store, "Jeff", context="from the Fall Block Party last fall")
        assert r.status is Status.RESOLVED, r.rationale
        assert r.entity is not None
        assert r.entity.name == "Jeff Torres"
        assert r.confidence >= CONFIDENCE_THRESHOLD


def test_two_jeffs_disambiguated_by_org_in_context():
    with tempfile.TemporaryDirectory() as d:
        store = _store(Path(d))
        r = resolve(store, "Jeff", context="the Mystic Seaport Museum curator")
        assert r.status is Status.RESOLVED, r.rationale
        assert r.entity is not None
        assert r.entity.name == "Jeff Brennan"


def test_two_jeffs_with_no_context_returns_ambiguous():
    with tempfile.TemporaryDirectory() as d:
        store = _store(Path(d))
        r = resolve(store, "Jeff", context="")
        assert r.status is Status.AMBIGUOUS
        assert {c.name for c in r.candidates} == {"Jeff Torres", "Jeff Brennan"}


def test_two_jeffs_with_weak_context_returns_ambiguous():
    # Generic context that points to neither candidate must NOT confidently pick one.
    with tempfile.TemporaryDirectory() as d:
        store = _store(Path(d))
        r = resolve(store, "Jeff", context="we were talking about the weather yesterday")
        assert r.status is Status.AMBIGUOUS, r.rationale


def test_no_match_for_unknown_name():
    with tempfile.TemporaryDirectory() as d:
        store = _store(Path(d))
        r = resolve(store, "Beyonce Knowles")
        assert r.status is Status.NO_MATCH


def test_event_resolution_works_too():
    with tempfile.TemporaryDirectory() as d:
        store = _store(Path(d))
        r = resolve(store, "Fall Block Party", kind="event")
        assert r.status is Status.RESOLVED
        assert r.entity is not None
        assert "Groton" in (r.entity.attributes.get("location") or "")


def test_embedder_signal_does_not_break_offline_path():
    # With FakeEmbedder, embed scores are deterministic noise; should still produce
    # a sensible result when graph proximity dominates.
    with tempfile.TemporaryDirectory() as d:
        store = _store(Path(d))
        r = resolve(
            store,
            "Jeff",
            context="from the Fall Block Party last fall",
            embedder=FakeEmbedder(),
        )
        assert r.status is Status.RESOLVED
        assert r.entity is not None
        assert r.entity.name == "Jeff Torres"


def test_resolution_carries_per_candidate_scores():
    with tempfile.TemporaryDirectory() as d:
        store = _store(Path(d))
        r = resolve(store, "Jeff", context="Mystic Seaport Museum")
        assert len(r.scores) == 2
        score_map = dict(r.scores)
        assert score_map["person:jeff-brennan"] > score_map["person:jeff-torres"]
