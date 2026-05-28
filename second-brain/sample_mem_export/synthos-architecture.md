# SynthOS — Technical Architecture Blueprint

## Key Decisions
- Locked a generic pipeline core with swappable per-vendor adapters.
- Principle: behavior in code, identity in data.

## Workarounds
The wholesale ingest path (#17091) currently writes to Square directly and
bypasses the audit log — a known workaround we adopted to ship fast, flagged in
the risk register to fix before scale.
