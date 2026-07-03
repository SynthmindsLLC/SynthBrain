# Feed the Brain — every intake channel

Everything converges on two pickup points the brain polls: the **BrainInbox
drop folder** and the **AgentMail intake inbox**. Start the daemon once and
anything you drop, forward, or share lands in the index within a minute.

```bash
cd second-brain
BRAIN_INBOX_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/BrainInbox" \
AGENTMAIL_API_KEY="<key>" \
python -m brain.cli --db data/brain_index --entdb data/entities.db --embedder local watch
```

> Point `BRAIN_INBOX_DIR` at an **iCloud Drive folder** (path above) and your
> iPhone can feed the brain from anywhere — files sync down and the watcher
> picks them up. Default is `~/BrainInbox` (Mac-only).

## Channel by channel

### Forward an email → `synthbrain@agentmail.to`

Forward from any mail client. The `agentmail` adapter polls the inbox every
few watch cycles. One-time setup: create an API key in the AgentMail console
and export `AGENTMAIL_API_KEY` for the watcher. (Inbox created 2026-07-03;
org also holds synthminds@/phytosynth@.)

Alternative, no key needed: drag any message out of Mail.app into BrainInbox —
it saves as `.eml` and the inbox adapter parses subject/from/date/body.

### Forward a text (iPhone share sheet)

Create a Shortcut once — **Shortcuts → + → name it "Feed Brain"**:

1. Settings (ⓘ) → enable **Show in Share Sheet** (accept Text, URLs, Safari pages).
2. Add action **Text** — content: `Shortcut Input`.
3. Add action **Save File** → destination **iCloud Drive → BrainInbox**,
   ask-where **off**, filename e.g. `Ask Each Time` off (auto).

Then in Messages: long-press a message → Share → **Feed Brain**. Same flow
works from Safari, Mail, Notes, Photos (text), anywhere with a share sheet.

### POST /inbox (scripts, agents, Shortcuts-over-HTTP)

```bash
curl -X POST localhost:8088/inbox -H 'Content-Type: application/json' \
  -d '{"text":"...", "title":"optional", "url":"optional", "source_hint":"cli"}'
```

Writes a markdown file into BrainInbox (honors the bearer token). The watcher
ingests it on the next cycle — one ingestion path for every channel.

### Drag anything

Drop `.md` `.txt` `.eml` `.pdf` `.docx` into BrainInbox. After a clean ingest
files move to `processed/YYYY-MM/`; unparseable ones quarantine in `failed/`.

## Always-on (launchd)

`docs/setup/com.synthminds.brain-watch.plist` — edit the two env values,
then:

```bash
cp docs/setup/com.synthminds.brain-watch.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.synthminds.brain-watch.plist
```

## Rules of the road

- **Don't run `watch` while a bulk ingest is running** — single writer on the
  LanceDB index. Stop one before starting the other.
- The watcher holds the local embedding model resident (~400MB). On the 8GB
  Mac that's fine alone, but it's the reason bulk + watch don't coexist.
- Empty cycles leave no ledger rows; every real intake shows up on the
  dashboard's Intake panel with source `inbox` or `agentmail`.
- iMessage self-chat capture (reading chat.db directly) is wave-2 — needs the
  Full Disk Access grant. The share-sheet shortcut covers texts today.
