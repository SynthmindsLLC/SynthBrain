# Universal Intake — feed the brain from anywhere (2026-07-03)

**Directive (Wes):** "I want to be able to feed the brain any possible way —
forwarding a text, an email. Come up with a plan and start building."

## Architecture decision: pull-based pickup points

The brain stays local-first. Intake lands in places the brain **polls** —
never an exposed port, never a public webhook. Every channel converges on the
same ingestion path (adapters → pipeline → ledger → dashboard Intake panel).

```
  iPhone share-sheet ─┐
  "save .eml" ────────┤→  BrainInbox/ (iCloud-synced folder) ─┐
  POST /inbox ────────┘                                        ├→ brain watch ─→ pipeline
  forward email ─────→  synthbrain@agentmail.to (polled) ─────┘
```

| Channel                         | How Wes feeds it                                                                                                 | Component                               |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Anything from iPhone            | Share sheet → "Feed Brain" shortcut → file in iCloud BrainInbox                                                  | `inbox` adapter                         |
| Forward an email                | Forward to **synthbrain@agentmail.to**                                                                           | `agentmail` adapter (AGENTMAIL_API_KEY) |
| Forward a text                  | Share the message → Feed Brain shortcut (today); iMessage self-chat via chat.db (wave 2, needs Full Disk Access) | `inbox` adapter                         |
| Save an email file              | Mail.app → drag message to BrainInbox (saves .eml)                                                               | `inbox` adapter (.eml parser)           |
| Programmatic / scripts / agents | `POST /inbox {text,title,url}` on the brain API                                                                  | api.py → writes into BrainInbox         |
| Drag any doc                    | Drop into BrainInbox                                                                                             | `inbox` adapter (md/txt/eml/pdf/docx)   |

## Components (built this session)

1. **`brain/adapters/inbox_adapter.py`** — scans the inbox dir (default
   `~/BrainInbox`, override `BRAIN_INBOX_DIR`); md/txt/eml/docx/pdf; `.eml`
   parsed with stdlib `email` (subject→title, From/To/Date header block,
   text/plain preferred, HTML stripped as fallback); content-hash source ids
   (idempotent re-drops). **Move-on-commit:** files relocate to
   `processed/YYYY-MM/` (or `failed/`) ONLY via `commit_checkpoint()` — the
   CLI calls it after a clean zero-error run, same contract as the
   filesystem/claude-code watermarks. No checkpoint table needed: the folder
   IS the queue.
2. **`brain/adapters/agentmail_adapter.py`** — polls the AgentMail REST API
   for the intake inbox; timestamp watermark (deferred commit); renders
   messages like .eml. Needs `AGENTMAIL_API_KEY` (user action, one time).
3. **`POST /inbox`** — bearer-protected; writes the payload as a markdown
   file into BrainInbox. One ingestion path; the endpoint is just a producer.
4. **`brain watch`** — polling daemon (default 60s): inbox every cycle,
   agentmail every 5th; empty cycles leave no ledger rows. launchd plist in
   `docs/setup/` for always-on operation.

## Deferred (wave 2)

Twilio SMS number → pickup, Gmail "brain" label intake, iMessage self-chat
capture, Tailscale for remote POST /inbox, attachment OCR.

## Ops constraints

- Do NOT run `brain watch` while a bulk ingest is running (single-writer
  LanceDB assumption on this machine).
- AgentMail inbox `synthbrain@agentmail.to` created 2026-07-03 (org already
  held phytosynth@/synthminds@). Real-content emails are Wes-initiated
  forwards only — the session's own test message is synthetic.
