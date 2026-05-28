"""Smoke test for the spine. Runs offline with the fake embedder.

    pip install pytest && pytest -q
"""

import tempfile
from pathlib import Path

from brain.adapters.mem_adapter import MemAdapter
from brain.core.embed import get_embedder
from brain.core.index import BrainIndex
from brain.core.pipeline import ingest


def _build_index(tmp: Path) -> BrainIndex:
    export = tmp / "export"
    export.mkdir()
    (export / "moa.md").write_text(
        "# PBTV MOA\n\n## Key Decisions\n- Locked a 70/30 plant consignment split.\n"
        "\n## Reasoning\nWe chose 70/30 because Monica carries the storefront risk.\n",
        encoding="utf-8",
    )
    idx = BrainIndex(str(tmp / "idx"), get_embedder("fake"))
    n = ingest(idx, MemAdapter(str(export)).fetch())
    assert n > 0
    return idx


def test_ingest_and_query():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        idx = _build_index(tmp)
        assert idx.count() >= 2

        hits = idx.query("consignment split terms", k=3)
        assert hits, "expected at least one match"
        assert any("70/30" in h["text"] for h in hits)


def test_tribal_knowledge_distinguished_from_artifact():
    # The valuable property the spike proves: judgment/reasoning content gets a
    # non-artifact layer. The exact decision-vs-reasoning call is intentionally
    # left to the Phase-2 LLM classifier — the heuristic fires on "chose" before
    # "because", which is precisely the ambiguity that motivates the upgrade.
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        idx = _build_index(tmp)
        hits = idx.query("why 70/30 Monica storefront risk", k=5)
        monica = [h for h in hits if "Monica" in h["text"]]
        assert monica, "expected the reasoning chunk to be retrievable"
        assert monica[0]["layer"] in ("decision", "reasoning", "workaround"), (
            "judgment content must be distinguished from plain artifacts"
        )


def test_project_tagging():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        idx = _build_index(tmp)
        pbtv = idx.query("split", project="pbtv", k=5)
        assert pbtv, "expected pbtv-tagged chunks"
