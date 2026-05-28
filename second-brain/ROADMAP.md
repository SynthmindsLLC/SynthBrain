# ROADMAP — Second Brain

## Phases

| Phase | Scope | Status |
|---|---|---|
| **0 — Spine** | LanceDB index + MemoryChunk + Mem adapter + CLI | ✅ done |
| **1 — Past + entities-in** | Contacts (.vcf) + Calendar (.ics) + entity graph | ✅ done. ⬜ remaining: Drive, hard-drive (Filesystem), M365 chunk adapters |
| **2 — Present + resolution** | Claude/ChatGPT export, Granola, FieldyAI adapters; LLM layer classifier; **`resolve()` + `dossier()`** | ⬜ next |
| **3 — Retrieval surface** | salience layer + synthesis + dossier query mode + latency budget | ⬜ |
| **4 — Glasses** | Even Hub plugin + STT + HUD render | ⬜ |

`docs/g2-r1-reference-architecture.md` is the detailed build doc for Phases 3–4.

---

## NEXT TASK: `resolve()` — context-aware entity resolution

The make-or-break component. Spec:

```
resolve(mention: str, context: str, kind: str) -> Resolution
```

- `mention` — the raw token heard/seen ("Jeff").
- `context` — surrounding conversation/text ("...the party last fall...").
- Returns the best entity **with a confidence**, or a NO-MATCH / AMBIGUOUS result.

Algorithm (cheap → expensive):
1. **Exact / alias hit** in `EntityStore.find_by_name`. One hit → done (high conf).
2. **Multiple hits** (the real case — two "Jeff"s) → disambiguate with `context`:
   - signal: shared events/places/orgs mentioned in context vs. each candidate's
     edges/attributes (graph proximity);
   - signal: embedding similarity between `context` and each candidate's profile;
   - combine → ranked candidates + confidence.
3. **No hit** → optional fuzzy name match; else return NO-MATCH. **Do NOT guess.**

Hard rules:
- Below a confidence threshold, return AMBIGUOUS and let the surface show "2 Jeffs?"
  rather than confidently popping the wrong person on the lens. A wrong dossier is
  worse than no dossier.
- Pure-Python + deterministic fallback must work with the `fake` embedder so tests
  run offline; the LLM/embedding path is an opt-in upgrade.

Tests to add: single-match, two-Jeffs-disambiguated-by-context, no-match,
below-threshold-returns-ambiguous.

## THEN: `dossier()`

```
dossier(person_mention, event_hint, context) -> Card
```
1. `resolve()` the person and the event.
2. Graph-join: chunks where `edge(person, mentioned_in)` ∧ `about(event)`.
3. LLM-synthesize → 3–5 bullets, ≤8 words each (HUD constraints in the G2 doc).
4. Return structured Card (name, role, relationship, where-met, what-discussed).

---

## Open questions

- **FieldyAI ingestion** — no connector; does Fieldy expose an API or transcript
  export? Verify before Phase 2. It's the "what we discussed" source.
- **Embedding model for production** — `nomic-embed-text-v1.5` vs `bge-small` (local)
  vs OpenAI. Decide before indexing the full corpus (re-embedding is expensive).
- **Entity resolution at scale** — `find_by_name` is a full scan; fine for a personal
  graph, revisit if entities exceed ~50k.
- **Where the brain runs for the glasses** — phone-side companion vs. always-on box
  the phone queries (the G2 doc assumes a phone companion). Affects how the index is
  served in Phase 4.

## Decisions log (from chat design sessions)

- Canonical brain = local index; Mem demoted to one source. (overrides G2 research)
- Adapters built against **universal export formats** (.vcf, .ics, Mem markdown) —
  provider-agnostic, offline-testable. Live-connector versions are a later upgrade.
- Two stores: LanceDB (vectors) + SQLite (entity graph). Dossier = graph join.
- Privacy/legal parked for prototype; **hard gate before recording others in
  production** (CT all-party consent + owner is active-duty Navy → command/OPSEC
  conversation first). Full risk analysis in Mem "Synapse Session — G2 …" note.
