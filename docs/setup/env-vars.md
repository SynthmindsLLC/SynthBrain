# `.env.local` setup — one file, every secret

The Python brain reads connector credentials from process env. Everything
lives in `second-brain/.env.local` (gitignored). This doc walks through
what each variable is, where to get it, and how to load the file before
running the CLI.

## 1. Create the file

```bash
cd second-brain
cp .env.example .env.local
```

Open `.env.local` in your editor. The template below is annotated.

## 2. Connector-by-connector reference

You don't need to fill all of these. Each block is independent — fill
only what you want to run today, add more later. The CLI will tell you
which env var is missing if you try a connector that's not wired up.

### Fieldy AI (transcripts)

```bash
FIELDY_API_KEY=sk-f-PASTE_ROTATED_KEY_HERE
FIELDY_API_BASE=https://api.fieldy.ai/api/public/v2
FIELDY_MCP_URL=https://api.fieldy.ai/mcp
```

Get the key: Fieldy app → Settings → Developer Settings → Public API →
**Create API key**. Apple shows it once.

### Google (Drive + Calendar + People + Gmail — one OAuth client, all four)

```bash
GOOGLE_OAUTH_CLIENT_ID=YOUR_CLIENT_ID.apps.googleusercontent.com
GOOGLE_OAUTH_CLIENT_SECRET=YOUR_CLIENT_SECRET
GOOGLE_OAUTH_REFRESH_TOKEN=PASTE_REFRESH_TOKEN
```

How to get them — one-time setup:

1. https://console.cloud.google.com → **APIs & Services → Credentials** →
   **Create Credentials → OAuth client ID**.
2. Application type: **Web application**.
3. Authorized redirect URIs: `https://developers.google.com/oauthplayground`.
4. **Copy Client ID and Client Secret** into the env vars above.
5. **Enable the APIs** under **APIs & Services → Library**: Drive, Calendar,
   People, Gmail.
6. Go to https://developers.google.com/oauthplayground. Click the **gear** in
   the top right, check **Use your own OAuth credentials**, paste the
   Client ID + secret.
7. In **Step 1**, paste all four scopes (one per line):
   ```
   https://www.googleapis.com/auth/drive.readonly
   https://www.googleapis.com/auth/calendar.readonly
   https://www.googleapis.com/auth/contacts.readonly
   https://www.googleapis.com/auth/gmail.readonly
   ```
8. **Authorize APIs** → sign in as your owner account → **Allow**.
9. **Step 2** → **Exchange authorization code for tokens**.
10. Copy the **Refresh token** value into `GOOGLE_OAUTH_REFRESH_TOKEN`.

In Testing mode (default; we recommend you stay here for personal use),
that refresh token expires after 7 days. Re-mint via the same Playground
flow when needed. The connector will fail loud with a 400 when it needs
refreshing.

### iCloud Mail (IMAP)

```bash
IMAP_HOST=imap.mail.me.com
IMAP_PORT=993
IMAP_USERNAME=YOUR_APPLE_ID@icloud.com
IMAP_PASSWORD=xxxx-xxxx-xxxx-xxxx
IMAP_FOLDER=INBOX
IMAP_OWN_DOMAINS=synthminds.ai
```

iCloud Mail has no public REST API. Use IMAP with an
**app-specific password**:

1. https://appleid.apple.com → **Sign-In and Security → App-Specific
   Passwords** → **Generate**.
2. Label it `SynthBrain IMAP`.
3. Copy the 19-character password (Apple shows it once).
4. Paste into `IMAP_PASSWORD`. **Never** use your real iCloud password.

### iMessage (Messages.app)

No env var required by default — the adapter reads
`~/Library/Messages/chat.db`. But **macOS requires Full Disk Access** for
your terminal:

System Settings → Privacy & Security → **Full Disk Access** → enable for
Terminal (or iTerm, or whichever shell you use).

If you copied `chat.db` somewhere else, override:

```bash
IMESSAGE_DB_PATH=/path/to/your/chat.db
```

### iCloud Notes

Like iMessage, requires Full Disk Access. Default path:
`~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite`. Override:

```bash
ICLOUD_NOTES_DB_PATH=/path/to/NoteStore.sqlite
```

Or point the adapter at a folder of exported notes (`.txt` / `.md` / `.html`).

### GitHub (issues + PRs + comments across all your repos)

```bash
GITHUB_TOKEN=github_pat_PASTE_TOKEN
GITHUB_USERNAME=YOUR_GITHUB_LOGIN
```

How to get the token:

1. https://github.com/settings/personal-access-tokens → **Fine-grained
   tokens** → **Generate new token**.
2. Repository access: **All repositories** (or pick specific repos).
3. Permissions:
   - **Issues**: Read
   - **Pull requests**: Read
   - **Contents**: Read
   - **Metadata**: Read (auto-required)
4. Generate, copy `github_pat_...` into `GITHUB_TOKEN`.

`GITHUB_USERNAME` is your login (e.g. `CommodoreWesmardo`). If not set,
the adapter resolves it via `GET /user`.

### Microsoft 365 / Outlook (Graph)

Only needed if you still use M365.

```bash
MS_TENANT_ID=common
MS_CLIENT_ID=YOUR_APP_REGISTRATION_CLIENT_ID
MS_REFRESH_TOKEN=PASTE_REFRESH_TOKEN
M365_OWN_DOMAINS=synthminds.ai
```

