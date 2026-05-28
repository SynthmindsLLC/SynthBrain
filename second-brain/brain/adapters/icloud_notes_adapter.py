"""iCloud Notes adapter — Apple Notes / iCloud Notes -> chunks.

Two paths, behind one interface:

  Path A (preferred for personal use): macOS local NoteStore.sqlite
    ~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite

    The Notes app keeps a local SQLite database mirroring iCloud state.
    Unencrypted notes (the default) have their body in `ZNOTEDATA.ZDATA`
    as a gzipped protobuf. We decompress, extract the longest
    human-readable run, and emit one RawDoc per note.

    Encrypted ("Locked") notes are skipped — we never have the password.
    Notes are identified by the `ZNOTE.ZIDENTIFIER` UUID so re-runs
    upsert deterministically.

  Path B (durable cross-platform): folder of exported notes
    Notes.app -> File -> Export as PDF / Markdown / text per note, or
    the iCloud.com "Export as HTML" bulk dump. Point --source at the
    folder of files. Same shape as the filesystem adapter; one note
    per file, source_id = filename stem, content extractor matches the
    file extension.

Adapter chooses Path A when --source points at the NoteStore.sqlite
file (or no source is given and the default macOS path exists), Path B
otherwise.
"""

from __future__ import annotations

import gzip
import os
import re
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "icloud-notes"

DEFAULT_DB_PATH = (
    "~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite"
)

# Cocoa epoch (matches iMessage adapter)
COCOA_EPOCH = datetime(2001, 1, 1, tzinfo=timezone.utc)


