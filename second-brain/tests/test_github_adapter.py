"""GitHub adapter tests — patch _get so no network is hit."""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from brain.adapters.github_adapter import GitHubAdapter, GitHubAuthError
from brain.core.checkpoint import CheckpointStore


SAMPLE_ITEMS = [
    {
        "title": "Pick a chunking strategy",
        "body": "Tradeoffs:\n- fixed-size: cheap, ignores structure\n- header-aware: +9% recall",
        "state": "closed",
        "labels": [{"name": "decision"}, {"name": "phase-0"}],
        "user": {"login": "wes"},
        "html_url": "https://github.com/synthmindsllc/synthbrain/issues/12",
        "created_at": "2026-04-01T10:00:00Z",
        "updated_at": "2026-04-03T11:00:00Z",
    },
    {
        "title": "Add resolve()",
        "body": "Noisy-OR over graph proximity + distinctive attr.",
        "state": "merged",
        "labels": [],
        "user": {"login": "wes"},
        "html_url": "https://github.com/synthmindsllc/synthbrain/pull/27",
        "created_at": "2026-05-15T10:00:00Z",
        "updated_at": "2026-05-18T11:00:00Z",
    },
]

SAMPLE_COMMENTS = {
    ("synthmindsllc", "synthbrain", 12): [
        {"user": {"login": "wes"}, "body": "Going with header-aware."},
        {"user": {"login": "reviewer"}, "body": "+1, matches the research."},
    ],
    ("synthmindsllc", "synthbrain", 27): [
        {"user": {"login": "wes"}, "body": "Tests included."},
    ],
}


def _make_fake_get(items, *, whoami="wes"):
    """Return a fake _get matching paths the adapter will hit."""
    page_calls = {"n": 0}

    def fake_get(self, path, params):  # noqa: ARG001 - signature compat
        if path == "/user":
            return {"login": whoami}
        if path == "/search/issues":
            page = params.get("page", 1)
            if page > 1:
                return {"items": []}
            return {"items": items}
        if path.startswith("/repos/") and path.endswith("/comments"):
            # /repos/<owner>/<repo>/issues/<n>/comments
            _, _, owner, repo, _, number_str, _ = path.split("/")
            number = int(number_str)
            return SAMPLE_COMMENTS.get((owner, repo, number), [])
        raise AssertionError(f"unexpected path {path}")

    return fake_get


@pytest.fixture(autouse=True)
def _env(monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "ghp_test")
    monkeypatch.setenv("GITHUB_USERNAME", "wes")


def test_raises_without_token(monkeypatch):
    monkeypatch.delenv("GITHUB_TOKEN")
    with pytest.raises(GitHubAuthError):
        GitHubAdapter()


def test_emits_one_doc_per_issue_or_pr_with_comments():
    with patch.object(GitHubAdapter, "_get", new=_make_fake_get(SAMPLE_ITEMS)):
        docs = list(GitHubAdapter().fetch())
    assert len(docs) == 2
    by_id = {d.source_id: d for d in docs}
    assert "synthmindsllc/synthbrain#12" in by_id
    assert "synthmindsllc/synthbrain#27" in by_id
    issue = by_id["synthmindsllc/synthbrain#12"]
    assert issue.meta["kind"] == "issues"
    assert issue.meta["labels"] == ["decision", "phase-0"]
    assert "header-aware" in issue.text
    assert "+1, matches the research" in issue.text  # comments included
    assert set(issue.meta["participants"]) == {"wes", "reviewer"}


def test_checkpoint_advances_to_latest_updated_at():
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch.object(GitHubAdapter, "_get", new=_make_fake_get(SAMPLE_ITEMS)):
            list(GitHubAdapter(checkpoint_db=cp_db).fetch())
        saved = CheckpointStore(cp_db).get("github")
        assert saved == "2026-05-18T11:00:00Z"


def test_subsequent_run_adds_updated_filter_to_search():
    captured: list[dict] = []

    def fake_get_capture(self, path, params):
        if path == "/user":
            return {"login": "wes"}
        if path == "/search/issues":
            captured.append(dict(params))
            return {"items": []}
        return []

    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        CheckpointStore(cp_db).set("github", "2026-05-01T00:00:00Z")
        with patch.object(GitHubAdapter, "_get", new=fake_get_capture):
            list(GitHubAdapter(checkpoint_db=cp_db).fetch())
        assert captured
        q = captured[0]["q"]
        assert "involves:wes" in q
        assert "updated:>2026-05-01T00:00:00Z" in q


def test_long_body_is_truncated():
    big_body = "x" * 50_000
    item = dict(SAMPLE_ITEMS[0])
    item["body"] = big_body
    with patch.object(GitHubAdapter, "_get",
                      new=_make_fake_get([item])):
        docs = list(GitHubAdapter().fetch())
    assert "…(truncated)" in docs[0].text
    assert len(docs[0].text) < 25_000


def test_kind_is_pull_for_pr_urls():
    with patch.object(GitHubAdapter, "_get", new=_make_fake_get(SAMPLE_ITEMS)):
        docs = list(GitHubAdapter().fetch())
    pr = next(d for d in docs if d.source_id == "synthmindsllc/synthbrain#27")
    assert pr.meta["kind"] == "pull"
