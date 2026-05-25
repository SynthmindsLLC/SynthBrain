# @synthbrain/connector-vault

Imports the legacy Obsidian vault into Mem.ai, folder by folder. Codifies the
transform rules proven in the `04 - 🤖 Prompts` pilot (see
`docs/ingestion/04-prompts-pilot.md`).

## What it does

1. Walks a vault folder for `.md` files.
2. **Classifies** each: `migrate` / `exclude-drawing` (Excalidraw `.md`) /
   `drop-duplicate` (exact-content dupes like Obsidian's ` 1.md` copies).
3. **Transforms** each migrate file into a Mem note:
   - strips Obsidian frontmatter, merges its `tags` into the inline tag line
   - title = filename (emoji preserved)
   - `Tags:` line carries `#source/vault #type/reference #domain/... #group/<subfolder> #status/active|wip` + frontmatter tags
   - **escapes `<…>` angle brackets** when present so Mem stores XML/placeholder
     prompts verbatim (Mem's sanitizer otherwise strips `<tag>`)
4. **Writes** to Mem via HTTP, in batches, with a progress summary.

## Usage

```bash
# Dry-run (default — no writes, logs intended notes):
pnpm --filter @synthbrain/connector-vault start -- \
  --folder "/home/user/SynthBrain/04 - 🤖 Prompts" \
  --collection "Reference/Prompts"

# Commit (requires MEM_API_KEY in env):
MEM_API_KEY=... pnpm --filter @synthbrain/connector-vault start -- \
  --folder "/home/user/SynthBrain/04 - 🤖 Prompts" \
  --collection "Reference/Prompts" --commit
```

Flags: `--folder` (required), `--collection`, `--commit`, `--base-tags`,
`--batch-size`.

## Notes

- **Dry-run is the default.** `--commit` is required to write.
- Large files (e.g. the 6.5k-word Professor Synapse, 5k-word arXiv taxonomy)
  stream straight from disk to the Mem HTTP API — they never pass through an
  LLM context, which is exactly why bulk/large-file ingestion belongs here
  rather than in chat.
- Idempotency across re-runs (external_id → mem_note_id index) is the next
  addition; today a re-run would create duplicates, so commit a folder once.
