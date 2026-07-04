"""Reddit (saved RSS), Instagram (data export), Zoom (recordings), and the
m365 teams mode — all offline with mocked HTTP."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import pytest

from brain.adapters.instagram_adapter import InstagramAdapter, _fix_mojibake
from brain.adapters.reddit_adapter import RedditAdapter
from brain.adapters.zoom_adapter import ZoomAdapter, ZoomAuthError, vtt_to_text
from brain.core.checkpoint import CheckpointStore


class _FakeResp:
    def __init__(self, body: bytes):
        self._body = body

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


# --- reddit --------------------------------------------------------------------

SAVED_ATOM = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>saved by wes</title>
  <entry>
    <id>t3_abc123</id>
    <title>Newman weighting for affiliation networks</title>
    <updated>2026-07-03T18:00:00+00:00</updated>
    <link href="https://www.reddit.com/r/networkscience/comments/abc123/"/>
    <category term="networkscience" label="r/networkscience"/>
    <content type="html">&lt;p&gt;Great &lt;b&gt;thread&lt;/b&gt; on projections.&lt;/p&gt;</content>
  </entry>
  <entry>
    <id>t3_old111</id>
    <title>Old saved thing</title>
    <updated>2026-06-01T00:00:00+00:00</updated>
    <link href="https://www.reddit.com/r/misc/comments/old111/"/>
    <category term="misc" label="r/misc"/>
    <content type="html">old</content>
  </entry>
</feed>"""


def test_reddit_requires_feed_url(monkeypatch):
    monkeypatch.delenv("REDDIT_FEED_URL", raising=False)
    with pytest.raises(RuntimeError, match="REDDIT_FEED_URL"):
        RedditAdapter()


def test_reddit_parses_and_defers_watermark(tmp_path, monkeypatch):
    import brain.adapters.reddit_adapter as mod

    monkeypatch.setattr(mod.urllib.request, "urlopen",
                        lambda req, timeout=0: _FakeResp(SAVED_ATOM))
    entdb = str(tmp_path / "e.db")
    a = RedditAdapter("https://old.reddit.com/user/w/saved.rss?feed=tok&user=w",
                      checkpoint_db=entdb)
    docs = list(a.fetch())
    assert len(docs) == 2
    top = next(d for d in docs if d.source_id == "t3_abc123")
    assert top.source == "reddit"
    assert "**Subreddit:** r/networkscience" in top.text
    assert "Great" in top.text and "<b>" not in top.text
    assert top.url.endswith("/abc123/")
    assert top.created_at == datetime(2026, 7, 3, 18, tzinfo=timezone.utc)

    cp = CheckpointStore(entdb)
    assert cp.get("reddit", a.checkpoint_key) is None
    a.commit_checkpoint()
    assert cp.get("reddit", a.checkpoint_key) == "2026-07-03T18:00:00+00:00"

    # Committed watermark suppresses both entries on the next poll.
    b = RedditAdapter("https://old.reddit.com/user/w/saved.rss?feed=tok&user=w",
                      checkpoint_db=entdb)
    monkeypatch.setattr(mod.urllib.request, "urlopen",
                        lambda req, timeout=0: _FakeResp(SAVED_ATOM))
    assert list(b.fetch()) == []


def test_reddit_rejects_entity_bombs(tmp_path, monkeypatch):
    """defusedxml must refuse DTD/entity tricks from a hostile feed."""
    bomb = b"""<?xml version="1.0"?><!DOCTYPE lolz [<!ENTITY a "x">]>
    <feed xmlns="http://www.w3.org/2005/Atom"><entry><id>&a;</id></entry></feed>"""
    import brain.adapters.reddit_adapter as mod

    monkeypatch.setattr(mod.urllib.request, "urlopen",
                        lambda req, timeout=0: _FakeResp(bomb))
    a = RedditAdapter("https://old.reddit.com/user/w/saved.rss?feed=t&user=w")
    with pytest.raises(Exception):
        list(a.fetch())


