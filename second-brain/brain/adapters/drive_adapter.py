"""Drive (Google) chunk adapter — pulls Doc/PDF/text content into LanceDB.

Replaces the TS `apps/connectors/drive --ingest` second pass. The TS Drive
connector still owns the *organize* job (move/rename/trash); this adapter is
for ingesting Drive content into the brain's vector index.

Auth: same OAuth refresh-token + scopes as the live Calendar / People
adapters (`gcal_live_adapter`). Add `drive.readonly` (or `drive` if you
already have it) to the same client.

Incremental sync via Drive Changes API:
  - changes.getStartPageToken() once on first run -> stored in checkpoint
  - changes.list(pageToken=...) each run; advance the token at the end
  - Deleted/trashed files are skipped (LanceDB chunks for them remain;
    cleanup is a separate pass and Phase 3 polish)

Content extraction:
  - Google Docs: exported as text/markdown via files.export()
  - PDFs / DOCX / TXT / MD: downloaded to a temp buffer, parsed in-memory
    using the same extractors as filesystem_adapter (lazy-imported so
    docx2txt / pypdf stay optional)

Lazy import of googleapiclient keeps the rest of the brain dep-free.
"""

from __future__ import annotations

import io
import os
from datetime import datetime, timezone
from typing import Callable, Iterable

from ..core.checkpoint import CheckpointStore
from ..core.pipeline import RawDoc
from .base import Adapter

ADAPTER_NAME = "drive"
DEFAULT_PAGE_SIZE = 200
DEFAULT_MAX_BYTES = 10 * 1024 * 1024  # 10 MB; bigger Drive files are skipped

# Google MIME -> export MIME we ask for
DOC_EXPORT_MIME = {
    "application/vnd.google-apps.document": "text/markdown",
    "application/vnd.google-apps.spreadsheet": "text/csv",
    "application/vnd.google-apps.presentation": "text/plain",
}
# Native MIME -> in-memory text extractor
NATIVE_EXTRACTORS: dict[str, Callable[[bytes], str]] = {}


def _register_native_extractors() -> None:
    """Populate at import time; missing optional deps degrade to skip."""
    NATIVE_EXTRACTORS["text/plain"] = lambda b: b.decode("utf-8", errors="replace")
    NATIVE_EXTRACTORS["text/markdown"] = lambda b: b.decode("utf-8", errors="replace")
    NATIVE_EXTRACTORS["text/x-markdown"] = lambda b: b.decode("utf-8", errors="replace")
    NATIVE_EXTRACTORS["application/pdf"] = _extract_pdf
    NATIVE_EXTRACTORS[
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ] = _extract_docx


def _extract_pdf(data: bytes) -> str:
    try:
        from pypdf import PdfReader  # type: ignore[import-not-found]
    except ImportError:
        return ""
    reader = PdfReader(io.BytesIO(data))
    pages = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            pages.append("")
    return "\n\n".join(pages)


def _extract_docx(data: bytes) -> str:
    try:
        import docx2txt  # type: ignore[import-not-found]
    except ImportError:
        return ""
    # docx2txt only accepts paths; write a tmp file just in time.
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=True) as f:
        f.write(data)
        f.flush()
        return docx2txt.process(f.name) or ""


_register_native_extractors()


