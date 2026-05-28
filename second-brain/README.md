# Second Brain — Phase 0 Spike (the Spine)

The runnable spine of the intake conduit: a **canonical local index you own**,
fed by **swappable source adapters**, queried by chat now and the **Even G2
glasses** later. This is Phase 0 — the index + one adapter (Mem) + a query CLI.
It works and it's tested.

> Architecture note: this flips the assumption in the G2 research. The brain is
> **not** "a mirror of Mem." The brain is the local index; **Mem is just the
> first source feeding it.** Drive, M365, the hard drive, ChatGPT/Claude exports,
> Granola, and Fieldy all become additional adapters writing into the same index.

## The shape

```
SOURCES → ADAPTERS (@brain/adapter-*) → NORMALIZE → TAG+EMBED → INDEX (LanceDB) → RETRIEVE
                                                                          ├─ chat (now)
                                                                          └─ glasses (Phase 4)
```

Same pattern as SynthOS: behavior in the core, identity in the adapter. Every
source normalizes into one record — the **MemoryChunk**
(`brain/core/schema.py`): `text, source, source_id, url, created_at,
project_tags[], entity_tags[], layer, embedding`.

Tagging happens at ingest, two passes (`brain/core/tag.py`):
- **Pass 1** (cheap): project wing + entities.
- **Pass 2** (the valuable one): the Context-Graph layer —
  `artifact | decision | reasoning | workaround`. This is what lets the glasses
  surface *"why you decided X"* instead of *"a file named X."*

## Two stores, two jobs

- **LanceDB (vector index)** — "what's similar." Text chunks from Mem/Drive/etc.
- **SQLite (entity graph)** — "who is this, what are they connected to." People and
  events as nodes; `attended` / `mentioned_in` / etc. as edges. The **dossier**
  use case ("Jeff at the party last fall") is a graph join, not a similarity
  search, so it lives here.

## Run it (60 seconds)

Text side (the spine):
```bash
pip install -r requirements.txt
python -m brain.cli ingest --adapter mem --source ./sample_mem_export
python -m brain.cli query "what were the MOA consignment terms?"
python -m brain.cli query "why did we pick the enclosure?" --layer reasoning
```

Entity side (the dossier rails):
```bash
python -m brain.cli ingest-entities --kind contacts --source ./sample_contacts.vcf
python -m brain.cli ingest-entities --kind calendar --source ./sample_calendar.ics
python -m brain.cli who "Jeff Torres"          # contact details + events attended + co-attendees
python -m brain.cli entities --name Jeff        # NOTE: returns TWO Jeffs — the disambiguation gap
python -m brain.cli stats
```

`who "Jeff Torres"` already assembles the raw dossier: org, title, family note,
the Fall Block Party he attended, and who else was there. What it does **not** yet
do is resolve a *bare* "Jeff" to the right person from conversation context —
that's `resolve()`, the next step.

Seed real data: export contacts as **.vcf** (iPhone/Google/Outlook all do this)
and calendar as **.ics**; point `--source` at them.

```bash
pytest -q     # 7 tests, offline
```

## What's real vs. stubbed

| Piece | State |
|---|---|
| MemoryChunk schema, LanceDB index, query (semantic + layer + project filters) | ✅ working, tested |
| Header-aware chunking, pass-1 tagging | ✅ working |
| Pass-2 layer classification | ⚠️ heuristic; swap for an LLM in Phase 2 |
| Mem adapter (Markdown export) | ✅ working |
| **Entity graph store (SQLite): nodes, edges, merge-on-conflict, traversal** | ✅ **working, tested** |
| **Contacts adapter (.vcf → Person)** | ✅ **working, tested** |
| **Calendar adapter (.ics → Event + attended edges)** | ✅ **working, tested** |
| **`resolve(mention, context)` — pick the right Jeff** | ⬜ **next step** — the hard record-linkage problem |
| **`dossier()` — synthesize the popup card** | ⬜ next step (needs `resolve()` + LLM synthesis) |
| Mem API incremental sync | 🔌 stub — Phase 3 |
| Drive / hard-drive / M365 / Claude / ChatGPT / Fieldy adapters | ⬜ Phase 1–2 |
| Embedders: fake / local / openai | ✅ all three |

## Known issue handled

LanceDB 0.32 + pyarrow can segfault during interpreter teardown (a native
shutdown race; results are correct, only the exit code is affected). Two guards:
`requirements.txt` pins `pyarrow<18`, and the CLI hard-exits past the destructors.

## Phase plan

- **Phase 0 — Spine (this).** Index + Mem adapter + CLI. ✅
- **Phase 1 — Past.** Drive, hard-drive (Filesystem), M365 adapters. One per session.
- **Phase 2 — Present.** Claude export, ChatGPT export, Granola, Fieldy adapters + the LLM layer classifier. This is where your *reasoning* lives — highest value for glasses recall.
- **Phase 3 — Retrieval surface.** Salience layer + synthesis + the latency budget from the G2 research. Test in chat.
- **Phase 4 — Glasses.** Even Hub plugin + STT + HUD. The uploaded G2 research is the build doc, unchanged except it queries *this brain* instead of Mem.

## Handoff → Claude Code

This is the design spike. The ongoing build — Phases 1–4, real adapters,
incremental sync, the glasses plugin — is production code and belongs in **Claude
Code under CLAUDE.md**, not in chat. Drop this folder into a repo and continue
there. The adapter contract (`brain/adapters/base.py`) is the only thing each new
source needs to satisfy.