# --- instagram ------------------------------------------------------------------

def test_instagram_saved_posts_and_own_posts(tmp_path):
    root = tmp_path / "export"
    saved_dir = root / "your_instagram_activity" / "saved"
    saved_dir.mkdir(parents=True)
    (saved_dir / "saved_posts.json").write_text(json.dumps({
        "saved_saved_media": [
            {"title": "plantsofinstagram",
             "string_map_data": {"Saved on": {
                 "href": "https://www.instagram.com/p/XYZ/",
                 "timestamp": 1719800000}}},
        ]
    }), encoding="utf-8")
    content_dir = root / "your_instagram_activity" / "content"
    content_dir.mkdir(parents=True)
    (content_dir / "posts_1.json").write_text(json.dumps([
        {"title": "Milsbo greenhouse build â done!",
         "creation_timestamp": 1719900000,
         "media": [{"uri": "media/x.jpg",
                     "title": "Milsbo greenhouse build â done!",
                     "creation_timestamp": 1719900000}]},
    ]), encoding="utf-8")

    docs = list(InstagramAdapter(str(root)).fetch())
    assert len(docs) == 2
    saved = next(d for d in docs if d.meta["kind"] == "saved")
    assert saved.url == "https://www.instagram.com/p/XYZ/"
    assert "plantsofinstagram" in saved.text
    assert saved.created_at == datetime.fromtimestamp(1719800000, tz=timezone.utc)
    post = next(d for d in docs if d.meta["kind"] == "post")
    assert "—" in post.text  # mojibake repaired
    # Deterministic ids: re-running an export yields identical source_ids.
    again = list(InstagramAdapter(str(root)).fetch())
    assert {d.source_id for d in again} == {d.source_id for d in docs}


def test_instagram_missing_export(tmp_path):
    with pytest.raises(FileNotFoundError):
        InstagramAdapter(str(tmp_path / "nope"))


def test_fix_mojibake_passthrough():
    assert _fix_mojibake("plain ascii") == "plain ascii"
    assert _fix_mojibake("café already fine") == "café already fine"


# --- zoom -----------------------------------------------------------------------

def test_vtt_to_text():
    vtt = """WEBVTT

1
00:00:01.000 --> 00:00:03.000
Wes Shields: Welcome everyone.

2
00:00:03.500 --> 00:00:06.000
Wes Shields: Welcome everyone.

3
00:00:06.500 --> 00:00:09.000
Joseph: Thanks for having me.
"""
    out = vtt_to_text(vtt)
    assert out.count("Welcome everyone.") == 1  # rolling-caption dedupe
    assert "Joseph: Thanks for having me." in out
    assert "-->" not in out and "WEBVTT" not in out


def test_zoom_requires_creds(monkeypatch):
    for k in ("ZOOM_ACCOUNT_ID", "ZOOM_CLIENT_ID", "ZOOM_CLIENT_SECRET"):
        monkeypatch.delenv(k, raising=False)
    with pytest.raises(ZoomAuthError):
        ZoomAdapter()


