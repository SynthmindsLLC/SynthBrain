# @synthbrain/connector-drive

Move-capable Google Drive organizer. Executes the plan in
`docs/organization/google-drive-audit.md`: declutters My Drive root into a
clean taxonomy, archives dormant desktop-app folders, and trashes exact
duplicates — all reversibly and dry-run-first.

## Why this exists

The connected Drive **MCP** is read + copy + create only (no move/rename/
trash), so it can't declutter without duplicating. This connector uses the
Drive **REST API** directly:

- **move** → `files.update(addParents, removeParents)` (true move, not copy)
- **rename** → `files.update(name)`
- **delete** → `files.update(trashed: true)` (reversible — goes to Drive Trash)

## Auth

OAuth2 refresh token with the `https://www.googleapis.com/auth/drive` scope:

```
GOOGLE_OAUTH_CLIENT_ID=…
GOOGLE_OAUTH_CLIENT_SECRET=…
GOOGLE_OAUTH_REFRESH_TOKEN=…
```

## Usage

```bash
# Dry-run (default — logs every intended move/rename/trash, no writes):
pnpm --filter @synthbrain/connector-drive start

# Apply, including duplicate cleanup:
pnpm --filter @synthbrain/connector-drive start -- --commit --dedupe
```

## What it does

1. Lists My Drive root.
2. `--dedupe`: groups files by `md5Checksum`, keeps the largest, **trashes** the
   rest (reversible).
3. For each root item, `classifyToTarget` (see `taxonomy.ts`) picks a destination:
   - PBTV files/folders → `Projects/PBTV`
   - NAVSUP/ISOC course material → `Clients/ISOC-Navy`
   - prompt docs → `Reference/Prompts`
   - proposals → `Clients/_Proposals`
   - finance → `Finance`, resumes/bios → `Personal`
   - large videos/zips → `Media/Recordings`
   - dormant desktop-app folders → `_Archive/_AppData`
4. Creates the destination folders on demand and **moves** items in.
5. Renames Obsidian ` 1` duplicate-suffix files.
6. Prints a summary; unmatched items are left in place and flagged `[review]`.

## Safety

- **Dry-run is the default.** `--commit` required to write.
- Deletes are **trash**, not permanent — recoverable from Drive Trash.
- Unmatched items are never touched.
- Next: a second pass to ingest the doc/prompt files it relocates into the
  matching Mem collections (shares the vault connector's transform).
