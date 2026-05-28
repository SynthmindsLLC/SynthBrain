"""Dossier assembly — the north-star output. Spec + structure; synthesis is TODO.

dossier() is what the glasses ultimately call: resolve the people/events named in
the ambient cue, graph-join to the conversations that link them, and synthesize a
glanceable card. Depends on resolve() (see resolve.py) landing first.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .entities import EntityStore
from .index import BrainIndex
from .resolve import Status, resolve


@dataclass
class Card:
    """The popup. Keep it glanceable — HUD budget is ~5 lines (see G2 doc)."""
    name: str = ""
    role: str = ""              # title @ org
    relationship: str = ""     # how you know them / family note
    where_met: str = ""        # event + date + location
    discussed: list[str] = field(default_factory=list)  # 1-3 short bullets
    confidence: float = 0.0
    needs_disambiguation: list[str] = field(default_factory=list)  # candidate names if ambiguous


def dossier(
    store: EntityStore,
    index: BrainIndex,
    person_mention: str,
    event_hint: str = "",
    context: str = "",
    *,
    embedder=None,
    synthesize=None,
) -> Card:
    """Assemble the dossier. synthesize(person, event, chunks) -> list[str] is the
    LLM step (injected so this stays testable without an API)."""
    person_res = resolve(store, person_mention, context, "person", embedder=embedder)

    if person_res.status is Status.NO_MATCH:
        return Card(name=person_mention, confidence=0.0)
    if person_res.status is Status.AMBIGUOUS:
        # Do NOT guess — surface the choice.
        return Card(name=person_mention, confidence=person_res.confidence,
                    needs_disambiguation=[c.name for c in person_res.candidates])

    person = person_res.entity
    assert person is not None
    a = person.attributes

    card = Card(
        name=person.name,
        role=" @ ".join(x for x in (a.get("title", ""), a.get("org", "")) if x),
        relationship=a.get("note", ""),
        confidence=person_res.confidence,
    )

    # Resolve the event ("the party last fall") and find where they met.
    if event_hint:
        event_res = resolve(store, event_hint, context, "event", embedder=embedder)
        if event_res.status is Status.RESOLVED and event_res.entity:
            ev = event_res.entity
            card.where_met = f"{ev.name} — {ev.attributes.get('date','')} {ev.attributes.get('location','')}".strip()
            # TODO: confirm `person` actually attended `ev` via an edge; if not, drop where_met.

    # TODO: graph-join to conversation chunks linking person (+ event), then synthesize.
    #   chunks = index.query(f"{person.name} {event_hint} {context}", k=5)
    #   relevant = [c for c in chunks if _linked_to(store, person, c)]
    #   card.discussed = synthesize(person, event, relevant) if synthesize else [c['text'][:60] for c in relevant[:3]]

    return card
