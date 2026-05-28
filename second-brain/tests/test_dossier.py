"""dossier() tests — graph join + glanceable card assembly."""

from __future__ import annotations

import tempfile
from pathlib import Path

from brain.adapters.calendar_adapter import CalendarAdapter
from brain.adapters.contacts_adapter import ContactsAdapter
from brain.adapters.entity_base import ingest_entities
from brain.core.dossier import MAX_BULLETS, MAX_WORDS_PER_BULLET, dossier
from brain.core.embed import FakeEmbedder
from brain.core.entities import EntityStore
from brain.core.index import BrainIndex
from brain.core.schema import MemoryChunk


VCF = """BEGIN:VCARD
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
END:VEVENT
END:VCALENDAR
"""


def _bootstrap(tmp: Path) -> tuple[EntityStore, BrainIndex]:
    (tmp / "c.vcf").write_text(VCF, encoding="utf-8")
    (tmp / "c.ics").write_text(ICS, encoding="utf-8")
    store = EntityStore(str(tmp / "e.db"))
    ingest_entities(store, ContactsAdapter(str(tmp / "c.vcf")))
    ingest_entities(store, CalendarAdapter(str(tmp / "c.ics")))
    index = BrainIndex(str(tmp / "lance"), FakeEmbedder())
    return store, index


def test_card_for_unique_person_includes_role_and_relationship():
    with tempfile.TemporaryDirectory() as d:
        store, index = _bootstrap(Path(d))
        card = dossier(store, index, "Jeff Brennan")
        assert card.name == "Jeff Brennan"
        assert "Curator" in card.role and "Mystic Seaport Museum" in card.role
        assert "Boat conservation" in card.relationship
        assert card.confidence >= 0.9


def test_card_for_ambiguous_mention_returns_chooser_not_guess():
    with tempfile.TemporaryDirectory() as d:
        store, index = _bootstrap(Path(d))
        card = dossier(store, index, "Jeff", context="")
        assert set(card.needs_disambiguation) == {"Jeff Torres", "Jeff Brennan"}
        assert not card.role  # we refused to guess


def test_card_disambiguated_by_event_hint():
    with tempfile.TemporaryDirectory() as d:
        store, index = _bootstrap(Path(d))
        card = dossier(
            store,
            index,
            "Jeff",
            event_hint="Fall Block Party",
            context="from the party last fall",
        )
        assert card.name == "Jeff Torres"
        assert "Fall Block Party" in card.where_met
        assert "Groton" in card.where_met


def test_card_where_met_only_set_when_attended_edge_exists():
    # Brennan did NOT attend the Fall Block Party; if we wrongly disambiguate
    # to him, where_met must NOT claim he was there.
    with tempfile.TemporaryDirectory() as d:
        store, index = _bootstrap(Path(d))
        card = dossier(
            store,
            index,
            "Jeff Brennan",
            event_hint="Fall Block Party",
        )
        assert card.name == "Jeff Brennan"
        assert not card.where_met


def test_card_for_unknown_person_returns_empty_card():
    with tempfile.TemporaryDirectory() as d:
        store, index = _bootstrap(Path(d))
        card = dossier(store, index, "Beyonce Knowles")
        assert card.name == "Beyonce Knowles"
        assert card.confidence == 0.0
        assert not card.role
        assert not card.needs_disambiguation


def test_bullets_truncated_to_hud_budget():
    with tempfile.TemporaryDirectory() as d:
        store, index = _bootstrap(Path(d))
        index.add_chunks([
            MemoryChunk(
                text="We discussed the maritime conservation roadmap and the museum's planned restoration of the Charles W Morgan over a long lunch.",
                source="mem",
                source_id="n1",
                entity_tags=["person:jeff-brennan"],
            ),
            MemoryChunk(
                text="Jeff also shared his concerns about funding for the boat shed expansion next spring.",
                source="mem",
                source_id="n2",
                entity_tags=["person:jeff-brennan"],
            ),
        ])
        card = dossier(store, index, "Jeff Brennan")
        assert 0 < len(card.discussed) <= MAX_BULLETS
        for bullet in card.discussed:
            words = bullet.replace("...", "").split()
            assert len(words) <= MAX_WORDS_PER_BULLET, bullet


def test_synthesize_hook_is_called_when_provided():
    calls = {"n": 0}

    def fake_synthesize(person, event, chunks):
        calls["n"] += 1
        return [f"about {person.name}", "second bullet here"]

    with tempfile.TemporaryDirectory() as d:
        store, index = _bootstrap(Path(d))
        index.add_chunks([
            MemoryChunk(
                text="Jeff Brennan note about restoration work.",
                source="mem",
                source_id="n1",
                entity_tags=["person:jeff-brennan"],
            ),
        ])
        card = dossier(store, index, "Jeff Brennan", synthesize=fake_synthesize)
        assert calls["n"] == 1
        assert card.discussed[0].startswith("about Jeff")
