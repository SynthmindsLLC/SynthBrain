# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added — 2026-07-02/03 bulk-ingest + dashboard session

- **Bulk ingestion hardening** (`second-brain/`): batched embed/upsert
  (flush 256 / embed 128 / delete 500), `--dry-run` with per-source/layer/
  project preview and skip reports, `ingest_runs` SQLite ledger with
  llm-vs-heuristic classification counters, per-doc error isolation,
  per-directory checkpoint namespacing, `--exclude` patterns.
- **`claude-code` adapter**: ingests Claude Code session transcripts
  (`~/.claude/projects/**.jsonl`) as conversational chunks.
- **Entity canonicalization at ingest**: extracted names resolve against the
  entity graph and canonical `kind:slug` ids join `entity_tags`.
- **Dashboard API**: `GET /stats/breakdown` (source/layer/project/day +
  entity/edge kind counts, 30s cache), `GET /ingest/runs`,
  `GET /chunks/recent`, `/graph` degree + kind/min_degree filters with
  top-degree sampling.
- **`/dashboard` route** (`apps/web`): KPI strip + Intake (ledger runs),
  Classification (layer/project bars, 30-day sparkline, source donut),
  embedded entity force-graph, live Recall (query + dossier card); 5s
  polling with visibility pause; graceful empty/outdated/unavailable states.
- **Graph schema**: person/event/place/org node kinds, brain edge rels, and
  node `degree` are first-class; the HUD understands entity graphs.
- **MCP harvest exports** (`second-brain/data/exports/`, gitignored):
  Mem.ai notes (122), Google Calendar year (.ics, 322 events + attendee
  edges), Granola meeting summaries (5) — generated via connected MCPs.
- **`scripts/bulk_ingest.sh`**: ordered wave-1 corpus runner (entities
  first), PII exclusions on every local corpus, per-run ledger rows.

### Fixed

- Checkpoint watermarks commit only after the pipeline's final flush
  succeeds with zero doc errors (was: silent permanent chunk loss on a
  failed tail flush; errored docs skipped forever).
- `BrainIndex` refuses an embedder whose dimension mismatches the existing
  index (was: silently garbage recall).
- Dry-run checkpoint rollback is scoped to the adapter under test (was:
  reverted/deleted concurrent adapters' sync tokens).
- Missing-source ingests write a failed ledger row; `[` is literal in
  exclude patterns; classification counters skip failed docs; dashboard
  never presents demo/mem data as the entity graph; transient breakdown
  failures aren't reported as "brain outdated".
- Pre-existing latent build failures in `apps/connectors/*`,
  `packages/normalize` (frontmatter list-tag parsing), and
  `even-hub/salience` (capitalized-greeting mentions).

### Changed

- `PROJECT_KEYWORDS` extended: synaptic-labs, synthsidian, jasmmm, verizon,
  anvl, synthbrain (additive; flagged for owner review).
- CLAUDE.md overlay: dashboard row superseded by the 2026-07-02 directive;
  canonical data paths under `second-brain/data/`.
