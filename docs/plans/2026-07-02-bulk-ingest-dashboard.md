# Build Plan — Bulk Historical Ingest + Second-Brain Dashboard (2026-07-02)

**Directive (Wes):** ingest tons of historical info through the pipeline for
classification, then visualize the second brain working. Full autonomy granted;
decisions below are made and documented, not queued for approval.

## Decisions (locked for this build)

| #   | Decision                                                                                                                                                                                                                                                                                         | Rationale                                                                                                                                           |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| A1  | **Embedder = `local`** (BAAI/bge-small-en-v1.5, 384-dim, MPS) for ALL bulk ingest and the served API (`BRAIN_EMBEDDER=local`).                                                                                                                                                                   | Free, offline, semantic-grade, private (no content leaves the machine). Embedder dim is baked into the LanceDB table — never start bulk on `fake`.  |
| A2  | **Canonical data paths:** `second-brain/data/brain_index` (LanceDB) + `second-brain/data/entities.db` (SQLite), absolute via `BRAIN_DB`/`BRAIN_ENTDB` everywhere. Gitignored (`brain_index/`, `*.db` already covered; `data/` added).                                                            | Kills the two-disjoint-brains failure mode (CWD-relative defaults).                                                                                 |
| A3  | **PROJECT_KEYWORDS extended additively** in `tag.py`: synaptic-labs, synthsidian, jasmmm, verizon, anvl, synthbrain.                                                                                                                                                                             | Historical corpora reference these; additive = zero loss; deterministic chunk ids make re-ingest cheap if Wes prunes later. Flagged for his review. |
| A4  | **Classification = heuristic** for bulk wave 1; LLM re-classification deferred to an optional batched pass.                                                                                                                                                                                      | `--llm-classifier` is 1 sync Haiku call/chunk; ~15–40k chunks is impractical. Ledger records heuristic/llm counters so quality work is measurable.  |
| A5  | **PII policy for wave 1:** local file corpora ingested broadly EXCEPT bank/tax/financial-statement documents (excluded by path/filename pattern); Drive cloud-stub mirror NOT bulk-ingested (would hydrate ~1GB+; live `drive` adapter later). iMessage deferred (needs Full Disk Access grant). | Vision says "intake ALL information" and the brain is local + local embedder; financial account docs carry outsized risk for zero recall value.     |
| A6  | **Dashboard = new `/dashboard` route in `apps/web`**, inline-style glassmorphism matching the existing design language. **No Tailwind.** 21st.dev MCP consulted for inspiration only.                                                                                                            | The app has zero Tailwind; bolting it on for one page is stack churn.                                                                               |
| A7  | **Dashboard data flows through Next server-side proxies** (`/api/*` → brain HTTP). No CORS opening on the brain.                                                                                                                                                                                 | Proxy pattern already exists; keeps bearer token server-side.                                                                                       |
| A8  | Overlay row "Dashboard/analytics? **No**" is **superseded** by this directive.                                                                                                                                                                                                                   | Wes asked for it explicitly (2026-07-02).                                                                                                           |

## Corpora plan (wave 1 — zero-credential, all local)

| Order | Adapter                             | Corpus                                                                   | Est.               |
| ----- | ----------------------------------- | ------------------------------------------------------------------------ | ------------------ |
| 1     | `ingest-entities contacts/calendar` | repo samples (real .vcf/.ics export = user action, later)                | seed               |
| 2     | `filesystem`                        | repo vault `~/Downloads/SynthBrain` (00–05 + Mission Control + Workshop) | 2,846 md, 238MB    |
| 3     | `filesystem`                        | Obsidian vault `.../My Drive/Obsidian/2ndBrain`                          | 768 md, 52MB       |
| 4     | `claude-code` (NEW adapter)         | `~/.claude/projects/**/*.jsonl` (exclude `alltheplants`)                 | 308 sessions, 76MB |
| 5     | `filesystem`                        | `~/Documents` + `~/Desktop`                                              | 92 files           |
| 6     | `filesystem`                        | `~/Downloads` loose docs (excl. SynthBrain repo, financial/tax patterns) | 347 files, 387MB   |

Deferred (wave 2, needs creds/user action): iMessage (FDA grant + B6 fix), live Drive,
gmail/imap (verdict persistence first), slack/github/m365, ChatGPT export, Mem export, Granola.

## Workstream PY — pipeline hardening + API (sequential: PY1 → PY2)

**PY1 (hardening):**

