"""Entity resolution — THE NEXT TASK. Currently a spec + deterministic fallback.

resolve() turns a heard/seen mention ("Jeff") plus surrounding context
("...the party last fall...") into the right entity, WITH a confidence. This is
the make-or-break piece for the dossier: a wrong dossier on the lens is worse
than no dossier, so this must refuse to guess.

Status: the exact/alias path (tier 1) and the ambiguity signal (tier 2 trigger)
are implemented deterministically so it's testable offline. The context-based
disambiguation (graph proximity + embedding similarity) and the fuzzy fallback
are TODO — see ROADMAP.md "NEXT TASK".
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .entities import Entity, EntityStore


class Status(str, Enum):
    RESOLVED = "resolved"      # one confident match
    AMBIGUOUS = "ambiguous"    # multiple plausible; surface a chooser, do NOT guess
    NO_MATCH = "no_match"      # nothing plausible


@dataclass
class Resolution:
    status: Status
    entity: Entity | None = None
    candidates: list[Entity] = field(default_factory=list)
    confidence: float = 0.0
    rationale: str = ""


# Below this, prefer AMBIGUOUS over a confident (possibly wrong) pop on the lens.
CONFIDENCE_THRESHOLD = 0.6


def resolve(
    store: EntityStore,
    mention: str,
    context: str = "",
    kind: str = "person",
    *,
    embedder=None,
) -> Resolution:
    hits = store.find_by_name(mention, kind)

    # Tier 1 — exactly one exact/alias hit: done.
    if len(hits) == 1:
        return Resolution(Status.RESOLVED, entity=hits[0], confidence=0.95,
                          rationale="unique exact/alias match")

    # Tier 2 — multiple hits: the real disambiguation problem.
    if len(hits) > 1:
        ranked = _disambiguate(store, hits, context, embedder)
        top, score = ranked[0]
        if score >= CONFIDENCE_THRESHOLD and (len(ranked) == 1 or score - ranked[1][1] > 0.15):
            return Resolution(Status.RESOLVED, entity=top, candidates=hits,
                              confidence=score, rationale="disambiguated by context")
        return Resolution(Status.AMBIGUOUS, candidates=hits, confidence=score,
                          rationale=f"{len(hits)} candidates; context insufficient")

    # Tier 3 — no exact hit. TODO: fuzzy name match (rapidfuzz / embedding) before NO_MATCH.
    return Resolution(Status.NO_MATCH, rationale="no exact/alias match")


def _disambiguate(store, candidates: list[Entity], context: str, embedder) -> list[tuple[Entity, float]]:
    """Rank candidates against context. TODO: real implementation.

    Intended signals (combine into a score):
      1. Graph proximity — do entities named in `context` connect (via edges) to the
         candidate? (e.g. "the party" event the candidate attended).
      2. Embedding similarity between `context` and each candidate's profile blurb
         (use `embedder` when provided; skip when None so offline tests still run).
      3. Attribute keyword overlap (org/place/topic mentioned in context).

    Current placeholder: keyword overlap between context and each candidate's
    attribute values — enough to be deterministic and testable; NOT production-grade.
    """
    ctx = context.lower()
    scored: list[tuple[Entity, float]] = []
    for e in candidates:
        blob = " ".join(str(v) for v in e.attributes.values()).lower()
        tokens = {t for t in blob.split() if len(t) > 3}
        overlap = sum(1 for t in tokens if t in ctx)
        scored.append((e, min(0.5 + 0.1 * overlap, 0.99) if overlap else 0.3))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored
