"""GitHub adapter — issues, PRs, and comments you authored or commented on.

Pure "tribal knowledge" pipeline: the *why* behind every architectural
decision Wes has shipped lives in PR descriptions, issue threads, and
review comments. Across repos, across orgs.

Uses GitHub REST API v3 with a personal access token (PAT) in
GITHUB_TOKEN. The token's repo scope determines what we can read:
  - `public_repo` covers all your public activity (issues, PRs, comments)
  - `repo` adds private repos you have access to

Authentication is the user's own PAT; this adapter intentionally does
NOT use the MCP scope (locked to synthmindsllc/synthbrain). The user's
broader GitHub activity is a separate axis.

Incremental sync:
  - First run: search for items authored by or involving the user, paged
    with cursor; capture the latest issue update_at as the watermark.
  - Subsequent runs: same search with `updated:>WATERMARK` filter so we
    only fetch what changed.
  - Comments on each item are fetched per-item (one API call each); the
    rate limit gates total volume more than the search.

Each issue/PR becomes ONE RawDoc carrying:
  - title, body, state (open|closed|merged), labels
  - all comments in chronological order
  - participant names

source_id = `<owner>/<repo>#<number>` so re-runs upsert deterministically.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "github"
GH_API = "https://api.github.com"
DEFAULT_PER_PAGE = 50
DEFAULT_TIMEOUT = 30
MAX_BODY_CHARS = 20_000          # truncate runaway PR descriptions


class GitHubAuthError(RuntimeError):
    pass


class GitHubAPIError(RuntimeError):
    pass


class GitHubAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        *,
        token: str | None = None,
        username: str | None = None,
        checkpoint_db: str | None = None,
        per_page: int = DEFAULT_PER_PAGE,
        max_items: int | None = None,
        include_comments: bool = True,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.token = token or os.environ.get("GITHUB_TOKEN")
        if not self.token:
            raise GitHubAuthError(
                "GITHUB_TOKEN not set. Create a fine-grained PAT at "
                "github.com/settings/personal-access-tokens with repo read "
                "scope and put it in .env.local."
            )
        self.username = username or os.environ.get("GITHUB_USERNAME") or self._whoami()
        if not self.username:
            raise GitHubAuthError("Unable to resolve GitHub username from token.")
        self.checkpoint_db = checkpoint_db
        self.per_page = max(1, min(per_page, 100))
        self.max_items = max_items
        self.include_comments = include_comments
        self.timeout = timeout

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = cp.get(self.name) if cp else None
        newest = watermark

        emitted = 0
        for item in self._iter_items(watermark):
            doc = self._item_to_doc(item)
            if doc is None:
                continue
            yield doc
            emitted += 1
            updated = item.get("updated_at")
            if updated and (newest is None or updated > newest):
                newest = updated
            if self.max_items and emitted >= self.max_items:
                break

        if cp and newest:
            cp.set(self.name, newest)

    # ---- queries ------------------------------------------------------

    def _whoami(self) -> str | None:
        try:
            payload = self._get("/user", {})
            return payload.get("login")
        except (GitHubAuthError, GitHubAPIError):
            return None

    def _iter_items(self, watermark: str | None) -> Iterable[dict]:
        """Search issues + PRs that involve the user."""
        # 'involves' covers author, assignee, mentioned, commenter
        q_parts = [f"involves:{self.username}"]
        if watermark:
            q_parts.append(f"updated:>{watermark}")
        query = " ".join(q_parts)
        page = 1
        while True:
            payload = self._get(
                "/search/issues",
                {"q": query, "per_page": self.per_page, "page": page,
                 "sort": "updated", "order": "asc"},
            )
            items = payload.get("items") or []
            if not items:
                return
            for item in items:
                yield item
            if len(items) < self.per_page:
                return
            page += 1
            # GitHub caps search at 1000 results total
            if page * self.per_page > 1000:
                return

    def _fetch_comments(self, owner: str, repo: str, number: int) -> list[dict]:
        try:
            return self._get(
                f"/repos/{owner}/{repo}/issues/{number}/comments",
                {"per_page": self.per_page},
            )
        except GitHubAPIError:
            return []

    def _item_to_doc(self, item: dict) -> RawDoc | None:
        url = item.get("html_url") or ""
        if not url:
            return None
        # html_url shape: https://github.com/<owner>/<repo>/issues|pull/<n>
        try:
            _, _, _, owner, repo, kind, number_str = url.rsplit("/", 6)
            number = int(number_str)
        except (ValueError, IndexError):
            return None

        title = (item.get("title") or "").strip()
        body = (item.get("body") or "").strip()
        if len(body) > MAX_BODY_CHARS:
            body = body[:MAX_BODY_CHARS] + "\n\n…(truncated)"
        state = item.get("state") or ""
        labels = [l.get("name", "") for l in (item.get("labels") or []) if isinstance(l, dict)]
        author = ((item.get("user") or {}).get("login")) or "unknown"

        body_lines = [
            f"# {title}",
            f"_{kind.upper()}_  {owner}/{repo}#{number}  • state: {state}",
            f"_Author:_ {author}",
        ]
        if labels:
            body_lines.append(f"_Labels:_ {', '.join(labels)}")
        body_lines.append("")
        body_lines.append(body or "(no description)")

        participants = {author}

        if self.include_comments:
            comments = self._fetch_comments(owner, repo, number)
            for c in comments:
                cuser = ((c.get("user") or {}).get("login")) or "unknown"
                ctext = (c.get("body") or "").strip()
                if not ctext:
                    continue
                participants.add(cuser)
                body_lines.append("")
                body_lines.append(f"**{cuser}:** {ctext}")

        created = _parse_ts(item.get("created_at"))
        updated = _parse_ts(item.get("updated_at")) or created
        return RawDoc(
            text="\n".join(body_lines).strip(),
            source=ADAPTER_NAME,
            source_id=f"{owner}/{repo}#{number}",
            url=url,
            created_at=updated or created or datetime.now(timezone.utc),
            meta={
                "owner": owner,
                "repo": repo,
                "number": number,
                "kind": kind,                   # "issues" or "pull"
                "state": state,
                "labels": labels,
                "author": author,
                "participants": sorted(participants),
            },
        )

    # ---- HTTP ---------------------------------------------------------

    def _get(self, path: str, params: dict[str, Any]) -> Any:
        qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        url = f"{GH_API}{path}" + (f"?{qs}" if qs else "")
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "synthbrain-github/0.1",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                raise GitHubAuthError(
                    f"GitHub auth failed ({e.code}). Check GITHUB_TOKEN scope."
                ) from e
            raise GitHubAPIError(f"GitHub {path} -> HTTP {e.code}") from e
        except urllib.error.URLError as e:
            raise GitHubAPIError(f"GitHub network error: {e.reason}") from e


def _parse_ts(value: Any) -> datetime | None:
    if not value:
        return None
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None
