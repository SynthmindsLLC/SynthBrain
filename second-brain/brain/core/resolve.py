"""Entity resolution — the make-or-break piece for the dossier.

resolve() turns a heard/seen mention ("Jeff") plus surrounding context
("...the party last fall...") into the right entity WITH a confidence. A wrong
dossier on the lens is worse than no dossier, so this MUST refuse to guess: below
threshold, we return AMBIGUOUS and let the surface ask "which Jeff?".

Algorithm (cheap -> expensive):
  Tier 1: exact / alias match (case-insensitive) on name. One hit -> done.
  Tier 2: multiple hits -> rank candidates by combined signal:
            - graph proximity (does context mention entities the candidate is
              connected to in the graph? -- highest-weight signal),
            - attribute keyword overlap (org, title, role, note words present
              in context),
            - embedding similarity between context and a candidate profile blurb
              (only when an embedder is supplied; skipped offline).
  Tier 3: no exact hit -> optional fuzzy name match; else NO_MATCH. Never guess.

Hard rules:
  - Top score must exceed CONFIDENCE_THRESHOLD AND beat runner-up by MARGIN,
    or we return AMBIGUOUS.
  - Pure-Python deterministic fallback works with the `fake` embedder so the
    tests run offline; the LLM/embedding path is opt-in.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from enum import Enum

from .entities import Entity, EntityStore

CONFIDENCE_THRESHOLD = 0.6
MARGIN = 0.12
DISTINCT_DECAY = 0.7
SHARED_DECAY = 0.25
EMBED_FLOOR = 0.4  # cosine sim below this contributes nothing

_WORD = re.compile(r"[a-z0-9][a-z0-9'\-]+")
_STOPWORDS = frozenset({
    "the", "and", "for", "with", "from", "that", "this", "was", "were", "are",
    "had", "has", "have", "but", "you", "your", "their", "they", "them", "our",
    "his", "her", "him", "she", "who", "what", "when", "where", "why", "how",
    "about", "into", "over", "under", "between", "before", "after", "last",
    "next", "year", "month", "week", "day", "today", "tomorrow", "yesterday",
})


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
    scores: list[tuple[str, float]] = field(default_factory=list)


def resolve(
    store: EntityStore,
    mention: str,
    context: str = "",
    kind: str = "person",
    *,
    embedder=None,
) -> Resolution:
    hits = store.find_by_name(mention, kind)

    if len(hits) == 1:
        return Resolution(
            Status.RESOLVED,
            entity=hits[0],
            confidence=0.95,
            rationale="unique exact/alias match",
            scores=[(hits[0].id, 0.95)],
        )

    if len(hits) > 1:
        ranked = _disambiguate(store, hits, context, embedder)
        scores = [(e.id, s) for e, s in ranked]
        top, top_score = ranked[0]
        runner_up = ranked[1][1] if len(ranked) > 1 else 0.0
        if top_score >= CONFIDENCE_THRESHOLD and (top_score - runner_up) >= MARGIN:
            return Resolution(
                Status.RESOLVED,
                entity=top,
                candidates=hits,
                confidence=top_score,
                rationale=f"disambiguated by context (margin {top_score - runner_up:.2f})",
                scores=scores,
            )
        return Resolution(
            Status.AMBIGUOUS,
            candidates=hits,
            confidence=top_score,
            rationale=f"{len(hits)} candidates; top={top_score:.2f} runner-up={runner_up:.2f}",
            scores=scores,
        )

    return Resolution(Status.NO_MATCH, rationale="no exact/alias match for " + repr(mention))


def _disambiguate(
    store: EntityStore,
    candidates: list[Entity],
    context: str,
    embedder,
) -> list[tuple[Entity, float]]:
    """Combine three independent calibrated signals via noisy-OR.

    Each signal returns a 0-1 confidence that it alone identifies the candidate;
    noisy-OR (1 - prod(1 - p_i)) is the right combiner for independent positives.
    Distinctive tokens (in this candidate's profile but not others') are weighted
    far higher than shared tokens, so org/title hits that uniquely point at one
    candidate can clear the threshold on their own.
    """
    if not context.strip():
        return [(c, 0.0) for c in candidates]

    context_norm = context.lower()
    context_tokens = _tokens(context_norm)
    context_entities = _entities_in_context(store, context_norm)

    profile_tokens = {c.id: _profile_tokens(c) for c in candidates}
    shared = set.intersection(*profile_tokens.values()) if profile_tokens else set()

    embed_scores: dict[str, float] = {}
    if embedder is not None:
        embed_scores = _embedding_scores(candidates, context, embedder)

    scored: list[tuple[Entity, float]] = []
    for cand in candidates:
        g = _graph_proximity(store, cand, context_entities, context_norm)
        distinct = profile_tokens[cand.id] - shared
        a = _attribute_signal(context_tokens, profile_tokens[cand.id], distinct)
        e = _embed_signal(embed_scores.get(cand.id, 0.0)) if embedder else 0.0
        score = _noisy_or((g, a, e))
        scored.append((cand, round(min(max(score, 0.0), 0.99), 4)))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored


def _noisy_or(signals: tuple[float, ...]) -> float:
    """1 - prod(1 - p_i). Clamps inputs to [0, 1] first."""
    p = 1.0
    for s in signals:
        p *= 1.0 - max(0.0, min(1.0, s))
    return 1.0 - p


def _graph_proximity(
    store: EntityStore,
    candidate: Entity,
    context_entities: set[str],
    context_norm: str,
) -> float:
    """Highest-weight signal: does the candidate touch entities named in context?
    Walks 1 hop out; counts hits against entities referenced in `context`.
    Also rewards raw substring hits on neighbor names when the context didn't
    parse cleanly (e.g. "the party" -> "Fall Block Party")."""
    direct_hits = 0
    fuzzy_hits = 0
    neighbors = store.neighbors(candidate.id)
    for _edge, neighbor in neighbors:
        if not neighbor:
            continue
        if neighbor.id in context_entities:
            direct_hits += 1
        elif _name_appears(neighbor, context_norm):
            fuzzy_hits += 1
    if direct_hits == 0 and fuzzy_hits == 0:
        return 0.0
    score = 1.0 - math.exp(-(direct_hits + 0.5 * fuzzy_hits))
    return score


def _profile_tokens(candidate: Entity) -> set[str]:
    """All tokens that could plausibly identify the candidate in context."""
    tokens: set[str] = _tokens(candidate.name.lower())
    for v in candidate.attributes.values():
        tokens |= _tokens(str(v).lower())
    for alias in candidate.aliases:
        tokens |= _tokens(alias.lower())
    return tokens - _STOPWORDS


def _attribute_signal(
    context_tokens: set[str],
    cand_tokens: set[str],
    distinctive_tokens: set[str],
) -> float:
    """Calibrated 0-1 confidence from context-vs-profile token overlap.
    Distinctive hits decay fast (each one adds a lot); shared hits decay slow."""
    if not context_tokens or not cand_tokens:
        return 0.0
    distinct_hits = len(context_tokens & distinctive_tokens)
    shared_hits = len(context_tokens & (cand_tokens - distinctive_tokens))
    if distinct_hits == 0 and shared_hits == 0:
        return 0.0
    return 1.0 - math.exp(-(DISTINCT_DECAY * distinct_hits + SHARED_DECAY * shared_hits))


def _embed_signal(cosine: float) -> float:
    """Squash cosine sim to a calibrated 0-1: ignore below floor, scale above."""
    if cosine < EMBED_FLOOR:
        return 0.0
    return min((cosine - EMBED_FLOOR) / (1.0 - EMBED_FLOOR), 1.0)


def _embedding_scores(candidates: list[Entity], context: str, embedder) -> dict[str, float]:
    """Cosine sim between context vector and each candidate's profile blurb vector.
    Embedder must expose .embed(list[str]) -> list[list[float]]."""
    blurbs = [_profile_blurb(c) for c in candidates]
    vectors = embedder.embed([context, *blurbs])
    ctx_vec = vectors[0]
    out: dict[str, float] = {}
    for cand, vec in zip(candidates, vectors[1:]):
        out[cand.id] = max(0.0, _cosine(ctx_vec, vec))
    return out


def _profile_blurb(entity: Entity) -> str:
    bits = [entity.name]
    for key in ("title", "org", "role", "location", "note", "date"):
        v = entity.attributes.get(key)
        if v:
            bits.append(str(v))
    bits.extend(entity.aliases)
    return " ".join(bits)


def _entities_in_context(store: EntityStore, context_norm: str) -> set[str]:
    """Identify entity IDs whose name/alias appears in the context string."""
    if not context_norm.strip():
        return set()
    found: set[str] = set()
    for entity in store.all_entities():
        if _name_appears(entity, context_norm):
            found.add(entity.id)
    return found


def _name_appears(entity: Entity, context_norm: str) -> bool:
    names = [entity.name.lower(), *(a.lower() for a in entity.aliases)]
    for n in names:
        if len(n) < 4:
            continue
        if n in context_norm:
            return True
    return False


def _tokens(text: str) -> set[str]:
    return {m.group(0) for m in _WORD.finditer(text)} - _STOPWORDS


def _cosine(a, b) -> float:
    if not a or not b:
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)