1. https://portal.azure.com → **Azure Active Directory → App
   registrations → New registration**.
2. Name: `SynthBrain`, supported account types: **Personal Microsoft
   accounts only** (for `@outlook.com`/`@hotmail.com`) or **Both** (for
   work-account too).
3. Redirect URI (mobile/desktop): `http://localhost` (any localhost works
   for personal use).
4. **API permissions** → **Add a permission → Microsoft Graph → Delegated**:
   - `Mail.Read`
   - `Calendars.Read`
   - `User.Read`
   - `offline_access`
5. **Overview → Application (client) ID** → paste into `MS_CLIENT_ID`.
6. Mint the refresh token via the
   [Microsoft device-code flow](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-device-code).
   A 30-line Python script is enough; the connector will read the
   resulting refresh token from `MS_REFRESH_TOKEN`.

`MS_TENANT_ID=common` works for personal Microsoft accounts; use your
specific tenant GUID for organization-only accounts.

### Slack (DMs + private channels)

```bash
SLACK_USER_TOKEN=xoxp-...
```

User token (xoxp-) required because DMs aren't visible to bot tokens.

1. https://api.slack.com/apps → **Create New App → From scratch** →
   pick your workspace.
2. **OAuth & Permissions → User Token Scopes** → add:
   - `channels:history`, `groups:history`, `im:history`, `mpim:history`
   - `channels:read`, `groups:read`, `im:read`, `mpim:read`
   - `users:read`
3. **Install to Workspace** → approve → copy the **User OAuth Token**
   (starts with `xoxp-`) into `SLACK_USER_TOKEN`.

### Anthropic (LLM tiebreaker + dossier synthesis)

```bash
ANTHROPIC_API_KEY=sk-ant-PASTE_KEY
```

https://console.anthropic.com → **API Keys**. Enables:
- the email-filter LLM tiebreaker for ambiguous messages
- the default `synthesize_dossier` hook (HUD bullets)
- the opt-in pass-2 layer classifier (`brain ingest --llm-classifier`)

Without this, the brain still runs end-to-end on heuristics — just less
sharp.

### OpenAI (cloud embeddings)

```bash
OPENAI_API_KEY=sk-...
```

Only needed if you use `brain ingest --embedder openai`. Default is
`--embedder fake` (offline, deterministic, fine for development);
`--embedder local` is the on-device path for production glasses-mode.

## 3. Load the file before running

The Python brain reads `os.environ` directly. Pick one of these:

### A) Load in shell every time (simplest)

```bash
cd second-brain
set -a; . ./.env.local; set +a
python -m brain.cli --entdb ./entities.db ingest --adapter gmail
```

`set -a` makes every assignment in the file exported (so the subprocess
sees them). `set +a` turns that off again for safety.

### B) `direnv` auto-loads on `cd` (recommended for daily use)

```bash
brew install direnv         # if not already
cd second-brain
echo 'dotenv .env.local' > .envrc
direnv allow
```

Now every shell that enters `second-brain/` has the env loaded
automatically. Add `eval "$(direnv hook bash)"` (or `zsh`) to your shell
rc to enable.

### C) One-off prefix

```bash
env $(grep -v '^#' .env.local | xargs) \
    python -m brain.cli ingest --adapter slack
```

## 4. Verify (without exposing values)

```bash
cd second-brain
set -a; . ./.env.local; set +a

# Prints which env vars are set; never the values:
env | grep -E '^(FIELDY|GOOGLE_OAUTH|ANTHROPIC|IMAP|GITHUB|MS_|SLACK)' | cut -d= -f1
```

## 5. GitHub Actions (the hourly cron)

`.github/workflows/sync-entities.yml` runs hourly. It expects the SAME
variable names in repo secrets at:

```
https://github.com/SynthmindsLLC/SynthBrain/settings/secrets/actions
```

Each secret is opt-in — when a step's required secret is absent the
workflow skips it gracefully. Recommended order to wire:

1. `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`,
   `GOOGLE_OAUTH_REFRESH_TOKEN` → activates Calendar + People + (optional)
   Gmail + Drive sync.
2. `GMAIL_ENABLED` = `true` → flips on the Gmail step.
3. `ICLOUD_IMAP_USERNAME`, `ICLOUD_IMAP_PASSWORD`, `IMAP_OWN_DOMAINS` →
   activates the iCloud step.
4. `ANTHROPIC_API_KEY` → activates the LLM tiebreaker in email filter +
   dossier synthesis.

## 6. Common gotchas

- **`source` requires `set -a` to export.** Without it the values are
  read but not visible to Python subprocesses.
- **No quotes around values.** `FIELDY_API_KEY=sk-f-xyz`, not
  `FIELDY_API_KEY="sk-f-xyz"`. The dotenv loader passes quotes through.
- **No trailing whitespace** after values.
- **Apple's app-specific password** has dashes: `xxxx-xxxx-xxxx-xxxx`.
  Paste with the dashes; the IMAP server expects them.
- **Google refresh tokens in Testing mode last 7 days.** Re-mint via the
  Playground; the connector fails loud with a 400 when it needs renewal.
- **`.env.local` is gitignored.** If `git add .env.local` errors with
  "ignored", that's correct — never override with `-f`.
