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
5. **Keep Publishing status = "Testing". Do NOT publish.**
   - `auth/drive` is a **restricted** scope. Google only demands the
     verification/branding process (Verification Center) when the app is
     **In production / Published**. In **Testing** you skip all of that.
   - Trade-off: in Testing, a `drive`-scope refresh token lasts **7 days**,
     then re-mint via step 4. Fine for running the reorg on demand.
   - During consent in the Playground you'll see "Google hasn't verified this
     app" → **Advanced → Go to {app} (unsafe) → Allow**. Safe — it's your own app.
   - If you already clicked Publish and landed in the Verification Center:
     go back to the consent screen and click **Back to testing**.

> **Durable alternative (no 7-day expiry, no consent screen):** a **service
> account**. Since `synthminds.ai` is a Google Workspace domain you own, you can
> either (a) enable domain-wide delegation for the service account in the
> Workspace Admin console, or (b) simply **share the Drive folders with the
> service account's email**. Then the connector authenticates with the service
> account JSON key — long-lived, no verification. Slightly more setup; best for
> scheduled/recurring runs.

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
