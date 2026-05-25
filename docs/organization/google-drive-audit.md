# Google Drive — Organization Audit

> Read-only audit of `wes@synthminds.ai` My Drive. Recommendations are **proposed, not yet executed** — reorganizing a live Drive is destructive-adjacent, so moves/merges/deletes wait for explicit go (and a move-capable tool; see "Tooling note").

## Headline findings

- **~65 top-level folders**, the majority of which are **dormant desktop-app cruft** auto-created in 2022–2023 (Adobe, WhirlwindFX, iZotope, SOLIDWORKS, Syncios, dr.fone, JoyToKey, STAR WARS Squadrons, My Games, Horizon Zero Dawn, vMixStorage, TASCAM, ATEM Autosave, WindowsPowerShell, Custom Office Templates, Zoom, Outlook/Outlook Files, Topaz, Picsio, Wolow Companion).
- **100+ loose files sitting in My Drive root** — no folder. PDFs, CSVs, docx, Google Docs, zips, and several **very large videos** (`recording1.mp4` 472 MB, two Zoom `GMT…mp4` 323 MB + 261 MB, a 315 MB session zip) all loose at the root.
- **Duplicate folders:** `Saved from Chrome` exists **twice**; `Box Import` and `Box import` (case-only difference).
- **Duplicate files:** `Plants By The Village — Design System (Print).pdf` appears **twice** (13 MB and 40 MB versions); multiple `Synthminds Fact Sheet` variants; `Wes Bio Slide` in 3 formats (pdf/pptx/gslides).
- **Mem-ingestion sources hiding in Drive:** lots of **prompt docs** loose in root (Prompting Principles, Prompt Hacking, Prompt Library Samples, Resume Metaprompt, Recursive Reprompting Example, Prompt Evaluation Prompt, Learning With Prompting) → these should also flow into the Mem `Reference/Prompts` collection. Plus `Obsidian/`, `Fireflies Meetings/`, `Meet Recordings/` folders.

## Proposed taxonomy (mirrors the Mem collection scheme)

```
My Drive/
├── Projects/            active build work
│   ├── PBTV/            ← pbtv-pdp-photos-*, Pbtv-icloud, + all loose PBTV files
│   ├── Main Page Vid/
│   └── Image course/
├── Clients/
│   ├── ISOC-Navy/       ← NAVSUP PDFs, curriculum maps, ISOC pptx/docx (loose in root now)
│   ├── Internova/  Morpheme/  Whidbey Vet Orders/  Ai_Sentinel/
│   └── _Proposals/      ← Vecorsense, STAR Support, District Proposal, Pitches/
├── Reference/
│   ├── Prompts/         ← all loose prompt docs (also → Mem Reference/Prompts)
│   ├── BrandProfiles/  Logos/  2.0 resources/
│   └── Dev/             ← Code, GitHub, Colab Notebooks, Opal
├── Knowledge/           Mem ingestion sources
│   ├── Obsidian/   .obsidian/   excalidraw/
│   └── Meetings/        ← Fireflies Meetings, Meet Recordings, YU meeting
├── Finance/             ← SM LLC Statements, Bank, Invoices, 2023 Taxes, pricelist, WES_Synthminds_LLC
├── Personal/            ← resumes, cover letters, bio slides
├── Media/
│   └── Recordings/      ← the large loose .mp4 / session zips
└── _Archive/
    └── _AppData/        ← all dormant desktop-app installer folders (2022–23)
```

## Action plan (by batch, each needs go-ahead)

1. **Dedupe (safe, high-value):**
   - Merge `Saved from Chrome` (×2) → one.
   - Merge `Box Import` + `Box import` → one.
   - Resolve `Plants By The Village — Design System (Print).pdf` (keep the 40 MB; the 13 MB looks like a re-export) — confirm before deleting either.
2. **De-clutter root:** move the 100+ loose files into the taxonomy above (PBTV → Projects/PBTV, NAVSUP/ISOC → Clients/ISOC-Navy, prompt docs → Reference/Prompts, proposals → Clients/_Proposals, finance → Finance/, big videos → Media/Recordings).
3. **Archive app cruft:** move the ~25 dormant desktop-app folders into `_Archive/_AppData/`. None touched since 2022–23; none referenced by active work.
4. **Cross-ingest to Mem:** the loose **prompt docs** + `Obsidian/` + meeting folders feed the same Mem collections the vault connector targets.

## Tooling note

The connected Google Drive MCP exposes **read + copy + create**, but **no move / rename / delete / set-parents** operation. So I can audit and recommend (done), and I can *copy* files into new folders, but I can't cleanly *move* or *dedupe* without either:
- a move-capable Drive tool/scope (preferred), or
- you running the moves, or
- a small Drive-organizer script using the Drive API `files.update?addParents/removeParents` with an OAuth token.

**Recommend:** add the move/trash scope to the Drive connector so the vault connector's sibling `apps/connectors/drive` can execute this plan idempotently (and ingest docs to Mem in the same pass). Until then this doc is the approved-pending blueprint.
