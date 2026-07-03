"""Claude Code session adapter — ~/.claude/projects transcripts -> RawDocs.

Claude Code writes one JSONL transcript per session at
`<projects-root>/<project-slug>/<session-uuid>.jsonl`. Each line is one JSON
event; only 'user'/'assistant' message events carry conversation text — the
rest (last-prompt, mode, attachment, file-history-snapshot, ai-title, ...) is
session machinery. Message content is either a plain string or a list of
blocks, of which only {type: "text"} blocks are prose — tool_use/tool_result/
thinking blocks are skipped.

One RawDoc per session file, rendered in the claude_adapter idiom
(`**user:** ...` / `**assistant:** ...` joined by blank lines) and capped at
MAX_DOC_CHARS with a truncation marker. Malformed lines are counted in
`skip_report` and never abort the file. Watermark is the max session-file
mtime, namespaced per projects root (same pattern as the filesystem adapter).
Directories whose path contains `node_modules` are always skipped; exclude
terms ADD to DEFAULT_EXCLUDES ('alltheplants' — not Wes's work product), they
never replace them. Nested jsonl artifacts (subagents/workflows journals) are
NOT sessions — only depth-2 `<project>/<session>.jsonl` files are read.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter
from .filesystem_adapter import _parse_iso

ADAPTER_NAME = "claude-code"
DEFAULT_PROJECTS_ROOT = "~/.claude/projects"
DEFAULT_EXCLUDES = ("alltheplants",)
MAX_DOC_CHARS = 400 * 1024
TRUNCATION_MARKER = "\n\n[transcript truncated at 400KB]"
MAX_SKIP_SAMPLES = 20
_MESSAGE_TYPES = ("user", "assistant")


class ClaudeCodeAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source: str = "",
        *,
        checkpoint_db: str | None = None,
        since: str | None = None,
        exclude: list[str] | None = None,
    ) -> None:
        self.projects_root = Path(source or DEFAULT_PROJECTS_ROOT).expanduser().resolve()
        if not self.projects_root.exists():
            raise FileNotFoundError(
                f"Claude Code projects root not found: {self.projects_root}"
            )
        self.checkpoint_db = checkpoint_db
        self.since = _parse_iso(since) if since else None
        # Additive: caller terms extend the defaults, never replace them.
        self.exclude_terms = [t.lower() for t in (*DEFAULT_EXCLUDES, *(exclude or []))]
        # Namespace the watermark per projects root so two roots never share one.
        dir_hash = hashlib.sha1(str(self.projects_root).encode("utf-8")).hexdigest()[:12]
        self.checkpoint_key = f"last_sync:{dir_hash}"
        self.skip_report: dict[str, dict[str, Any]] = {}
        self._pending_watermark: str | None = None

    def fetch(self) -> Iterable[RawDoc]:
        self.skip_report = {}
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = self.since or (
            _parse_iso(cp.get(self.name, self.checkpoint_key)) if cp else None
        )
        newest_seen: datetime | None = None

        for project_dir in sorted(self.projects_root.iterdir()):
            if not project_dir.is_dir():
                continue
            if self._is_excluded(project_dir):
                self._record_skip("excluded", project_dir)
                continue
            for path in sorted(project_dir.glob("*.jsonl")):
                try:
                    stat = path.stat()
                except OSError:
                    self._record_skip("unreadable", path)
                    continue
                mtime = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
                if watermark and mtime <= watermark:
                    continue
                try:
                    text, rendered, truncated = self._render_session(path)
                except OSError:
                    self._record_skip("unreadable", path)
                    continue
                if rendered == 0:
                    self._record_skip("empty", path)
                    continue
                yield RawDoc(
                    text=text,
                    source=self.name,
                    source_id=path.stem,
                    url="",
                    created_at=mtime,
                    meta={
                        "project": project_dir.name,
                        "path": str(path),
                        "messages": rendered,
                        "truncated": truncated,
                    },
                )
                if newest_seen is None or mtime > newest_seen:
                    newest_seen = mtime

        # Recorded, not committed — the CLI calls commit_checkpoint() only
        # after the pipeline's final flush succeeded with zero doc errors
        # (same tail-flush-loss guard as the filesystem adapter).
        if cp and newest_seen:
            self._pending_watermark = newest_seen.isoformat()

    def commit_checkpoint(self) -> None:
        if self.checkpoint_db and self._pending_watermark:
            CheckpointStore(self.checkpoint_db).set(
                self.name, self._pending_watermark, key=self.checkpoint_key
            )
            self._pending_watermark = None

    def _render_session(self, path: Path) -> tuple[str, int, bool]:
        """One session file -> (rendered markdown, messages rendered, truncated).

        Defensive per-line: a malformed line is counted and skipped, never
        fatal (the pipeline's per-doc isolation is the second net, not the
        first). Stops reading once the char cap is reached."""
        title = f"# Claude Code — {path.parent.name} — {path.stem}"
        parts: list[str] = [title]
        total = len(title)
        rendered = 0
        truncated = False
        with path.open(encoding="utf-8", errors="replace") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    event = json.loads(line)
                except ValueError:
                    self._record_skip("bad_line", f"{path}:{lineno}")
                    continue
                if not isinstance(event, dict) or event.get("type") not in _MESSAGE_TYPES:
                    continue
                msg = event.get("message")
                if not isinstance(msg, dict):
                    continue
                text = _extract_text(msg.get("content"))
                if not text:
                    continue
                role = msg.get("role") or event["type"]
                entry = f"**{role}:** {text}"
                if total + len(entry) + 2 > MAX_DOC_CHARS:
                    room = MAX_DOC_CHARS - total - 2
                    if room > 0:
                        parts.append(entry[:room])
                        rendered += 1
                    parts.append(TRUNCATION_MARKER.strip())
                    truncated = True
                    break
                parts.append(entry)
                total += len(entry) + 2
                rendered += 1
        return "\n\n".join(parts), rendered, truncated

    def _is_excluded(self, project_dir: Path) -> bool:
        low = project_dir.as_posix().lower()
        if "node_modules" in low:
            return True
        name = project_dir.name.lower()
        return any(term in name for term in self.exclude_terms)

    def _record_skip(self, reason: str, sample: Any) -> None:
        entry = self.skip_report.setdefault(reason, {"count": 0, "samples": []})
        entry["count"] += 1
        if len(entry["samples"]) < MAX_SKIP_SAMPLES:
            entry["samples"].append(str(sample))


def _extract_text(content: Any) -> str:
    """Message content is a plain string or a list of blocks; only
    {type: "text"} blocks are conversation prose."""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for block in content:
            if (
                isinstance(block, dict)
                and block.get("type") == "text"
                and isinstance(block.get("text"), str)
            ):
                parts.append(block["text"])
        return "\n".join(p for p in parts if p).strip()
    return ""
