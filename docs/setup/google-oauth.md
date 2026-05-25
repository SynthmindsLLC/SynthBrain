# Google OAuth — refresh token for the Drive connector

`apps/connectors/drive` needs an OAuth2 refresh token with the
`https://www.googleapis.com/auth/drive` scope (full move/rename/trash). Below
is the fastest path (OAuth Playground). One-time setup.

## 1. Enable the Drive API
1. https://console.cloud.google.com → select or create a project.
2. **APIs & Services → Library** → search **Google Drive API** → **Enable**.

## 2. OAuth consent screen
1. **APIs & Services → OAuth consent screen** → User type **External** → create.
2. App name + your support email → Save.
3. **Scopes** → Add → `https://www.googleapis.com/auth/drive` → Save.
4. **Test users** → add `wes@synthminds.ai`.
   - ⚠️ In "Testing" mode, refresh tokens for restricted scopes **expire after 7 days**. For ongoing use, click **Publish app** (no Google verification needed for a single-user/internal app you own), which makes the refresh token long-lived.

## 3. Create OAuth client credentials
1. **APIs & Services → Credentials → Create Credentials → OAuth client ID**.
2. Application type: **Web application**.
3. **Authorized redirect URIs** → add `https://developers.google.com/oauthplayground`.
4. Create → copy the **Client ID** and **Client secret**.
   → these become `GOOGLE_OAUTH_CLIENT_ID` and `GOOGLE_OAUTH_CLIENT_SECRET`.

## 4. Mint a refresh token (OAuth Playground)
1. Go to https://developers.google.com/oauthplayground.
2. Top-right **⚙ (gear)** → check **Use your own OAuth credentials** → paste the Client ID + secret.
3. Left panel **Step 1**: in "Input your own scopes" enter
   `https://www.googleapis.com/auth/drive` → **Authorize APIs** → sign in as
   `wes@synthminds.ai` → Allow.
4. **Step 2**: click **Exchange authorization code for tokens**.
5. Copy the **Refresh token** → this is `GOOGLE_OAUTH_REFRESH_TOKEN`.

## 5. Mem API key (for `--ingest`)
- https://mem.ai → Settings → **API / Integrations** → create an API access token
  → this is `MEM_API_KEY`.

## 6. Put it all in `.env.local` (gitignored)
```
GOOGLE_OAUTH_CLIENT_ID=…
GOOGLE_OAUTH_CLIENT_SECRET=…
GOOGLE_OAUTH_REFRESH_TOKEN=…
MEM_API_KEY=…
```

## 7. Run it
```bash
# Dry-run first — logs every intended move/rename/trash/ingest, writes nothing:
pnpm --filter @synthbrain/connector-drive start

# Apply: declutter + dedupe + ingest docs into Mem:
pnpm --filter @synthbrain/connector-drive start -- --commit --dedupe --ingest
```

Deletes are Drive **Trash** (reversible). Unmatched items are left untouched.
The same `MEM_API_KEY` also runs the vault importer
(`pnpm --filter @synthbrain/connector-vault start -- --folder … --commit`).
