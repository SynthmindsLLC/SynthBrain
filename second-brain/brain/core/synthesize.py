"""LLM hooks: layer classification + dossier bullet synthesis.

Both are injected, never imported by core code. Default implementations are
deterministic / heuristic so the brain runs offline (`fake` embedder, no API
keys). The LLM paths are opt-in upgrades.

Two surfaces:
  - classify_layer_llm(text) -> "artifact|decision|reasoning|workaround"
    Sharper than the regex heuristic in tag.py for ambiguous text.
  - synthesize_dossier(person, event, chunks) -> list[str]
    Compresses N chunks into 3-5 HUD-budget bullets.

Both call Anthropic Haiku via the Messages API when ANTHROPIC_API_KEY is
present; otherwise they raise (caller is expected to fall back to the
heuristic / first-sentence path). No model is downloaded; no fallback to a
weaker LLM — explicit > clever.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Iterable

from .entities import Entity

ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = "claude-haiku-4-5-20251001"
ANTHROPIC_VERSION = "2023-06-01"

LAYER_VALUES = ("artifact", "decision", "reasoning", "workaround")

LAYER_PROMPT = """\
Classify this text into exactly ONE Context-Graph layer:
- "artifact": a final output / deliverable / asset (a document, a screenshot, a working spec).
- "decision": a choice was made (we picked X, we're going with Y, locked the approach).
- "reasoning": the WHY — tradeoffs considered, rationale, why-not-other-options.
- "workaround": a hack/bypass/temporary fix used because the right path is blocked.

Reply with ONLY one word, lowercase: artifact, decision, reasoning, or workaround.

Text:
\"\"\"
{text}
\"\"\"
"""

DOSSIER_PROMPT = """\
You are surfacing a dossier card on a smart-glasses HUD. Hard constraints:
- 3 to 5 bullets, no more.
- Each bullet <= 8 words.
- Glanceable: facts about THIS person (and event if given), not generic.
- Don't repeat the person's name in bullets.
- No emojis, no markdown, no surrounding quotes.

Person: {person_name}{event_line}

Excerpts that mention them:
{excerpts}

Output: one bullet per line, no leading "-" or numbering.
"""


class SynthesizeError(RuntimeError):
    pass


def _post_anthropic(body: dict, *, timeout: int = 20) -> dict:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise SynthesizeError("ANTHROPIC_API_KEY not set; LLM path unavailable.")
    req = urllib.request.Request(
        ANTHROPIC_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "x-api-key": key,
            "anthropic-version": ANTHROPIC_VERSION,
            "content-type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise SynthesizeError(
            f"Anthropic API error {e.code}: {e.read().decode('utf-8', 'replace')[:200]}"
        ) from e
    except urllib.error.URLError as e:
        raise SynthesizeError(f"Anthropic network error: {e.reason}") from e


def _extract_text(payload: dict) -> str:
    content = payload.get("content") or []
    for block in content:
        if isinstance(block, dict) and block.get("type") == "text":
            return (block.get("text") or "").strip()
    return ""


def classify_layer_llm(text: str, *, model: str = DEFAULT_MODEL) -> str:
    """Sharper layer classifier. Returns one of LAYER_VALUES.
    Caller catches SynthesizeError and falls back to the heuristic."""
    snippet = text[:1500]
    body = {
        "model": model,
        "max_tokens": 6,
        "messages": [{"role": "user", "content": LAYER_PROMPT.format(text=snippet)}],
    }
    payload = _post_anthropic(body)
    raw = _extract_text(payload).strip().lower().strip(".,'\"")
    if raw in LAYER_VALUES:
        return raw
    # If model returned a sentence, pick the first known token.
    for token in raw.split():
        token = token.strip(".,'\"")
        if token in LAYER_VALUES:
            return token
    raise SynthesizeError(f"unexpected layer label from LLM: {raw!r}")


def synthesize_dossier(
    person: Entity,
    event: Entity | None,
    chunks: Iterable[dict],
    *,
    model: str = DEFAULT_MODEL,
    max_excerpt_chars: int = 600,
) -> list[str]:
    """Default `synthesize` hook for dossier(). Compresses chunks -> HUD bullets."""
    excerpts = []
    for i, c in enumerate(chunks, 1):
        text = (c.get("text") or "").strip().replace("\n", " ")
        if not text:
            continue
        excerpts.append(f"[{i}] {text[:max_excerpt_chars]}")
        if len(excerpts) >= 5:
            break
    if not excerpts:
        return []
    event_line = f" / Event: {event.name}" if event else ""
    prompt = DOSSIER_PROMPT.format(
        person_name=person.name,
        event_line=event_line,
        excerpts="\n\n".join(excerpts),
    )
    body = {
        "model": model,
        "max_tokens": 240,
        "messages": [{"role": "user", "content": prompt}],
    }
    payload = _post_anthropic(body)
    text = _extract_text(payload)
    bullets = [
        line.lstrip("-•* ").rstrip(".").strip()
        for line in text.splitlines()
        if line.strip()
    ]
    return bullets[:5]
