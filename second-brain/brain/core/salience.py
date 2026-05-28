"""Salience scoring — "should I surface this chunk on the lens?"

The G2 reference doc flags this as the unsolved research problem: ambient
transcripts produce thousands of chunks; only a handful are worth flashing
on the HUD. This module gives the retrieval surface a single, calibrated
0-1 score per chunk so it can threshold.

Signals (independent, combined via noisy-OR so any one can clear the bar):
  - tfidf:      domain-specific TF-IDF score against the chunk corpus
                (built on demand from the index; cached on the BrainIndex)
  - recency:    exponential decay from chunk.created_at; tunable half-life
  - entity:     density of entity_tags relative to chunk length
  - layer:      reasoning / decision / workaround weighted higher than artifact
                (Context-Graph framing: tribal knowledge > finished outputs)
  - context_hit: optional boost when current context tokens overlap with chunk

The default is offline + deterministic so it can run alongside the `fake`
embedder. Tunables live as module constants; tests pin the math.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable

# --- tunables -----------------------------------------------------------------

DEFAULT_HALF_LIFE_DAYS = 30
LAYER_WEIGHT = {
    "reasoning": 0.85,
    "decision": 0.75,
    "workaround": 0.7,
    "artifact": 0.35,
}
TFIDF_CAP = 8.0
ENTITY_PER_100_CHARS_CAP = 3.0
CONTEXT_OVERLAP_CAP = 4

_WORD = re.compile(r"[a-z0-9][a-z0-9'\-]+")
_STOPWORDS = frozenset({
    "the", "and", "for", "with", "from", "that", "this", "was", "were", "are",
    "had", "has", "have", "but", "you", "your", "their", "they", "them", "our",
    "his", "her", "him", "she", "who", "what", "when", "where", "why", "how",
    "about", "into", "over", "under", "between", "before", "after", "last",
    "next", "year", "month", "week", "day", "today", "tomorrow", "yesterday",
})


# --- public API ---------------------------------------------------------------

@dataclass
class SalienceBreakdown:
    """Per-signal contribution to the score, for debugging / surface tuning."""
    tfidf: float = 0.0
    recency: float = 0.0
    entity: float = 0.0
    layer: float = 0.0
    context: float = 0.0
    total: float = 0.0


def score_chunk(
    chunk: dict,
    *,
    idf: dict[str, float] | None = None,
    avg_doc_len: float = 100.0,
    context_tokens: set[str] | None = None,
    now: datetime | None = None,
    half_life_days: float = DEFAULT_HALF_LIFE_DAYS,
) -> SalienceBreakdown:
    """Score one chunk dict (as returned by BrainIndex.query / .all).

    Pass `idf` from `build_idf(corpus)` to get the TF-IDF signal; omit for a
    zero TF-IDF score (cheap mode). Pass `context_tokens` from the current
    conversation to bias toward chunks that overlap it.
    """
    text = chunk.get("text", "") or ""
    text_tokens = _tokens(text)

    tfidf_score = _tfidf_signal(text_tokens, idf) if idf else 0.0
    recency_score = _recency_signal(chunk.get("created_at"), now, half_life_days)
    entity_score = _entity_density_signal(chunk.get("entity_tags") or [], len(text))
    layer_score = LAYER_WEIGHT.get(chunk.get("layer") or "artifact", 0.35)
    context_score = (
        _context_signal(text_tokens, context_tokens)
        if context_tokens else 0.0
    )

    total = _noisy_or([tfidf_score, recency_score, entity_score, layer_score, context_score])
    return SalienceBreakdown(
        tfidf=round(tfidf_score, 4),
        recency=round(recency_score, 4),
        entity=round(entity_score, 4),
        layer=round(layer_score, 4),
        context=round(context_score, 4),
        total=round(total, 4),
    )


def build_idf(corpus: Iterable[str]) -> dict[str, float]:
    """Inverse-document-frequency over a chunk corpus. Cache and re-use."""
    df: dict[str, int] = {}
    n_docs = 0
    for text in corpus:
        n_docs += 1
        for tok in _tokens(text):
            df[tok] = df.get(tok, 0) + 1
    if n_docs == 0:
        return {}
    return {tok: math.log((n_docs + 1) / (c + 1)) + 1.0 for tok, c in df.items()}


def filter_by_salience(
    chunks: list[dict],
    *,
    threshold: float = 0.6,
    idf: dict[str, float] | None = None,
    context_tokens: set[str] | None = None,
    now: datetime | None = None,
) -> list[tuple[dict, SalienceBreakdown]]:
    """Convenience: score + threshold + sort descending."""
    out: list[tuple[dict, SalienceBreakdown]] = []
    for c in chunks:
        b = score_chunk(c, idf=idf, context_tokens=context_tokens, now=now)
        if b.total >= threshold:
            out.append((c, b))
    out.sort(key=lambda x: x[1].total, reverse=True)
    return out


# --- signal helpers -----------------------------------------------------------

def _tfidf_signal(text_tokens: set[str], idf: dict[str, float]) -> float:
    if not text_tokens or not idf:
        return 0.0
    score = sum(idf.get(tok, 0.0) for tok in text_tokens)
    # squash to 0-1
    return min(score / TFIDF_CAP, 1.0)


def _recency_signal(
    created_at: str | None, now: datetime | None, half_life_days: float
) -> float:
    if not created_at:
        return 0.0
    try:
        if isinstance(created_at, str):
            ts = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        else:
            ts = created_at
    except ValueError:
        return 0.0
    now = now or datetime.now(timezone.utc)
    if ts > now:
        return 1.0
    age_days = (now - ts).total_seconds() / 86400.0
    return 0.5 ** (age_days / max(half_life_days, 1.0))


def _entity_density_signal(entity_tags: list[str], text_len: int) -> float:
    if not entity_tags or text_len == 0:
        return 0.0
    per_100 = len(entity_tags) * 100.0 / max(text_len, 1)
    return min(per_100 / ENTITY_PER_100_CHARS_CAP, 1.0)


def _context_signal(text_tokens: set[str], context_tokens: set[str] | None) -> float:
    if not text_tokens or not context_tokens:
        return 0.0
    overlap = len(text_tokens & context_tokens)
    if overlap == 0:
        return 0.0
    return 1.0 - math.exp(-overlap / CONTEXT_OVERLAP_CAP)


def _noisy_or(signals: list[float]) -> float:
    p = 1.0
    for s in signals:
        p *= 1.0 - max(0.0, min(1.0, s))
    return 1.0 - p


def _tokens(text: str) -> set[str]:
    return {m.group(0) for m in _WORD.finditer(text.lower())} - _STOPWORDS