- **B1** Batched ingest: `pipeline.ingest()` flushes every 256 chunks; `BrainIndex.add_chunks` batches embed + delete calls (chunked `id IN` deletes, e.g. 500 ids/statement).
- **B2** `--dry-run` on `ingest`: full adapter+chunk+tag pass, prints per-source/layer/project counts + skip report, writes nothing.
- **B3+B12** `ingest_runs` ledger table (in entities.db via CheckpointStore's db): run_id, adapter, source, started/finished, status, docs, chunks, errors, skipped, llm/heuristic counts, error_samples JSON. Per-doc try/except isolation (one bad doc ≠ aborted run).
- **B7** Filesystem adapter: checkpoint key namespaced per source dir (hash); skip events logged + counted (oversize, unsupported ext, extractor missing/failed).
- **D5** api.py: validate `layer` against LAYERS, reject quotes in `project`; SQLite `check_same_thread=False` + lock (or per-request conn).
- Tests for all of the above; suite stays green.

**PY2 (adapter + endpoints), after PY1:**

- **B11** `claude_code_adapter.py`: parses Claude Code session JSONL (`~/.claude/projects/<proj>/<session>.jsonl`; lines are JSON events; extract user/assistant message events, render `**speaker:** text` per claude_adapter idiom; skip meta/tool noise; source_id = session filename stem; mtime checkpoint; `--source` = projects root; skip dirs containing `node_modules`).
- **B9** Entity canonicalization at ingest: after `tag_entities`, exact/alias-match names against EntityStore; append matched `kind:slug` ids to `entity_tags` (keep raw names).
- **D1** `GET /stats/breakdown` → `{chunks_total, by_source{}, by_layer{}, by_project{}, by_day[{date,chunks}], entities{total,by_kind{}}, edges{total,by_rel{}}, generated_at}` (LanceDB `to_arrow()` scan + SQLite counts; 30s in-process cache).
- **D2** `GET /ingest/runs?limit=` → `{runs:[…ledger rows…]}` newest-first.
- **D3** `GET /chunks/recent?limit=&source=&layer=` → `{chunks:[{id, text≤400chars, source, source_id, url, layer, project_tags, entity_tags, created_at}]}`.
- **D6** `/graph`: add `kind` + `min_degree` filters, `degree` on nodes, top-N-by-degree sampling instead of insertion-order truncation.
- Tests via TestClient; suite green.

## Workstream WEB (parallel with PY)

- **D8** Extend `packages/graph-schema` Zod: node kinds + `person|event|place|org`, link kinds + brain RELS (`attended|mentioned_in|discussed_with|works_at|family_of`); fix `mem-source.ts` lossy mapping + HUD filter for brain graphs.
- **D10** Scope `touch-action:none`/`overscroll-behavior:none` to the graph canvas, not global.
- **D7** New `/dashboard` route, 4 glass panels on #0a0a14: **A** ingest runs/stats (ledger table + totals + per-source bars), **B** classification breakdown (layer/project/source distributions — inline SVG bars, no chart lib), **C** entity force graph (reuse existing GraphCanvas, kind colors), **D** live query bar → results list → click-through dossier card (wire existing `/api/dossier`).
- New `lib/brain-http.ts` wrappers: `brainStatsBreakdown`, `brainIngestRuns`, `brainRecentChunks`; new routes: `GET /api/stats`, `GET /api/runs`, `GET /api/recent`, `POST /api/query`.
- **D9** Lightweight polling hook (5s) for stats/runs; graceful `brain_unavailable` empty-states.
- **D11** Extend `source-colors.ts`: imessage, icloud-notes, github, m365, slack, claude, chatgpt, claude-code, filesystem, mem.
- **D12** Root `.env.example` += `BRAIN_URL`, `USE_BRAIN`, `BRAIN_BEARER_TOKEN`; commit `pnpm-lock.yaml`.
- `pnpm typecheck` + `pnpm --filter @synthbrain/web build` green.

## API contract (PY2 ↔ WEB — both sides build to THIS, not to each other)

Shapes exactly as specified in the PY2 bullets above; all new GETs honor the
existing optional bearer auth; errors follow existing `{error, message}` 503 style.

## Known constraints (do not violate)

- `pyarrow>=15,<18` pin and CLI `os._exit` guard stay.
- Agents do NOT run `git commit` — orchestrator commits at phase boundaries.
- No new Python deps (stdlib only) for PY; no new JS deps for WEB (inline SVG charts).
- Offline tests only (fake embedder, mocked externals).

## User actions pending (non-blocking, flagged to Wes)

1. Full Disk Access grant → unlocks iMessage (~100k msgs) + iCloud Notes.
2. ChatGPT export (Settings → Data controls → Export) → chatgpt adapter.
3. Contacts .vcf / real .ics export (or GOOGLE_OAUTH_* refresh token for live adapters).
4. Mem workspace export → mem adapter seeding.
5. Review A3 project-tag additions; prune if any are dead.