class DriveAdapter(Adapter):
    """Pulls Drive content as chunks. Incremental after the first run."""

    name = ADAPTER_NAME

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        refresh_token: str | None = None,
        checkpoint_db: str | None = None,
        folder_id: str | None = None,
        max_bytes: int = DEFAULT_MAX_BYTES,
        page_size: int = DEFAULT_PAGE_SIZE,
    ) -> None:
        self.client_id = client_id or os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
        self.refresh_token = refresh_token or os.environ.get("GOOGLE_OAUTH_REFRESH_TOKEN")
        if not all([self.client_id, self.client_secret, self.refresh_token]):
            raise RuntimeError(
                "Missing Google OAuth env. Set GOOGLE_OAUTH_CLIENT_ID, "
                "GOOGLE_OAUTH_CLIENT_SECRET, GOOGLE_OAUTH_REFRESH_TOKEN."
            )
        self.checkpoint_db = checkpoint_db
        self.folder_id = folder_id  # if set, only files under this folder
        self.max_bytes = max_bytes
        self.page_size = page_size

    def fetch(self) -> Iterable[RawDoc]:
        service = _drive_service(self.client_id, self.client_secret, self.refresh_token)
        cp = CheckpointStore(self.checkpoint_db) if self.checkpoint_db else None
        token = cp.get(self.name, key="page_token") if cp else None

        if token:
            yield from self._iter_via_changes(service, cp, token)
        else:
            # First run: full crawl, then capture the page token AFTER so
            # changes after this moment are caught next run.
            start_token = service.changes().getStartPageToken().execute().get("startPageToken")
            yield from self._iter_via_files_list(service)
            if cp and start_token:
                cp.set(self.name, start_token, key="page_token")

    def _iter_via_files_list(self, service) -> Iterable[RawDoc]:
        page_token: str | None = None
        q_parts = ["trashed = false", "mimeType != 'application/vnd.google-apps.folder'"]
        if self.folder_id:
            q_parts.insert(0, f"'{self.folder_id}' in parents")
        q = " and ".join(q_parts)
        while True:
            resp = service.files().list(
                q=q,
                fields=("nextPageToken, files(id,name,mimeType,size,modifiedTime,"
                        "webViewLink,parents)"),
                pageSize=self.page_size,
                pageToken=page_token,
            ).execute()
            for f in resp.get("files", []):
                doc = self._file_to_doc(service, f)
                if doc is not None:
                    yield doc
            page_token = resp.get("nextPageToken")
            if not page_token:
                return

    def _iter_via_changes(self, service, cp, page_token: str) -> Iterable[RawDoc]:
        next_page_token: str | None = None
        while True:
            resp = service.changes().list(
                pageToken=page_token,
                pageSize=self.page_size,
                fields=("newStartPageToken, nextPageToken, "
                        "changes(fileId, removed, "
                        "file(id,name,mimeType,size,modifiedTime,webViewLink,parents,trashed))"),
            ).execute()
            for ch in resp.get("changes", []):
                if ch.get("removed"):
                    continue
                f = ch.get("file") or {}
                if not f or f.get("trashed"):
                    continue
                if f.get("mimeType") == "application/vnd.google-apps.folder":
                    continue
                doc = self._file_to_doc(service, f)
                if doc is not None:
                    yield doc
            next_page_token = resp.get("nextPageToken")
            new_start = resp.get("newStartPageToken")
            if next_page_token:
                page_token = next_page_token
                continue
            if cp and new_start:
                cp.set(self.name, new_start, key="page_token")
            return

    def _file_to_doc(self, service, f: dict) -> RawDoc | None:
        size = int(f.get("size") or 0)
        if size and size > self.max_bytes:
            return None
        text = _extract_drive_text(service, f)
        if not text or not text.strip():
            return None
        modified = f.get("modifiedTime")
        try:
            ts = datetime.fromisoformat(modified.replace("Z", "+00:00")) if modified else datetime.now(timezone.utc)
        except (ValueError, AttributeError):
            ts = datetime.now(timezone.utc)
        return RawDoc(
            text=text.strip(),
            source=self.name,
            source_id=str(f["id"]),
            url=f.get("webViewLink", ""),
            created_at=ts.astimezone(timezone.utc),
            meta={
                "mime": f.get("mimeType", ""),
                "name": f.get("name", ""),
                "bytes": size,
            },
        )


def _extract_drive_text(service, f: dict) -> str:
    """Return text content for one Drive file, or "" if not extractable."""
    mime = f.get("mimeType", "")
    file_id = f.get("id")
    if not file_id:
        return ""

    if mime in DOC_EXPORT_MIME:
        # Google-native doc: export
        try:
            data = service.files().export(
                fileId=file_id, mimeType=DOC_EXPORT_MIME[mime]
            ).execute()
        except Exception:
            return ""
        if isinstance(data, bytes):
            return data.decode("utf-8", errors="replace")
        return str(data or "")

    extractor = NATIVE_EXTRACTORS.get(mime)
    if extractor is None:
        return ""

    try:
        data = service.files().get_media(fileId=file_id).execute()
    except Exception:
        return ""
    if isinstance(data, str):
        data = data.encode("utf-8")
    if not isinstance(data, (bytes, bytearray)):
        return ""
    try:
        return extractor(bytes(data))
    except Exception:
        return ""


def _drive_service(client_id: str, client_secret: str, refresh_token: str):
    from google.oauth2.credentials import Credentials  # type: ignore[import-not-found]
    from googleapiclient.discovery import build  # type: ignore[import-not-found]

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=["https://www.googleapis.com/auth/drive.readonly"],
    )
    return build("drive", "v3", credentials=creds, cache_discovery=False)
