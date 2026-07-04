# WES-TODO — things only you can do

> The autonomous build keeps going without these; each one unlocks the noted
> capability the moment it's done. Newest additions at the top of each tier.
> (Claude maintains this file — check it after every session.)

## 5-minute unlocks

- [ ] **Log into instagram.com in Chrome** → I request the data export in
      Account Center; when Meta's email lands, saved posts + your posts +
      stories ingest via the ready `instagram` adapter.
- [ ] **AgentMail API key** (console → API keys) → export `AGENTMAIL_API_KEY`
      → forward-any-email-to-brain goes live (synthbrain@agentmail.to).
- [ ] **Full Disk Access** for your terminal (System Settings → Privacy &
      Security) → unlocks iMessage history (~100k msgs), iCloud Notes, and
      Safari bookmarks without exports.
- [ ] **Build the "Feed Brain" iOS Shortcut** (3 steps —
      docs/setup/feed-the-brain.md) → share-sheet capture from your phone.

## 15-minute unlocks

- [ ] **Google OAuth run** (docs/setup/google-oauth.md; I drive it in Chrome,
      you handle 2FA) → Drive + Gmail + live Calendar + live Contacts
      adapters, which also means Google Meet / Gemini notes and the
      Fireflies summaries already sitting in Drive.
- [ ] **Zoom Server-to-Server app** (marketplace.zoom.us → Develop → Build
      App → Server-to-Server OAuth, recording read scope) → 3 env vars →
      meeting transcripts ingest.
- [ ] **Azure app consent for `Chat.Read`** (same app as m365 mail) →
      Teams chats ingest via `--adapter m365 --source teams`.
- [ ] **Contacts export (.vcf)** (iPhone: Settings → Contacts export, or
      Google Contacts → Export) → merges real names onto the email-named
      graph entities; directly fixes the split-identity metrics and
      dossier-by-name.

## Exports to request (arrive by email later; adapters ready)

- [ ] **ChatGPT** (Settings → Data controls → Export) → `chatgpt` adapter.
- [ ] **Google Takeout: YouTube watch history + Location History** →
      adapters on the roadmap (watch history next).
- [ ] **WhatsApp** (per-chat export .txt, if wanted) → adapter on roadmap.
- [ ] **Mem workspace export** (Settings → Export) → replaces the MCP
      harvest snapshot with the full corpus.

## Decisions / reviews

- [ ] **Repo visibility**: SynthmindsLLC/SynthBrain is PUBLIC and now ships
      adapters for your email/messages/social. Recommend flipping private
      before PR #4 leaves draft.
- [ ] **Review PROJECT_KEYWORDS** additions in `tag.py` (synaptic-labs,
      synthsidian, jasmmm, verizon, anvl, synthbrain) — prune any dead ones.
- [ ] **Raise the Anthropic monthly spend limit** (claude.ai/settings/usage)
      if you want multi-agent workflows again — subagent fan-outs died on it
      2026-07-03; everything since has been built inline.
- [ ] **launchd**: load docs/setup/com.synthminds.brain-watch.plist when
      you want always-on intake (add REDDIT_FEED_URL + AGENTMAIL_API_KEY
      into it first; the reddit URL is in second-brain/.env.local).

## Done (for the record)

- [x] Chrome control granted → Reddit saved-posts feed captured + LIVE
      (2026-07-04); bookmarks ingested from both profiles with data.
