"""Salience tests — every signal in isolation + the combined threshold path."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from brain.core.salience import (
    LAYER_WEIGHT,
    SalienceBreakdown,
    build_idf,
    filter_by_salience,
    score_chunk,
)

NOW = datetime(2026, 5, 28, tzinfo=timezone.utc)


def _chunk(text: str, *, layer="artifact", entity_tags=None, created_at=None) -> dict:
    return {
        "text": text,
        "layer": layer,
        "entity_tags": entity_tags or [],
        "created_at": created_at or NOW.isoformat(),
    }


# ----- recency --------------------------------------------------------------

def test_recency_decays_with_age():
    fresh = _chunk("x", created_at=NOW.isoformat())
    old = _chunk("x", created_at=(NOW - timedelta(days=180)).isoformat())
    s_fresh = score_chunk(fresh, now=NOW)
    s_old = score_chunk(old, now=NOW)
    assert s_fresh.recency > s_old.recency
    assert s_fresh.recency >= 0.99
    assert s_old.recency <= 0.10  # 6 half-lives -> ~0.016


def test_recency_handles_missing_timestamp():
    c = _chunk("x"); c["created_at"] = None
    b = score_chunk(c, now=NOW)
    assert b.recency == 0.0


# ----- layer ----------------------------------------------------------------

def test_layer_weights_match_tribal_knowledge_priority():
    """Reasoning > decision > workaround > artifact (matches Context-Graph framing)."""
    assert LAYER_WEIGHT["reasoning"] > LAYER_WEIGHT["decision"]
    assert LAYER_WEIGHT["decision"] > LAYER_WEIGHT["workaround"]
    assert LAYER_WEIGHT["workaround"] > LAYER_WEIGHT["artifact"]
    r = score_chunk(_chunk("x", layer="reasoning"), now=NOW)
    a = score_chunk(_chunk("x", layer="artifact"), now=NOW)
    assert r.layer > a.layer


# ----- entity density --------------------------------------------------------

def test_entity_density_rewards_tagged_chunks():
    dense = _chunk("Brief text", entity_tags=["Jeff", "Wes", "PBTV"])
    sparse = _chunk("A long text " * 50, entity_tags=["Jeff"])
    b_dense = score_chunk(dense, now=NOW)
    b_sparse = score_chunk(sparse, now=NOW)
    assert b_dense.entity > b_sparse.entity


def test_entity_density_zero_when_no_tags():
    assert score_chunk(_chunk("x"), now=NOW).entity == 0.0


# ----- tfidf ----------------------------------------------------------------

def test_tfidf_uses_provided_idf():
    corpus = [
        "the maritime conservation roadmap",
        "the lunch meeting agenda",
        "the lunch and the agenda again",
    ]
    idf = build_idf(corpus)
    # rare tokens (maritime, conservation, roadmap) should have higher idf than 'lunch'
    assert idf["maritime"] > idf["lunch"]
    # chunks with rarer tokens score higher
    rare = score_chunk(_chunk("maritime conservation roadmap"), idf=idf, now=NOW)
    common = score_chunk(_chunk("the lunch agenda"), idf=idf, now=NOW)
    assert rare.tfidf > common.tfidf


def test_tfidf_zero_without_idf():
    assert score_chunk(_chunk("rare tokens here"), now=NOW).tfidf == 0.0


# ----- context_hit ----------------------------------------------------------

def test_context_overlap_boosts_score():
    # Use an older chunk so the recency signal doesn't saturate the noisy-OR
    # at 1.0 (which would hide the context contribution).
    old_ts = (NOW - timedelta(days=200)).isoformat()
    c = _chunk("Jeff Torres maritime conservation lunch", created_at=old_ts)
    no_ctx = score_chunk(c, now=NOW)
    with_ctx = score_chunk(c, context_tokens={"maritime", "lunch"}, now=NOW)
    assert with_ctx.context > 0
    assert with_ctx.total > no_ctx.total


# ----- combined / threshold -------------------------------------------------

def test_filter_by_salience_orders_descending_and_thresholds():
    chunks = [
        _chunk("recent reasoning about Jeff",
               layer="reasoning",
               entity_tags=["Jeff", "Wes"],
               created_at=NOW.isoformat()),
        _chunk("an old artifact with no tags",
               layer="artifact",
               created_at=(NOW - timedelta(days=365)).isoformat()),
    ]
    kept = filter_by_salience(chunks, threshold=0.5, now=NOW)
    assert len(kept) >= 1
    assert kept[0][0]["text"].startswith("recent reasoning")


def test_combined_score_can_exceed_any_single_signal():
    """noisy-OR property: multiple weak signals can clear a threshold one can't."""
    c = _chunk(
        "lunch meeting summary",
        layer="reasoning",
        entity_tags=["A", "B"],
        created_at=NOW.isoformat(),
    )
    b = score_chunk(c, now=NOW)
    assert b.total >= max(b.recency, b.layer, b.entity)


def test_breakdown_shape():
    b = score_chunk(_chunk("x"), now=NOW)
    assert isinstance(b, SalienceBreakdown)
    assert 0.0 <= b.total <= 1.0
