"""iMessage adapter — macOS Messages.app chat.db -> conversation chunks.

The biggest personal "what we discussed" source: years of texts with the
people who matter most. Reads the local SQLite database the macOS Messages
app maintains:

    ~/Library/Messages/chat.db

Per-chat is the natural ingest unit (a chat = a thread, group or 1-on-1).
Messages within a chat are aggregated into ~~250-word groups and emitted
as one RawDoc per group. The source_id is `chat:<chat_guid>:<group_idx>`
so re-runs upsert deterministically.

Schema notes (Apple's, not ours):
  - chat (rowid, guid, display_name, chat_identifier)
  - handle (rowid, id [phone/email], country)
  - message (rowid, text, attributedBody, handle_id, date, is_from_me)
  - chat_message_join (chat_id, message_id)
  - chat_handle_join (chat_id, handle_id)
  Dates are nanoseconds since 2001-01-01 (Cocoa epoch).
  In recent macOS, plain `text` is often NULL — the body lives in
  `attributedBody` as a binary plist; we decode the human-readable
  string out of it.

Privacy: same hard gate as the glasses. This adapter is opt-in, runs
locally only, never network-bound, and DOES NOT export anything by
default. The user must run it explicitly on their own device.
"""

from __future__ import annotations

import os
import re
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "imessage"

# Apple Cocoa epoch is 2001-01-01 00:00:00 UTC. Dates are nanoseconds since then.
COCOA_EPOCH = datetime(2001, 1, 1, tzinfo=timezone.utc)

DEFAULT_DB_PATH = "~/Library/Messages/chat.db"
DEFAULT_WORDS_PER_GROUP = 250
DEFAULT_BACKFILL_DAYS = 365 * 3   # 3 years on first run by default

# Regex to extract printable runs from the NSAttributedString binary plist.
# Real plist parsing is overkill; the human-readable text is one of the
# longest printable runs in the blob.
_PRINTABLE_RUN = re.compile(rb"[\x20-\x7e\xc2-\xfd][\x20-\x7e\xc2-\xfd\n]{4,}")


class IMessageAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        *,
        db_path: str | None = None,
        checkpoint_db: str | None = None,
        since_days: int | None = None,
        words_per_group: int = DEFAULT_WORDS_PER_GROUP,
        include_groups: bool = True,
        max_chats: int | None = None,
    ) -> None:
        self.db_path = Path(db_path or os.environ.get("IMESSAGE_DB_PATH", DEFAULT_DB_PATH)).expanduser()
        if not self.db_path.exists():
            raise FileNotFoundError(
                f"iMessage db not found at {self.db_path}. Grant Full Disk Access to "
                "your terminal in System Settings -> Privacy & Security, or set "
                "IMESSAGE_DB_PATH explicitly."
            )
        self.checkpoint_db = checkpoint_db
        self.since_days = since_days if since_days is not None else DEFAULT_BACKFILL_DAYS
        self.words_per_group = max(50, words_per_group)
        self.include_groups = include_groups
        self.max_chats = max_chats

    def fetch(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark_ns = self._resolve_watermark(cp)
        newest_ns = watermark_ns

        # iMessage's chat.db is locked while Messages.app holds it; opening
        # read-only via URI bypasses the busy lock in most cases.
        uri = f"file:{self.db_path}?mode=ro&immutable=1"
        conn = sqlite3.connect(uri, uri=True)
        conn.row_factory = sqlite3.Row
        try:
            chats = list(self._list_chats(conn))
            if self.max_chats:
                chats = chats[: self.max_chats]
            for chat in chats:
                for doc in self._chat_to_docs(conn, chat, watermark_ns):
                    yield doc
                    if doc.meta.get("max_message_ns", 0) > newest_ns:
                        newest_ns = doc.meta["max_message_ns"]
        finally:
            conn.close()

        if cp:
            cp.set(self.name, str(newest_ns))

    # ---- query helpers --------------------------------------------------

    def _resolve_watermark(self, cp: CheckpointStore | None) -> int:
        if cp:
            stored = cp.get(self.name)
            if stored and stored.isdigit():
                return int(stored)
        # First run: backfill window
        cutoff = datetime.now(timezone.utc) - timedelta(days=self.since_days)
        return _datetime_to_apple_ns(cutoff)

    def _list_chats(self, conn: sqlite3.Connection) -> Iterable[sqlite3.Row]:
        sql = """
            SELECT
              chat.ROWID AS chat_id,
              chat.guid AS chat_guid,
              chat.display_name AS display_name,
              chat.chat_identifier AS chat_identifier,
              chat.style AS chat_style,
              COUNT(message.ROWID) AS msg_count
            FROM chat
              LEFT JOIN chat_message_join ON chat_message_join.chat_id = chat.ROWID
              LEFT JOIN message ON message.ROWID = chat_message_join.message_id
            GROUP BY chat.ROWID
            ORDER BY MAX(message.date) DESC
        """
        for row in conn.execute(sql):
            if not self.include_groups and row["chat_style"] == 43:
                # 43 = group chat in chat.style
                continue
            yield row

    def _chat_to_docs(
        self, conn: sqlite3.Connection, chat: sqlite3.Row, watermark_ns: int
    ) -> Iterable[RawDoc]:
        chat_id = chat["chat_id"]
        chat_guid = chat["chat_guid"] or f"chat-{chat_id}"
        display = chat["display_name"] or chat["chat_identifier"] or chat_guid

        # Pull all messages for this chat newer than the watermark.
        messages = list(conn.execute(
            """
            SELECT
              message.ROWID AS msg_id,
              message.text AS text,
              message.attributedBody AS attributed,
              message.is_from_me AS is_from_me,
              message.date AS date_ns,
              handle.id AS handle_id
            FROM message
              JOIN chat_message_join ON chat_message_join.message_id = message.ROWID
              LEFT JOIN handle ON message.handle_id = handle.ROWID
            WHERE chat_message_join.chat_id = ?
              AND message.date > ?
            ORDER BY message.date ASC
            """,
            (chat_id, watermark_ns),
        ))
        if not messages:
            return

        lines: list[tuple[int, str, str]] = []  # (date_ns, speaker, text)
        for m in messages:
            body = _extract_text(m)
            if not body:
                continue
            speaker = "me" if m["is_from_me"] else (m["handle_id"] or "them")
            lines.append((m["date_ns"], speaker, body))

        if not lines:
            return

        participants = sorted({s for _, s, _ in lines if s != "me"})

        # Group by word budget
        group_idx = 0
        buf: list[tuple[int, str, str]] = []
        buf_words = 0
        for ns, speaker, body in lines:
            words = len(body.split())
            buf.append((ns, speaker, body))
            buf_words += words
            if buf_words >= self.words_per_group:
                yield _emit_group(
                    chat_guid, display, participants, buf, group_idx
                )
                group_idx += 1
                buf = []
                buf_words = 0
        if buf:
            yield _emit_group(
                chat_guid, display, participants, buf, group_idx
            )


def _emit_group(
    chat_guid: str,
    display: str,
    participants: list[str],
    buf: list[tuple[int, str, str]],
    group_idx: int,
) -> RawDoc:
    first_ns = buf[0][0]
    last_ns = buf[-1][0]
    start_dt = _apple_ns_to_datetime(first_ns)
    end_dt = _apple_ns_to_datetime(last_ns)

    body_lines = [
        f"# {display}",
        f"_Participants:_ {', '.join(participants) or '(unknown)'}",
        f"_When:_ {start_dt.isoformat()} -> {end_dt.isoformat()}",
        "",
    ]
    for ns, speaker, body in buf:
        body_lines.append(f"{speaker}: {body}")

    return RawDoc(
        text="\n".join(body_lines).strip(),
        source=ADAPTER_NAME,
        source_id=f"chat:{chat_guid}:{group_idx}",
        url="",
        created_at=end_dt,
        meta={
            "chat_guid": chat_guid,
            "display": display,
            "participants": participants,
            "min_message_ns": first_ns,
            "max_message_ns": last_ns,
            "message_count": len(buf),
        },
    )


def _extract_text(msg: sqlite3.Row) -> str:
    """Prefer the plain-text column; fall back to attributedBody plist scrape."""
    text = msg["text"]
    if isinstance(text, str) and text.strip():
        return text.strip()
    blob = msg["attributed"]
    if blob is None:
        return ""
    if isinstance(blob, memoryview):
        blob = bytes(blob)
    if not isinstance(blob, (bytes, bytearray)):
        return ""
    runs = _PRINTABLE_RUN.findall(blob)
    if not runs:
        return ""
    # The body is usually the longest printable run; fall back to the second-
    # longest if the longest is one of Apple's wrapper class names.
    decoded: list[str] = []
    for run in runs:
        try:
            text = run.decode("utf-8", errors="replace").strip()
        except Exception:
            continue
        text = _strip_leading_apple_class(text)
        if text and len(text) > 3:
            decoded.append(text)
    if not decoded:
        return ""
    decoded.sort(key=len, reverse=True)
    return decoded[0]


_APPLE_CLASS_PREFIX_RE = re.compile(
    r"^(?:(?:NSAttributed|NSConcrete|NSDictionary|NSMutable|NSNumber|NSString|"
    r"NSArray|streamtyped|NSData|NSValue|NSObject|__kCFAllocator|"
    r"com\.apple\.|iI)\w*\s*)+"
)


def _strip_leading_apple_class(s: str) -> str:
    """Apple's binary plist stores class markers like 'NSDictionary' inline
    against the real text. Strip any sequence of leading marker tokens to
    reveal the human-readable body underneath."""
    return _APPLE_CLASS_PREFIX_RE.sub("", s).strip()


def _apple_ns_to_datetime(ns: int) -> datetime:
    # macOS High Sierra+ stores Cocoa-epoch nanoseconds (~10^17 for current
    # dates). Older databases store seconds (~10^9). Detect by magnitude.
    if ns > 1_000_000_000_000_000:       # > 1e15 -> nanoseconds
        seconds = ns / 1_000_000_000
    elif ns > 10_000_000_000:            # > 1e10 -> microseconds
        seconds = ns / 1_000_000
    else:
        seconds = ns                     # seconds
    return COCOA_EPOCH + timedelta(seconds=seconds)


def _datetime_to_apple_ns(dt: datetime) -> int:
    delta = dt - COCOA_EPOCH
    return int(delta.total_seconds() * 1_000_000_000)