def test_zoom_fetch_transcript(tmp_path, monkeypatch):
    for k in ("ZOOM_ACCOUNT_ID", "ZOOM_CLIENT_ID", "ZOOM_CLIENT_SECRET"):
        monkeypatch.setenv(k, "x")
    import brain.adapters.zoom_adapter as mod

    transcript_vtt = "WEBVTT\n\n1\n00:00:01.000 --> 00:00:02.000\nWes: decision made.\n"
    recordings = {"meetings": [{
        "uuid": "uu1", "topic": "SynthOS sync", "duration": 30,
        "start_time": "2026-07-02T15:00:00Z",
        "share_url": "https://zoom.us/rec/share/xyz",
        "recording_files": [
            {"file_type": "MP4", "download_url": "https://zoom.us/rec/dl/video"},
            {"file_type": "TRANSCRIPT", "download_url": "https://zoom.us/rec/dl/vtt"},
        ],
    }]}

    def fake_urlopen(req, timeout=0):
        url = req.full_url
        if url.startswith(mod.TOKEN_URL):
            return _FakeResp(json.dumps({"access_token": "tok"}).encode())
        if "/recordings" in url:
            return _FakeResp(json.dumps(recordings).encode())
        if url.endswith("/vtt"):
            return _FakeResp(transcript_vtt.encode())
        return _FakeResp(b"{}")

    monkeypatch.setattr(mod.urllib.request, "urlopen", fake_urlopen)
    entdb = str(tmp_path / "e.db")
    a = ZoomAdapter(checkpoint_db=entdb)
    (doc,) = a.fetch()
    assert doc.source == "zoom" and doc.source_id == "uu1"
    assert doc.text.startswith("# SynthOS sync")
    assert "Wes: decision made." in doc.text
    assert doc.meta["kind"] == "transcript"
    a.commit_checkpoint()
    assert CheckpointStore(entdb).get("zoom", a.checkpoint_key) == "2026-07-02T15:00:00Z"


# --- m365 teams mode ------------------------------------------------------------

def test_m365_teams_mode(tmp_path, monkeypatch):
    monkeypatch.setenv("MS_CLIENT_ID", "cid")
    monkeypatch.setenv("MS_REFRESH_TOKEN", "rt")
    import brain.adapters.m365_adapter as mod
    from brain.adapters.m365_adapter import M365Adapter

    chats = {"value": [{
        "id": "chat1", "topic": None, "webUrl": "https://teams.microsoft.com/l/chat1",
        "members": [{"displayName": "Wes"}, {"displayName": "Joseph"}],
    }]}
    messages = {"value": [
        {"id": "m2", "createdDateTime": "2026-07-03T12:05:00Z",
         "messageType": "message",
         "from": {"user": {"displayName": "Joseph"}},
         "body": {"contentType": "html", "content": "<p>shipping <b>Friday</b></p>"}},
        {"id": "m1", "createdDateTime": "2026-07-03T12:00:00Z",
         "messageType": "message",
         "from": {"user": {"displayName": "Wes"}},
         "body": {"contentType": "text", "content": "status?"}},
        {"id": "m0", "createdDateTime": "2026-07-03T11:00:00Z",
         "messageType": "unknownFutureValue",
         "body": {"contentType": "text", "content": "system noise"}},
    ]}

    monkeypatch.setattr(M365Adapter, "_mint_access_token", lambda self: "tok")

    def fake_get_url(self, url, params):
        if "/chats/chat1/messages" in url:
            return messages
        if url.endswith("/me/chats"):
            return chats
        return {}

    monkeypatch.setattr(M365Adapter, "_get_url", fake_get_url)

    entdb = str(tmp_path / "e.db")
    a = M365Adapter("teams", checkpoint_db=entdb)
    (doc,) = a.fetch()
    assert doc.source_id == "teams:chat1:m2"
    assert doc.text.startswith("# Teams: Wes, Joseph")
    assert "**Wes:** status?" in doc.text
    assert "shipping Friday" in doc.text and "<b>" not in doc.text
    assert doc.meta["messages"] == 2

    # Watermark deferred: nothing until commit; then reruns yield nothing.
    cp = CheckpointStore(entdb)
    assert cp.get("m365", "teams_chat:chat1") is None
    a.commit_checkpoint()
    assert cp.get("m365", "teams_chat:chat1") == "2026-07-03T12:05:00Z"
    b = M365Adapter("teams", checkpoint_db=entdb)
    assert list(b.fetch()) == []


def test_m365_rejects_unknown_source(monkeypatch):
    monkeypatch.setenv("MS_CLIENT_ID", "cid")
    monkeypatch.setenv("MS_REFRESH_TOKEN", "rt")
    from brain.adapters.m365_adapter import M365Adapter

    with pytest.raises(ValueError):
        M365Adapter("carrier-pigeon")
