# Connector research + roadmap (2026-07-04)

Survey of prior art before building the social/meeting connectors, plus the
future-connector shortlist it produced.

## Prior art findings

- **[karlicoss/HPI](https://github.com/karlicoss/HPI)** — the canonical
  personal-data-pipeline project. Architecture matches ours exactly
  (export-first, local filesystem, periodic sync, normalized objects, "local
  first — no runtime API calls"). Treated as validation + a connector
  shopping list: Reddit, Instapaper/Pocket, browser history (promnesia),
  YouTube watch history, Google Location History, last.fm, RSS readers,
  Kobo/Kindle annotations, RescueTime.
- **[khoj-ai/khoj](https://github.com/khoj-ai/khoj)** — self-hosted AI
  second brain; RAG over personal docs + agents/automations. Their scheduled
  "automations" mirror our watch daemon; nothing architectural to steal that
  we lack.
- **[screenpipe](https://github.com/screenpipe/screenpipe)** — 24/7
  screen+audio capture, local. The ambient-capture endgame (our Phase 4 /
  G2 glasses) as a desktop analog; heavy, revisit for ambient later.
- **Reddit API policy (Nov 2025)**: pre-approval now required for ALL API
  apps, including personal
  ([ReplyDaddy](https://replydaddy.com/blog/reddit-api-pre-approval-2025-personal-projects-crackdown),
  [rate-limit guide](https://painonsocial.com/blog/reddit-api-rate-limits-guide)).
  → We use the sanctioned **private RSS feeds** (reddit.com/prefs/feeds)
  instead: no OAuth, no approval, pollable. Backlog beyond the ~25-item feed
  window comes from the GDPR export (saved_posts.csv) if wanted.
- **Instagram**: personal-content API is dead (Basic Display, 2024).
  Scraping a logged-in session risks account flags. → Official Meta data
  export (includes `saved_posts.json`) + adapter; export re-requested
  periodically (Chrome-assisted).

## Built this session

reddit (saved RSS, watch-daemon polled) · instagram (data-export JSON:
saved/posts/stories/likes, mojibake-repaired) · zoom (Server-to-Server
OAuth, recording transcripts as VTT→text, chat fallback) · m365 teams mode
(Graph /me/chats, per-chat deferred watermarks).

## Future-connector shortlist (from HPI + gaps)

1. **Browser history** (Chrome History sqlite — same read pattern as
   bookmarks; promnesia proves the value) — high signal for "what was I
   looking into".
2. **YouTube watch history** (Google Takeout) — pairs with bookmarks.
3. **Pocket/Instapaper** exports if used.
4. **Google Location History** (Takeout; place entities + `attended`-style
   edges — feeds the dossier's "where you met").
5. **WhatsApp export** (chat .txt export per conversation).
6. **RSS/newsletter reader** — a feeds.txt of subscriptions polled by watch.
7. **Fireflies transcripts** — already in Drive; lands with the Drive
   adapter once Google OAuth is provisioned.

## Provisioning state (Chrome-assisted)

- ✅ Reddit feed token captured from prefs/feeds → `.env.local`
  (REDDIT_FEED_URL) — live-tested, 53 chunks ingested.
- ⬜ Instagram export request (accountscenter → Download your information;
  JSON, all time) — arrives by email days later; drop the unzipped folder
  and run `ingest --adapter instagram --source <folder>`.
- ⬜ Google OAuth (docs/setup/google-oauth.md) — GCP console flow; unlocks
  drive/gmail/gcal-live/people-live (+ Meet/Gemini notes + Fireflies in
  Drive). Needs a Chrome session with 2FA on hand.
- ⬜ Zoom Server-to-Server app (marketplace.zoom.us) → ZOOM_* env.
- ⬜ Azure app Chat.Read consent for the Teams mode → MS_* env.
