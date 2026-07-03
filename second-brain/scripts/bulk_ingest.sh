#!/bin/bash
# Bulk historical ingest — wave 1 (zero-credential local corpora).
# See docs/plans/2026-07-02-bulk-ingest-dashboard.md for the corpora plan.
#
# Entity sources first (canonicalization + dossier edges depend on a seeded
# graph), then chunk sources. Every run writes an ingest_runs ledger row that
# the dashboard's Intake panel reads. Embedder is ALWAYS `local` (A1) and data
# paths are ALWAYS the canonical ones (A2) — never let these default.
#
# Usage: bash scripts/bulk_ingest.sh [--dry-run]
set -u  # no -e: one failed corpus must not abort the rest; failures land in the ledger

SB="$(cd "$(dirname "$0")/.." && pwd)"
PY="$SB/.venv/bin/python"
DB="$SB/data/brain_index"
ENTDB="$SB/data/entities.db"
LOG_DIR="$SB/data/ingest-logs"
mkdir -p "$LOG_DIR"
STAMP="$(date +%Y%m%d-%H%M%S)"
LOG="$LOG_DIR/bulk-$STAMP.log"
DRY="${1:-}"

run() {
  echo "=== $(date '+%H:%M:%S') $*" | tee -a "$LOG"
  "$PY" -m brain.cli --db "$DB" --entdb "$ENTDB" --embedder local "$@" ${DRY:+--dry-run} >> "$LOG" 2>&1
  echo "    exit=$?" | tee -a "$LOG"
}

run_entities() {
  echo "=== $(date '+%H:%M:%S') $*" | tee -a "$LOG"
  "$PY" -m brain.cli --db "$DB" --entdb "$ENTDB" "$@" >> "$LOG" 2>&1
  echo "    exit=$?" | tee -a "$LOG"
}

cd "$SB"

# ---- 1. Entity graph seed (skipped on --dry-run: ingest-entities has no dry mode)
if [ -z "$DRY" ]; then
  run_entities ingest-entities --kind contacts --source "$SB/sample_contacts.vcf"
  run_entities ingest-entities --kind calendar --source "$SB/sample_calendar.ics"
  run_entities ingest-entities --kind calendar --source "$SB/data/exports/calendar/wes-synthminds.ics"
fi

# ---- 2. Chunk corpora (order: curated -> vaults -> transcripts -> loose docs)
run ingest --adapter mem --source "$SB/data/exports/mem"
run ingest --adapter granola --source "$SB/data/exports/granola"

# Repo vault: the numbered wings + Mission Control + Workshop. Exclude the code
# trees and second-brain/data (would re-ingest the mem/granola exports under
# source=filesystem). SKIP_DIRS already drops .git/node_modules/.venv/dot-dirs.
run ingest --adapter filesystem --source "/Users/wes_shields/Downloads/SynthBrain" \
  --exclude "second-brain/*" --exclude "apps/*" --exclude "packages/*" \
  --exclude "even-hub/*" --exclude "docs/plans/*"

run ingest --adapter filesystem --source "/Users/wes_shields/Library/CloudStorage/GoogleDrive-wes@synthminds.ai/My Drive/Obsidian/2ndBrain"

run ingest --adapter claude-code --source "/Users/wes_shields/.claude/projects"

# A5 PII policy: financial-account material stays out of EVERY local corpus,
# not just Downloads. Substring matches are case-insensitive on the relative
# path ('[' is literal; only * and ? glob).
PII_EXCLUDES=(--exclude "taxes" --exclude "1099" --exclude "w-9" --exclude "w-2 "
  --exclude "bank" --exclude "statement" --exclude "payroll"
  --exclude "paystub" --exclude "invoice")

run ingest --adapter filesystem --source "/Users/wes_shields/Documents" "${PII_EXCLUDES[@]}"
run ingest --adapter filesystem --source "/Users/wes_shields/Desktop" "${PII_EXCLUDES[@]}"

# Loose Downloads docs: also exclude the SynthBrain clone (ingested above).
run ingest --adapter filesystem --source "/Users/wes_shields/Downloads" \
  --exclude "SynthBrain/*" "${PII_EXCLUDES[@]}"

echo "=== DONE $(date '+%H:%M:%S') — stats:" | tee -a "$LOG"
"$PY" -m brain.cli --db "$DB" --entdb "$ENTDB" stats | tee -a "$LOG"
