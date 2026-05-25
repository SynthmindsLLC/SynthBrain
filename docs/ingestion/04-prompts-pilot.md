# Ingestion Pilot — `04 - 🤖 Prompts`

> **Dual-output dry-run.** This is the proof-of-format pass: an *ingestion manifest* (what becomes Mem notes) plus a *vault-organization report* (recommendations for the source folder). **No Mem writes have occurred.** Nothing is committed to Mem until the manifest is approved.

## Summary

- **48 `.md` files** in the folder (+ 1 `.DS_Store` junk file).
- **44 → migrate** as prompt notes into Mem.
- **3 → exclude** (Excalidraw drawings mis-filed as prompts — not prompt content).
- **1 → drop** (exact duplicate).
- 21 files have YAML frontmatter; 27 don't. Existing tags are inconsistent (`#prompt`, bare `prompt`, `CustomGPT`, etc.).

## Mem target

- **Collection:** `Reference/Prompts`
- **Tags applied to every migrated note:**
  - `#source/vault` · `#type/reference` · `#domain/prompt-engineering`
  - `#status/active` (or `#status/wip` for the 3 WIP files)
  - `#group/<subfolder>` — `#group/gpts`, `#group/arxivbot`, `#group/random` (the `Random/` group is flagged for recategorization, see below)
  - Plus the note's existing frontmatter tags, normalized (strip leading `#`, dedupe): `prompt`, `meeting`, `blog`, `education`, `texttoimage`, `metaprompt`, etc.
- **Title:** filename without `.md` (emoji preserved — Mem supports it; renames recommended below).
- **Body:** full markdown, unchanged.
- **Discipline:** `search_notes` for each title before `create_note` (read-before-write); commit in batches of ~10 with progress logging.

## Triage classification

| Action | Count | Files |
|---|---|---|
| **migrate** | 44 | all prompt `.md` except those below |
| **exclude — Excalidraw drawing** | 3 | `Compi`, `Prof Synapse Phi 3`, `🖋️ SM` (have `excalidraw` frontmatter; these are canvases, not prompts — route to the `.canvas`/attachment path later) |
| **drop — duplicate** | 1 | `Random/ArxivBot/arXiv_field_categories 1.md` (byte-identical to `arXiv_field_categories.md`; the " 1" is an Obsidian copy artifact) |
| **junk** | 1 | `.DS_Store` (should be gitignored) |

## Dry-run ingestion manifest (sample of intended `create_note` calls)

```
[1/44] Reference/Prompts ← "How I prompt"
        tags: #source/vault #type/reference #domain/prompt-engineering #status/active #group/root
        body: 1569 words · no frontmatter
        search_notes("How I prompt") → (would check for existing)

[2/44] Reference/Prompts ← "🧙🏾‍♂️Professor Synapse"
        tags: #source/vault #type/reference #domain/prompt-engineering #status/active
              #group/root #prompt #professorsynapse
        body: 6544 words · frontmatter tags merged
        ⚠ largest file; canonical of the "Synapse" family (see org report)

[3/44] Reference/Prompts ← "Meeting Notes"
        tags: … #group/root #prompt #meeting #summarize
        body: 235 words

[4/44] Reference/Prompts ← "Brutally Honest Expert (BHE)"
        tags: … #group/gpts #customgpt #gpts #prompt
        body: 491 words

[42/44] Reference/Prompts ← "PodBot (WIP)"
        tags: … #group/random #status/wip
        body: 71 words · WIP

… (full 44-row mapping generated at commit time)
```

## Vault-organization report — recommendations for `04 - 🤖 Prompts`

Read-only recommendations. **No file in the vault is moved/renamed/deleted without explicit approval.**

### 1. Remove non-prompt content
- **3 Excalidraw files** (`Compi`, `Prof Synapse Phi 3`, `🖋️ SM`) are drawings stored as `.md`. Move to a `Drawings/` area or the attachment pipeline; don't ingest as prompts.
- **`.DS_Store`** — add to `.gitignore` (already covered by the root `.gitignore` rule) and delete.

### 2. Dedupe
- `arXiv_field_categories 1.md` is an exact copy of `arXiv_field_categories.md` — delete the ` 1` copy.
- **Near-duplicate pairs** to reconcile (keep one canonical, link the other):
  - `Linkedin Post Generator` (root) vs `Synthminds - Linkedin Post Generator` (Random)
  - `✍️BlogBot` (root) vs `BlogBot (Synthminds)` (Random)

### 3. Consolidate the "Synapse" family (7 files, scattered)
`🧙🏾‍♂️Professor Synapse` (6544w, canonical), `Alignment Professor Synapse`, `Professor Synapse (Custom Instructions`, `Prof Synapse Phi 3` (excalidraw), `Synapse_TTI`, `SynapseKB WIP`, `Synapse_DB (WIP)`. → Group under one `Synapse/` subfolder (or `#group/synapse` in Mem), mark the canonical, archive the WIPs.

### 4. Dissolve `Random/` (15 files)
It's a catch-all with no organizing principle. Proposed regroup:
- **Research:** `001. Research Article Summarizer`, `ArxivBot/*`
- **Content:** `BlogBot (Synthminds)`, `Synthminds - Linkedin Post Generator`, `GIF Creator`, `Image2Text2Image`
- **Education:** `EDUBot`, `7 Minute Life Coach`
- **Obsidian/tooling:** `CoPilot Plugin Prompt`
- **Synapse:** (see §3)

### 5. Naming hygiene
- `Professor Synapse (Custom Instructions` — unclosed paren; rename.
- `GCHAT bot` — inconsistent caps → `GChat Bot`.
- Emoji prefixes appear on some titles, not others — pick a convention (recommend: keep emoji, they read well in the graph).
- WIP files — either finish, or move to an `_Archive/` subfolder and tag `#status/wip`.

### 6. Status flags
3 WIP files (`PodBot (WIP)`, `SynapseKB WIP`, `Synapse_DB (WIP)`) → `#status/wip` on the Mem note; consider archiving in-vault.

## On `--commit`

1. `create_collection("Reference/Prompts")` if absent.
2. For each of the 44 files (batches of 10): `search_notes(title)` → skip/update if exists, else `create_note` with the tag set above → `add_note_to_collection`.
3. Progress log per batch; final report: created / skipped / failed counts.
4. Excluded + dropped files listed, not written.

**Status: awaiting approval. No Mem writes yet.**
