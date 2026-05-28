"""Drive adapter tests — mock the Google API service; no network."""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from brain.adapters.drive_adapter import DriveAdapter
from brain.core.checkpoint import CheckpointStore


@pytest.fixture(autouse=True)
def _google_env(monkeypatch):
    monkeypatch.setenv("GOOGLE_OAUTH_CLIENT_ID", "id")
    monkeypatch.setenv("GOOGLE_OAUTH_CLIENT_SECRET", "secret")
    monkeypatch.setenv("GOOGLE_OAUTH_REFRESH_TOKEN", "refresh")


def _fake_service(*, files_list_pages=None, changes_list_pages=None,
                  exports=None, downloads=None, start_token="tok-start"):
    """Build a MagicMock Drive service that returns canned responses."""
    files_list_pages = files_list_pages or [{"files": []}]
    changes_list_pages = changes_list_pages or [{"changes": [], "newStartPageToken": "tok-end"}]
    exports = exports or {}
    downloads = downloads or {}

    files = MagicMock()
    list_calls = {"n": 0}

    def files_list(**kwargs):
        i = list_calls["n"]
        list_calls["n"] += 1
        page = files_list_pages[i] if i < len(files_list_pages) else {"files": []}
        m = MagicMock(); m.execute.return_value = page
        return m
    files.list = files_list

    def files_export(*, fileId, mimeType):
        m = MagicMock(); m.execute.return_value = exports.get(fileId, b"")
        return m
    files.export = files_export

    def files_get_media(*, fileId):
        m = MagicMock(); m.execute.return_value = downloads.get(fileId, b"")
        return m
    files.get_media = files_get_media

    changes = MagicMock()
    start = MagicMock(); start.execute.return_value = {"startPageToken": start_token}
    changes.getStartPageToken = MagicMock(return_value=start)
    ch_calls = {"n": 0}

    def changes_list(**kwargs):
        i = ch_calls["n"]
        ch_calls["n"] += 1
        page = changes_list_pages[i] if i < len(changes_list_pages) else {"changes": []}
        m = MagicMock(); m.execute.return_value = page
        return m
    changes.list = changes_list

    service = MagicMock()
    service.files.return_value = files
    service.changes.return_value = changes
    return service, list_calls, ch_calls


def test_first_run_uses_files_list_and_captures_start_token():
    pages = [{
        "files": [
            {"id": "doc1", "name": "Spec.docx",
             "mimeType": "application/vnd.google-apps.document",
             "modifiedTime": "2026-05-28T10:00:00Z",
             "webViewLink": "https://docs.google.com/document/d/doc1"},
        ]
    }]
    exports = {"doc1": b"# Spec\n\nBody text"}
    service, _, _ = _fake_service(files_list_pages=pages, exports=exports,
                                  start_token="tok-end")
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch("brain.adapters.drive_adapter._drive_service", return_value=service):
            docs = list(DriveAdapter(checkpoint_db=cp_db).fetch())
        assert len(docs) == 1
        assert docs[0].source == "drive"
        assert docs[0].source_id == "doc1"
        assert "# Spec" in docs[0].text
        assert CheckpointStore(cp_db).get("drive", key="page_token") == "tok-end"


def test_second_run_uses_changes_list_with_stored_token():
    """First run primes the page_token; second run must call changes.list with it."""
    files_pages = [{"files": []}]
    changes_pages = [{
        "changes": [
            {"fileId": "f2",
             "file": {"id": "f2", "name": "note.md", "mimeType": "text/markdown",
                      "modifiedTime": "2026-05-28T11:00:00Z",
                      "webViewLink": "https://drive.google.com/file/d/f2"}}
        ],
        "newStartPageToken": "tok-next",
    }]
    downloads = {"f2": b"plain markdown body"}
    service, files_calls, ch_calls = _fake_service(
        files_list_pages=files_pages,
        changes_list_pages=changes_pages,
        downloads=downloads,
        start_token="tok1",
    )
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch("brain.adapters.drive_adapter._drive_service", return_value=service):
            # First run -- writes the start token via getStartPageToken
            list(DriveAdapter(checkpoint_db=cp_db).fetch())
            assert CheckpointStore(cp_db).get("drive", key="page_token") == "tok1"
            # Second run uses it via changes.list
            docs2 = list(DriveAdapter(checkpoint_db=cp_db).fetch())
        assert [d.source_id for d in docs2] == ["f2"]
        assert ch_calls["n"] >= 1
        # Advanced to the newStartPageToken at the end
        assert CheckpointStore(cp_db).get("drive", key="page_token") == "tok-next"


def test_removed_or_trashed_changes_are_skipped():
    files_pages = [{"files": []}]
    changes_pages = [{
        "changes": [
            {"fileId": "x", "removed": True},
            {"fileId": "y", "file": {"id": "y", "trashed": True,
                                      "mimeType": "text/markdown",
                                      "name": "trash.md"}},
            {"fileId": "z", "file": {"id": "z", "mimeType": "text/markdown",
                                      "name": "keep.md",
                                      "modifiedTime": "2026-05-28T10:00:00Z"}},
        ],
        "newStartPageToken": "after",
    }]
    downloads = {"z": b"kept"}
    service, _, _ = _fake_service(
        files_list_pages=files_pages,
        changes_list_pages=changes_pages,
        downloads=downloads,
        start_token="tok",
    )
    with tempfile.TemporaryDirectory() as d:
        cp_db = str(Path(d) / "e.db")
        with patch("brain.adapters.drive_adapter._drive_service", return_value=service):
            list(DriveAdapter(checkpoint_db=cp_db).fetch())  # prime
            docs = list(DriveAdapter(checkpoint_db=cp_db).fetch())
        assert {d.source_id for d in docs} == {"z"}


def test_oversize_files_skipped():
    pages = [{
        "files": [
            {"id": "big", "name": "Huge.pdf", "mimeType": "application/pdf",
             "size": "20000000", "modifiedTime": "2026-05-28T10:00:00Z"},
            {"id": "small", "name": "tiny.md", "mimeType": "text/markdown",
             "size": "12", "modifiedTime": "2026-05-28T10:00:00Z"},
        ]
    }]
    downloads = {"small": b"tiny body"}
    service, _, _ = _fake_service(files_list_pages=pages, downloads=downloads)
    with patch("brain.adapters.drive_adapter._drive_service", return_value=service):
        docs = list(DriveAdapter(max_bytes=1024).fetch())
    assert {d.source_id for d in docs} == {"small"}


def test_unsupported_mime_returns_no_doc():
    pages = [{
        "files": [
            {"id": "img", "name": "p.jpg", "mimeType": "image/jpeg",
             "modifiedTime": "2026-05-28T10:00:00Z"},
        ]
    }]
    service, _, _ = _fake_service(files_list_pages=pages)
    with patch("brain.adapters.drive_adapter._drive_service", return_value=service):
        docs = list(DriveAdapter().fetch())
    assert docs == []


def test_raises_when_oauth_missing(monkeypatch):
    monkeypatch.delenv("GOOGLE_OAUTH_REFRESH_TOKEN")
    with pytest.raises(RuntimeError, match="Missing Google OAuth env"):
        DriveAdapter()