class ICloudNotesAdapter(Adapter):
    name = ADAPTER_NAME

    def __init__(
        self,
        source: str = "",
        *,
        checkpoint_db: str | None = None,
        max_notes: int | None = None,
    ) -> None:
        self.checkpoint_db = checkpoint_db
        self.max_notes = max_notes
        resolved = self._resolve_source(source)
        self.source = resolved
        self.mode = "sqlite" if resolved.suffix.lower() == ".sqlite" else "folder"

    def _resolve_source(self, source: str) -> Path:
        if source:
            p = Path(source).expanduser()
        else:
            p = Path(os.environ.get("ICLOUD_NOTES_DB_PATH", DEFAULT_DB_PATH)).expanduser()
        if not p.exists():
            raise FileNotFoundError(
                f"iCloud Notes source not found at {p}. Either point --source "
                "at a folder of exported notes (.txt/.md/.html), or "
                "grant Full Disk Access to your terminal so it can read the "
                "macOS NoteStore.sqlite."
            )
        return p

    def fetch(self) -> Iterable[RawDoc]:
        if self.mode == "sqlite":
            yield from self._fetch_sqlite()
        else:
            yield from self._fetch_folder()

    # ---- Path A: macOS NoteStore --------------------------------------

    def _fetch_sqlite(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = float(cp.get(self.name) or 0) if cp else 0.0
        newest = watermark

        uri = f"file:{self.source}?mode=ro&immutable=1"
        conn = sqlite3.connect(uri, uri=True)
        conn.row_factory = sqlite3.Row
        try:
            rows = list(conn.execute(_NOTES_QUERY))
            count = 0
            for row in rows:
                doc, mtime = self._row_to_doc(row)
                if doc is None:
                    continue
                if mtime <= watermark:
                    continue
                yield doc
                count += 1
                if mtime > newest:
                    newest = mtime
                if self.max_notes and count >= self.max_notes:
                    break
        finally:
            conn.close()

        if cp:
            cp.set(self.name, str(newest))

    def _row_to_doc(self, row: sqlite3.Row) -> tuple[RawDoc | None, float]:
        if row["is_password_protected"]:
            return None, 0.0
        body = _extract_note_body(row["data"])
        if not body or not body.strip():
            return None, 0.0
        title = (row["title"] or _first_line(body) or "(untitled note)").strip()
        identifier = row["identifier"] or f"note-{row['note_id']}"
        modified = _cocoa_seconds_to_datetime(row["modification_date"] or 0)
        return (
            RawDoc(
                text=f"# {title}\n\n{body}".strip(),
                source=ADAPTER_NAME,
                source_id=str(identifier),
                url="",
                created_at=modified,
                meta={
                    "folder": row["folder_name"] or "",
                    "title": title,
                    "snippet": (row["snippet"] or "")[:200],
                },
            ),
            row["modification_date"] or 0.0,
        )

    # ---- Path B: folder of exports ------------------------------------

    def _fetch_folder(self) -> Iterable[RawDoc]:
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        watermark = float(cp.get(self.name) or 0) if cp else 0.0
        newest = watermark

        for path in self._iter_files():
            mtime = path.stat().st_mtime
            if mtime <= watermark:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if path.suffix.lower() in (".html", ".htm"):
                text = _html_to_text(text)
            text = text.strip()
            if not text:
                continue
            title = _first_line(text) or path.stem
            yield RawDoc(
                text=text,
                source=ADAPTER_NAME,
                source_id=path.stem,
                url=path.as_uri(),
                created_at=datetime.fromtimestamp(mtime, tz=timezone.utc),
                meta={"path": str(path), "title": title},
            )
            if mtime > newest:
                newest = mtime
        if cp:
            cp.set(self.name, str(newest))

    def _iter_files(self) -> Iterable[Path]:
        exts = {".txt", ".md", ".markdown", ".html", ".htm"}
        for path in sorted(self.source.rglob("*")):
            if path.is_file() and path.suffix.lower() in exts:
                yield path


_NOTES_QUERY = """
SELECT
  N.Z_PK              AS note_id,
  N.ZIDENTIFIER       AS identifier,
  N.ZTITLE1           AS title,
  N.ZSNIPPET          AS snippet,
  N.ZMODIFICATIONDATE AS modification_date,
  N.ZISPASSWORDPROTECTED AS is_password_protected,
  D.ZDATA             AS data,
  F.ZTITLE2           AS folder_name
FROM ZICCLOUDSYNCINGOBJECT N
  LEFT JOIN ZICNOTEDATA D ON D.ZNOTE = N.Z_PK
  LEFT JOIN ZICCLOUDSYNCINGOBJECT F ON F.Z_PK = N.ZFOLDER
WHERE N.Z_ENT = (
  SELECT Z_ENT FROM Z_PRIMARYKEY WHERE Z_NAME = 'ICNote'
)
  AND N.ZMARKEDFORDELETION = 0
"""


# Apple stores the note body as a gzipped protobuf. We don't parse the
# whole protobuf — the human-readable string is the longest printable run
# inside the decompressed bytes, after we strip protobuf framing.
_PRINTABLE_RUN = re.compile(
    rb"[\x20-\x7e\xc2-\xfd][\x20-\x7e\xc2-\xfd\n\t]{12,}"
)


def _extract_note_body(blob: bytes | memoryview | None) -> str:
    if blob is None:
        return ""
    if isinstance(blob, memoryview):
        blob = bytes(blob)
    if not isinstance(blob, (bytes, bytearray)):
        return ""
    blob = bytes(blob)
    if blob[:2] == b"\x1f\x8b":
        try:
            decompressed = gzip.decompress(blob)
        except Exception:
            decompressed = blob
    else:
        decompressed = blob
    runs = []
    for m in _PRINTABLE_RUN.findall(decompressed):
        try:
            text = m.decode("utf-8", errors="replace")
        except Exception:
            continue
        text = _strip_protobuf_noise(text)
        if len(text.strip()) > 12:
            runs.append(text.strip())
    if not runs:
        return ""
    runs.sort(key=len, reverse=True)
    return runs[0]


_PROTOBUF_NOISE_PREFIX = re.compile(
    r"^(?:[\x00-\x1f]+|public\.utf8-plain-text|public\.text|"
    r"com\.apple\.notes\.[\w\.]+|attachment-uuid|\w{8}-\w{4}-\w{4}-\w{4}-\w{12})+\s*"
)


def _strip_protobuf_noise(s: str) -> str:
    return _PROTOBUF_NOISE_PREFIX.sub("", s).strip()


_HTML_TAG_RE = re.compile(r"<[^>]+>")
_HTML_ENTITY_RE = re.compile(r"&(amp|lt|gt|nbsp|quot|#39);")
_HTML_REPL = {"amp": "&", "lt": "<", "gt": ">", "nbsp": " ", "quot": '"', "#39": "'"}


def _html_to_text(html: str) -> str:
    text = _HTML_TAG_RE.sub(" ", html)
    text = _HTML_ENTITY_RE.sub(lambda m: _HTML_REPL.get(m.group(1), m.group(0)), text)
    return re.sub(r"\s+", " ", text).strip()


def _first_line(text: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line:
            return line
    return ""


def _cocoa_seconds_to_datetime(seconds: float) -> datetime:
    if not seconds:
        return datetime.now(timezone.utc)
    try:
        return COCOA_EPOCH + timedelta(seconds=float(seconds))
    except (OverflowError, ValueError):
        return datetime.now(timezone.utc)
