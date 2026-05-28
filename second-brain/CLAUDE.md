# CLAUDE.md — Second Brain (intake conduit → Even G2 glasses)

This is the project context for Claude Code. Read it fully before touching code.
Companion: chat-side design history lives in Mem note **"Second Brain — Vision &
Architecture"** (collection: Synapse Sessions).

---

## What this is

A personal **second brain**: an intake conduit that ingests Wes's information from
every source — past (Drive, hard drive, M365), present (Claude/ChatGPT exports,
Granola, FieldyAI), and eventually ambient — normalizes it, tags it, indexes it,
and serves **rapid retrieval**. The end consumer is a pair of **Even Realities G2
smart glasses** that surface recall on the lens based on what they hear.

The **north-star use case** is the *person dossier*: mid-conversation the glasses
hear a name + a context cue ("Jeff" + "the party last fall") and pop a card —
full name, work/family, where you met, what you discussed.

> Prototype scope: privacy/legal is **deliberately parked** for now (owner's call).
> It is a hard gate before anything records other people in production — see ROADMAP.

---

## The one architectural decision everything hangs on

**The canonical brain is a LOCAL index the owner controls. Mem is just ONE source
feeding it — not the brain.** (This intentionally overrides the uploaded G2
research, which assumed Mem was canonical and LanceDB a mirror. Mem can't ingest
ChatGPT exports, crawl a hard drive, or hold FieldyAI transcripts, so it can't be
canonical.)

## Two stores, two jobs — do not conflate them

| Store | Tech | Answers | Holds |
|---|---|---|---|
| **Vector index** | LanceDB (on disk) | "what's similar?" | text **chunks** |
| **Entity graph** | SQLite | "who is this / what's connected?" | **entities + edges** |

The dossier is a **graph JOIN** (resolve person → resolve event → find the
conversation linking both), not a similarity search. That's why the graph store
exists. Edges can point at chunk IDs, so the graph rides on top of the vectors.

## The pattern: SynthOS, pointed at knowledge

Generic core + swappable adapters. **Behavior in code, identity in data.** Adding
a source = writing one adapter that satisfies a base contract; the core never
changes. (Same pattern as the owner's SynthOS platform.)

```
SOURCES → ADAPTERS → NORMALIZE → TAG+EMBED → INDEX (LanceDB chunks / SQLite entities) → RETRIEVE
                                                                          ├─ chat (now)
                                                                          └─ glasses (Phase 4)
```

---

## Repo map

```
brain/
  core/
    schema.py      MemoryChunk + LanceDB arrow schema  [the chunk contract]
    embed.py       Embedder protocol: fake | local | openai  [swappable]
    tag.py         two-pass tagging (project/entities + Context-Graph layer)
    pipeline.py    RawDoc → header-aware chunks → tag → index
    index.py       BrainIndex: LanceDB add/query (semantic + layer + project filters)
    entities.py    Entity, Edge, EntityStore (SQLite graph: merge-on-conflict, traversal)
    resolve.py     ✅ noisy-OR over graph proximity + distinctive-attr + embedding
    dossier.py     ✅ graph join + HUD-budget card (synthesis hook in synthesize.py)
    synthesize.py  ✅ Anthropic Haiku hooks (classify_layer_llm, synthesize_dossier)
    salience.py    ✅ tfidf + recency + entity + layer + context noisy-OR (Phase 3 prep)
    checkpoint.py  ✅ per-adapter sync-state store (SQLite)
  api.py           ✅ FastAPI HTTP surface (/resolve, /dossier, /who, /query, /graph)
  adapters/
    base.py             Adapter ABC (text/chunk sources)
    entity_base.py      EntityAdapter ABC + ingest_entities
    mem_adapter.py      ✅ Mem markdown export → chunks (+ MemApiAdapter stub)
    contacts_adapter.py ✅ .vcf → Person entities
    calendar_adapter.py ✅ .ics → Event entities + 'attended' edges
    fieldy_adapter.py   ✅ REST + checkpoint (MCP path queued)
    filesystem_adapter.py ✅ md/txt/docx/pdf + mtime checkpoint
    claude_adapter.py   ✅ conversations.json
    chatgpt_adapter.py  ✅ conversations.json
    gcal_live_adapter.py   ✅ Google Calendar API + syncToken (incremental)
    people_live_adapter.py ✅ Google People API + syncToken (incremental)
    drive_adapter.py    ✅ Google Drive changes API + content extract
    granola_adapter.py  ✅ JSON export + markdown summaries
  cli.py           ingest | ingest-entities | query | entities | who | resolve |
                   dossier | checkpoints | serve | stats
tests/             pytest, offline (every external API mocked); 99 passing
docs/              g2-r1-reference-architecture.md, context-graph-klarity.pdf
sample_*           runnable demo data
```

## Run / test

```bash
pip install -e .            # or: pip install -r requirements.txt
pytest -q                   # 7 tests, offline
python -m brain.cli ingest --adapter mem --source ./sample_mem_export
python -m brain.cli ingest-entities --kind contacts --source ./sample_contacts.vcf
python -m brain.cli ingest-entities --kind calendar --source ./sample_calendar.ics
python -m brain.cli who "Jeff Torres"
python -m brain.cli query "why did we pick the enclosure?" --layer reasoning
```

---

## Status

**Built + tested (Phases 0-3 mostly landed):** chunk schema, LanceDB index
(semantic/layer/project queries), header-aware chunking, pass-1 + pass-2
tagging (heuristic + opt-in Claude Haiku), entity graph store, Mem adapter,
Contacts (.vcf) + Calendar (.ics) adapters, **Fieldy + Filesystem + Claude
+ ChatGPT + Drive + Granola chunk adapters**, **live Google Calendar +
People entity adapters with syncToken**, **resolve() + dossier()** with
noisy-OR scoring + HUD-budget enforcement, **FastAPI HTTP surface**
(/resolve, /dossier, /who, /query, /graph), **salience layer** (tfidf +
recency + entity + layer + context-overlap). **99 offline tests passing.**

**Still ⬜ (in priority order):**
1. M365 adapter — if still in use (OneDrive + Outlook calendar).
2. Re-point apps/web at the Python brain — `lib/brain-http.ts` lands in
   this PR; UI surfaces (search bar, dossier card) come next.
3. Latency-budget logging on the FastAPI surface; deploy target choice
   (companion app on phone vs always-on box) — `docs/g2-r1-...md` §Phase 4.
4. Even Hub SDK wiring — `even-hub/` has the structural scaffold (beat
   stream, salience pre-filter, brain client, HUD render) and a
   deterministic replay; the Hub SDK + STT integration lands when SDK
   access + privacy gate clear.
5. Privacy gate before any real recording of others — CT all-party
   consent + Navy OPSEC review.

---

## Engineering conventions (owner's standards)

- DRY, well-tested, **engineered enough** (not over, not under).
- **Edge cases > speed. Explicit > clever.** Modular & swappable. Security by default.
- Parameterized DB queries — never string-concat user data into SQL. (Note: the
  LanceDB `delete` filter in `index.py` interpolates sha1 IDs — safe because they're
  hashes, but prefer a parameterized/escaped path if LanceDB adds one.)
- Env-managed secrets, never hardcoded (`OPENAI_API_KEY`, `MEM_API_KEY`).
- Validate inputs at boundaries; structured errors.
- Conventional Commits. GitHub Actions CI runs pytest (see `.github/workflows`).
- Watch the known AI pitfalls: package hallucination (verify imports), missing
  edge cases, tests that assert nothing meaningful, timezone bugs (entities/chunks
  store tz-aware UTC ISO — keep it that way).

## Gotchas already handled (don't re-discover these)

- **LanceDB teardown segfault:** LanceDB 0.32 + pyarrow ≥18 segfaults at
  interpreter shutdown (results are correct; only the exit code). Guards in place:
  `pyarrow<18` pin in deps + the CLI hard-exits via `os._exit`. Keep both.
- **vCard escaping:** real .vcf exports escape `,` and `;` as `\,` `\;`; vobject
  handles them. Hand-written test data must escape too.
- **Embedder default is `fake`** (offline, deterministic) so tests/CI need no model
  or API key. Real recall: `--embedder local` (private, for glasses mode) or
  `--embedder openai`. The fake embedder is NOT semantic-grade — never benchmark
  retrieval quality with it.

## Reference docs (in `docs/`)

- **g2-r1-reference-architecture.md** — the Synthminds deep-research report. The
  Phase 3–4 build doc: Deepgram Nova-3 / on-device Whisper STT, salience layer
  (flagged as the unsolved research problem), Gemini Flash-Lite / Haiku synthesis,
  15-second beat, 3–5 bullet HUD, Even Hub SDK, R1 `DOUBLE_CLICK_EVENT` = stop.
  Note: it assumes Mem-canonical; we overrode that (see above).
- **context-graph-klarity.pdf** — the mental model (NOT a product to buy). Nodes +
  edges; the L3 "tribal knowledge" layer (decisions, reasoning, workarounds) is why
  pass-2 tagging and the entity graph exist. "Human reasoning doesn't emit data."
