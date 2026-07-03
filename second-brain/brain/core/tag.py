"""Two-pass tagging, applied at ingest.

Pass 1 (cheap, deterministic): project wing + entities.
Pass 2 (the valuable one): Context-Graph layer — artifact|decision|reasoning|workaround.

The spike uses heuristics so it runs offline. Both passes are deliberately
isolated functions so you can replace either with an LLM/NER call in Phase 2
without touching the pipeline. The `classify_layer` heuristic is the obvious
first thing to upgrade to a small classifier — see TODO.
"""

from __future__ import annotations

import re

# Wes's project wings. Keyword -> canonical #project tag. Extend freely.
PROJECT_KEYWORDS: dict[str, str] = {
    "pbtv": "pbtv",
    "plants by the village": "pbtv",
    "olde mistick": "pbtv",
    "monica": "pbtv",
    "lady cove": "lady-cove",
    "haran": "lady-cove",
    "panasoffkee": "lady-cove",
    "vitaluve": "vitaluve",
    "milsbo": "vitaluve",
    "conservatory": "vitaluve",
    "synthminds": "synthminds",
    "synthos": "synthminds",
    "phytosynth": "phytosynth",
    "navy": "navy-va",
    "va ": "navy-va",
    "transition": "navy-va",
    # Extended 2026-07-02 for bulk historical ingest (union of tag sets found in
    # the vault-era tagging schema doc + active projects; additive only — safe,
    # multi-char substrings to avoid false positives).
    "synaptic labs": "synaptic-labs",
    "synaptic-labs": "synaptic-labs",
    "synthsidian": "synthsidian",
    "jasmmm": "jasmmm",
    "supply chain game": "jasmmm",
    "verizon": "verizon",
    "anvl": "anvl",
    "synthbrain": "synthbrain",
    "second brain": "synthbrain",
    "even realities": "synthbrain",
}

_DECISION = re.compile(r"\b(decided|chose|chosen|selected|opted|locked|approved|will use|going with)\b", re.I)
_REASONING = re.compile(r"\b(because|rationale|reason|trade-?off|tradeoff|the why|in order to|so that)\b", re.I)
_WORKAROUND = re.compile(r"\b(workaround|work around|hack|instead of|bypass|to get around|kludge)\b", re.I)

# Crude entity heuristic: multi-word Capitalized spans + known proper nouns.
# TODO(phase2): replace with spaCy NER or a small LLM extraction call.
_CAP_SPAN = re.compile(r"\b([A-Z][a-zA-Z0-9]+(?:\s+[A-Z][a-zA-Z0-9]+){0,3})\b")
_STOP_CAPS = {"The", "This", "That", "These", "Those", "It", "I", "We", "A", "An"}


def tag_project(text: str) -> list[str]:
    low = text.lower()
    hits = {tag for kw, tag in PROJECT_KEYWORDS.items() if kw in low}
    return sorted(hits)


def tag_entities(text: str, limit: int = 8) -> list[str]:
    seen: list[str] = []
    for m in _CAP_SPAN.finditer(text):
        span = m.group(1).strip()
        first = span.split()[0]
        if first in _STOP_CAPS:
            continue
        if span not in seen:
            seen.append(span)
        if len(seen) >= limit:
            break
    return seen


def classify_layer(text: str) -> str:
    """Pass-2. Heuristic for the spike. TODO(phase2): swap for an LLM classifier
    prompted with the Context-Graph definitions for sharper precision."""
    if _WORKAROUND.search(text):
        return "workaround"
    if _DECISION.search(text):
        return "decision"
    if _REASONING.search(text):
        return "reasoning"
    return "artifact"
