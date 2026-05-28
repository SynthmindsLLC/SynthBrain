"""Dossier assembly — the north-star output.

dossier() is what the glasses ultimately call: resolve the people/events named
in the ambient cue, graph-join to the conversations that link them, and
synthesize a glanceable card. Built on top of resolve() (resolve.py).

Card shape is constrained by HUD budget per second-brain/docs/g2-r1-...md:
3-5 bullets, <=8 words each. We enforce that here so the surface can't blow it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

from .entities import Entity, EntityStore
from .index import BrainIndex
from .resolve import Resolution, Status, resolve

MAX_BULLETS = 5
MAX_WORDS_PER_BULLET = 8


@dataclass
class Card:
    """The popup. Glanceable. Truncated by `_truncate_bullets`."""
    name: str = ""
    role: str = ""              # title @ org
    relationship: str = ""      # how you know them / family note
    where_met: str = ""         # event + date + location
    discussed: list[str] = field(default_factory=list)  # 1-3 short bullets
    confidence: float = 0.0
    needs_disambiguation: list[str] = field(default_factory=list)
    rationale: str = ""


SynthesizeFn = Callable[[Entity, Entity | None, list[dict]], list[str]]


def dossier(
    store: EntityStore,
    index: BrainIndex | None,
    person_mention: str,
    event_hint: str = "",
    context: str = "",
    *,
    embedder=None,
    synthesize: SynthesizeFn | None = None,
    chunk_k: int = 6,
) -> Card:
    """Assemble the dossier card.

    `synthesize(person, event, chunks) -> list[str]` is the LLM step, injected
    so this stays testable without an API. When omitted, falls back to surfacing
    the first sentence of the top-ranked chunk(s).
    """
    # Event hint is a powerful disambiguator (e.g. "Jeff" + "Fall Block Party"
    # short-circuits the two-Jeffs problem via graph proximity), so fold it into
    # the resolve context.
    resolve_context = " ".join(x for x in (event_hint, context) if x)
    person_res = resolve(store, person_mention, resolve_context, "person", embedder=embedder)

    if person_res.status is Status.NO_MATCH:
        return Card(name=person_mention, confidence=0.0,
                    rationale=person_res.rationale)
    if person_res.status is Status.AMBIGUOUS:
        return Card(
            name=person_mention,
            confidence=person_res.confidence,
            needs_disambiguation=[c.name for c in person_res.candidates],
            rationale=person_res.rationale,
        )

    person = person_res.entity
    assert person is not None
    card = _person_to_card_header(person, person_res)

    event = _resolve_event(store, event_hint, context, embedder)
    if event is not None and _person_attended(store, person, event):
        card.where_met = _format_event(event)

    if index is not None:
        chunks = _relevant_chunks(index, person, event, context, k=chunk_k)
        bullets = _bullets_from(chunks, person, event, synthesize)
        card.discussed = _truncate_bullets(bullets)

    return card


def _person_to_card_header(person: Entity, res: Resolution) -> Card:
    a = person.attributes
    role_parts = [x for x in (a.get("title", ""), a.get("org", "")) if x]
    return Card(
        name=person.name,
        role=" @ ".join(role_parts),
        relationship=a.get("note", ""),
        confidence=res.confidence,
        rationale=res.rationale,
    )


def _resolve_event(
    store: EntityStore, hint: str, context: str, embedder
) -> Entity | None:
    if not hint:
        return None
    res = resolve(store, hint, context, "event", embedder=embedder)
    if res.status is Status.RESOLVED:
        return res.entity
    return None


def _person_attended(store: EntityStore, person: Entity, event: Entity) -> bool:
    """Don't claim where_met unless an `attended` edge actually exists."""
    for edge, _ in store.neighbors(person.id, rel="attended"):
        if edge.dst == event.id:
            return True
    return False


def _format_event(event: Entity) -> str:
    a = event.attributes
    parts = [event.name]
    if a.get("date"):
        parts.append(str(a["date"]))
    if a.get("location"):
        parts.append(str(a["location"]))
    return " - ".join(parts)


def _relevant_chunks(
    index: BrainIndex,
    person: Entity,
    event: Entity | None,
    context: str,
    *,
    k: int,
) -> list[dict]:
    """Pull top chunks that mention the person (and event if provided)."""
    query_bits = [person.name]
    if event:
        query_bits.append(event.name)
    if context:
        query_bits.append(context)
    raw = index.query(" ".join(query_bits), k=k * 2)
    person_id = person.id
    event_id = event.id if event else None
    filtered: list[dict] = []
    for c in raw:
        tags = c.get("entity_tags", []) or []
        if person_id not in tags and person.name.lower() not in c.get("text", "").lower():
            continue
        if event_id and event_id not in tags and (event.name.lower() not in c.get("text", "").lower()):
            continue
        filtered.append(c)
        if len(filtered) >= k:
            break
    if not filtered:
        return raw[:k]
    return filtered


def _bullets_from(
    chunks: list[dict],
    person: Entity,
    event: Entity | None,
    synthesize: SynthesizeFn | None,
) -> list[str]:
    if not chunks:
        return []
    if synthesize is not None:
        return synthesize(person, event, chunks)
    bullets: list[str] = []
    for c in chunks[:MAX_BULLETS]:
        sentence = _first_sentence(c.get("text", ""))
        if sentence:
            bullets.append(sentence)
    return bullets


def _first_sentence(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    for terminator in (". ", "? ", "! ", "\n"):
        idx = text.find(terminator)
        if idx > 0:
            return text[:idx].strip()
    return text[:120]


def _truncate_bullets(bullets: list[str]) -> list[str]:
    out: list[str] = []
    for b in bullets[:MAX_BULLETS]:
        words = b.split()
        truncated = " ".join(words[:MAX_WORDS_PER_BULLET])
        if len(words) > MAX_WORDS_PER_BULLET:
            truncated += "..."
        out.append(truncated)
    return out
