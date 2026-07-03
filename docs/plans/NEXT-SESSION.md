# Next-Session Kickoff — SynthBrain

> Written 2026-07-03 at the end of the bulk-ingest + dashboard session.
> Read `CLAUDE.md` (root overlay) + `docs/plans/2026-07-02-bulk-ingest-dashboard.md`
>
> - `CHANGELOG.md` [Unreleased] before starting.

## Where things stand

- Branch `claude/integrate-mem-ai-1ZuZJ` (= draft PR #4) carries the whole
  project; 5 new commits pushed this session (plan, brain, web, QA fixes, perf).
- 201 Python tests + TS typecheck/vitest/build all green.
- Wave-1 bulk ingest ran against real corpora into
  `second-brain/data/{brain_index,entities.db}` (local machine only,
  gitignored) with the `local` embedder. Ledger rows in `ingest_runs`.
- Dashboard live at `localhost:3001/dashboard` when both servers run
  (see second-brain/CLAUDE.md "Run / test").

## One feature per session — pick ONE

1. **Entity enrichment (recommended next):** calendar attendees without a
   Google displayName became email-named Person entities
   (`person:joseph-synapticlabs-ai`), so dossier lookups by human name miss.
   Fix: (a) Wes exports real contacts .vcf → `ingest-entities contacts`
   merges names onto email aliases; (b) add a meta→entity pass so
   granola/imessage/slack attendees in chunk meta become Person entities +
   `mentioned_in` edges. This is the dossier-quality lever.
2. **Wave-2 corpora:** iMessage (needs Full Disk Access grant + verify the
   B6 group_idx overwrite fix that was NOT yet made — check before running),
   live Drive adapter (GOOGLE_OAUTH_*), gmail/imap (persist triage verdicts
   first), ChatGPT export (user action).
3. **LLM re-classification pass:** batched Haiku over decision/reasoning
   candidates (deterministic ids = cheap overwrite); ledger already counts
   llm vs heuristic.
4. **Draft PR #4 → ready:** repo is PUBLIC — decide visibility before
   widening; consider adding the pytest job to ci.yml (still missing).

## Open user actions (blocking specific items only)

Full Disk Access (iMessage/Notes) · ChatGPT export · contacts .vcf export ·
Mem workspace export (or keep MCP-harvest snapshots) · review the additive
PROJECT_KEYWORDS (tag.py) · repo visibility decision.

## Gotchas added this session (beyond the standing ones)

- Data + embedder: `second-brain/data/*`, `--embedder local` everywhere;
  BrainIndex now hard-fails on dim mismatch.
- Adapters with deferred watermarks (filesystem, claude-code): the CLI
  commits checkpoints only after a clean zero-error run; errored runs hold
  the watermark on purpose.
- Never add per-name EntityStore scans inside the chunk loop — build a map
  upfront (see `_build_canon_map`); the per-name version stalled a 70k-chunk
  run.
- The Anthropic monthly spend limit was hit during this session's QA
  workflow (8 verifier agents died) — check remaining budget before
  launching large agent fan-outs.
