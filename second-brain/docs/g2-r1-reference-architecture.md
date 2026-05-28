# Conversation Copilot for Even Realities G2 + R1: A Reference Architecture
## Synthminds Deep Research Report — May 2026

## TL;DR
- **A 15-second-cadence conversation copilot on the Even G2 + R1 ring is technically feasible today, with two important asterisks**: full MentraOS support for the G2 was only announced for January 2026 (per the Mentra blog post "Even Realities G2 Support Coming on MentraOS"), and ring events are mediated by the official Even Hub SDK (`@evenrealities/even_hub_sdk`), not yet by `@mentra/sdk`. Additionally, a true "long-press = stop" gesture is **not exposed to third-party apps** — `DOUBLE_CLICK_EVENT` on the R1 is the correct stop primitive.
- **The recommended stack is Deepgram Nova-3 (streaming STT, sub-300 ms) → on-phone salience filter → parallel retrieval over a local LanceDB mirror of Mem.ai (3–5 s fast-path) + OpenAlex/Semantic Scholar/Crossref enrichment (async) → Gemini 2.5 Flash-Lite or Claude Haiku 4.5 synthesis (≈600 ms TTFT) → 5-line bullet render to the G2 HUD via the Even Hub SDK**, refreshed on a fixed 15-second beat.
- **The hard constraints are legal and UX, not technical**: eleven US states (CA, CT, DE, FL, IL, MD, MA, MT, NH, PA, WA per the Reporters Committee for Freedom of the Press) require all-party consent to record in-person conversations, and the G2's monochrome green canvas tolerates only ~5 short lines of glanceable text. Build it as a *user-triggered*, *disclosed* tool with on-device transcription where possible.

## Key Findings
1. **Even Hub SDK is the only SDK that today distinguishes R1 ring input from G2 temple input** and exposes `CLICK_EVENT` (0), `DOUBLE_CLICK_EVENT` (3), `SCROLL_TOP_EVENT` (1), `SCROLL_BOTTOM_EVENT` (2) per `hub.evenrealities.com/docs/guides/input-events`. There is **no `LONG_PRESS_EVENT` for third-party plugins** — long-press is reserved by the OS shell for the main menu.
2. **MentraOS provides cross-glasses portability and a mature transcription pipeline** (`session.events.onTranscription`, `session.events.onButtonPress` with `pressType: 'short' | 'long'`), but as of May 2026 it does not document an R1-specific `buttonId`; ring presses surface as generic `MAIN` button events when they surface at all. Full G2 support was promised for January 2026 and has shipped pair/connect/display/microphone/touch gestures per the Mentra-Community/MentraOS release notes on GitHub.
3. **Deepgram Nova-3 is the right STT pick** for an always-on, English-first listening session. Per Deepgram's launch post "Introducing Nova-3" (deepgram.com/learn/introducing-nova-3-speech-to-text-api): "Nova-3 boasts a median WER of 6.84% on real-time audio streams... a 54.2% improvement over the next-best competitor (at 14.92%)." Sub-300 ms streaming latency is documented, with batch at $0.0043/min and streaming at $0.0077/min on Pay-as-you-go. The Daily.co "Benchmarking STT for Voice Agents" post (Feb 13, 2026) using pipecat-ai/stt-benchmark across 1,000 real-speech samples found Deepgram Nova-3 (247 ms median TTFS, 1.62% WER) and Soniox (249 ms, 1.29% WER) essentially tied on latency, with Soniox slightly more accurate; Speechmatics was slower (495 ms) but most accurate (1.07% WER).
4. **Mem.ai's v2 API supports `POST /v2/search-notes` and `GET /v2/notes`** (cursor-paginated, max 100/page, sortable by `created_at` or `updated_at`) per the `docs.mem.ai/api-reference/overview/changelog` 2025-11-17 release, plus a one-time Markdown export — sufficient to mirror your second brain into a local vector store and incrementally re-sync. The API does **not** expose embeddings or webhooks, so polling `updated_at` is the realistic sync pattern.
5. **LanceDB is the best vector store for this use case**: embedded (zero server), columnar Lance format, ~40–60 ms p50 query at moderate corpus sizes (per Vinayak's "LanceDB vs Qdrant for Conversational AI" Medium benchmark, May 2025), runs in-process with the phone-side companion service, and handles 1M+ chunks comfortably. Qdrant (~20–30 ms HNSW queries, ~95% Recall@1) is the right "graduation" target if the second brain grows beyond ~250k chunks or you need filterable HNSW.
6. **OpenAlex + Semantic Scholar + Crossref cover the academic enrichment layer.** Per Jason Priem's February 24, 2026 OpenAlex blog post and the OpenAlex changelog, **API keys are now required for all OpenAlex requests** (the unauthenticated polite pool was retired); free API keys receive 100,000 credits/day, with list queries costing 10 credits each (~10,000 list calls/day on the free tier). Semantic Scholar's REST API gives an introductory rate of 1 request/second per API key with higher tiers on review. Both are adequate when calls are gated by salience triggers (1–2 entity lookups per 15-second cycle, not per utterance).
7. **The 15-second cadence is comfortable, not tight**. Realistic budget: ~2 s rolling-window transcript → ~300 ms salience + query formation → ~60 ms LanceDB top-k → ~1.2 s academic/web enrichment (parallel) → ~800 ms LLM synthesis → ~400 ms BLE render = **≈3.8 s end-to-end for the Mem fast-path**, leaving ~9 s of slack to fold in late-arriving enrichment before the next refresh.
8. **Legally, the project lives in a yellow zone**. Per the Reporters Committee for Freedom of the Press, eleven US states require all-party consent for recording in-person conversations; on-device transcription with immediate audio discard materially reduces but does not eliminate exposure.

## Details

### 1. Real-time STT and the listening pipeline
The continuous-listen front end is the single most expensive component to get wrong, because any latency or accuracy regression there is multiplied through every downstream stage. The mainstream 2025–2026 benchmarks converge on a clear Pareto frontier: **Deepgram Nova-3** delivers a 6.84% median WER on real-time streams per Deepgram's launch post, with sub-300 ms streaming latency at $0.0077/min and diarization available as a per-minute add-on. Daily.co's open-source pipecat-ai/stt-benchmark (Feb 2026) measured Deepgram and Soniox as effectively tied on median TTFS (247 ms vs 249 ms), with Speechmatics slower (495 ms) but most accurate (1.07% WER); Soniox's own vendor benchmark (soniox.com/benchmarks) claims a 60-language study where Soniox reached 6.5% WER in English vs 9.3% for Deepgram.

For this app, **Deepgram Nova-3 over WebSocket from the phone-side companion server is the recommended default**. The G2 microphone array streams audio over BLE to the MentraOS app (or Even Hub plugin), which already exposes finalized transcript tokens through `session.events.onTranscription((data) => …)`. We pipe the same audio out to Deepgram and use Deepgram's transcript as the canonical input to the salience layer, treating the MentraOS transcript as a redundant fallback. Audio frames are buffered in 100 ms windows; interim transcripts arrive every ~200–300 ms; finalized utterances arrive on speaker pauses.

For users who require strict on-device processing (privacy, two-party-consent states, off-network), **`faster-whisper` running Whisper-large-v3-turbo on an M-series Mac or a CUDA box** is the right private-mode fallback, with the tradeoff of higher WER (~10–14%) and visibly worse handling of overlapping speech. WhisperLive provides a drop-in WebSocket facade.

**Diarization** is the third axis. Deepgram's diarization add-on tags speaker labels in the stream; for a 1:1 conversation we strongly prefer **device-side voice activity gating** — only segments where the *other* speaker is talking get pushed to the salience pipeline — because the user's own utterances are rarely the subject of useful augmentation. The G2's bone-conduction-adjacent mic placement and the in-ear delay of one's own voice make this gate inexpensive to implement.

### 2. Mem.ai second-brain RAG layer
The Mem.ai v2 REST API exposes `POST /v2/mem-it`, `POST /v2/notes` (create), `GET /v2/notes/{id}`, `DELETE /v2/notes/{id}`, `GET /v2/notes` (list, cursor-paginated, max 100/page, sortable by `created_at` or `updated_at`), `POST /v2/search-notes`, and matching collection endpoints (per the `docs.mem.ai/api-reference/overview/changelog` 2025-11-17 release notes). There are no webhooks and no embedding access. Mem also offers a one-time **Markdown export** of the entire workspace (emailed as a single .md archive) — this is how you seed the local mirror.

**Recommended sync pattern**:
1. **Initial seed**: trigger a Mem Markdown export from Settings, parse the resulting file into individual notes, store them on disk under a content-addressed path.
2. **Incremental sync**: every 15 minutes, call `GET /v2/notes?order_by=updated_at&limit=100` and walk the cursor until you hit notes older than the last-sync timestamp. Re-embed only the changed notes.
3. **Local index**: chunk each note with a **markdown-header-aware splitter** (target 300–500 tokens with 50-token overlap, splitting on `##`/`###` boundaries). The Weaviate "Chunking Strategies" guide and Firecrawl's 2026 chunking study both find header-aware splitting on markdown beats fixed-size by ~9% recall.
4. **Embedding**: OpenAI `text-embedding-3-small` (1536-d) for cloud-acceptable installs; `nomic-embed-text-v1.5` or `BAAI/bge-small-en-v1.5` running locally via Ollama or `sentence-transformers` for strict-private installs.
5. **Vector store**: **LanceDB** (embedded, on-disk Lance format), with `id`, `note_id`, `chunk_text`, `embedding`, `created_at`, `updated_at`, `collection_tags[]` as the schema. Benchmarks show 40–60 ms p50 retrieval with IVF_PQ at the corpus sizes a personal second-brain reaches (typically 5k–50k chunks).

**Sync limitation to flag**: Mem.ai's API does not currently expose a "since timestamp" server-side filter; you simulate it client-side by sorting `updated_at desc` and stopping at the watermark. Mem Pro's "Unlimited API keys" entitlement plus reasonable polling makes rate limits a non-issue for single-user use.

### 3. Web and academic enrichment retrieval
The enrichment layer runs asynchronously and is *opportunistically* slotted into the HUD when ready. The salience layer (see §5) emits a structured query plus 1–3 named entities; we fan that out to:

- **OpenAlex** (`api.openalex.org/works?search=…&api_key=…`) — 250M+ records. Per Jason Priem's Feb 24, 2026 announcement on the OpenAlex blog, API keys are now mandatory and free keys receive 100,000 credits/day with list queries costing 10 credits (~10,000 list calls/day). Typical response 300–600 ms. Best for breadth and citation counts.
- **Semantic Scholar Graph API** (`api.semanticscholar.org/graph/v1/paper/search`) — 1 RPS introductory rate per API key, returns abstracts and TLDRs (SPECTER2 embeddings available). Best for AI/CS topics and the built-in TLDR field, which is gold for HUD bullet rendering.
- **Crossref** (`api.crossref.org/works`) — DOI-grade metadata for credibility/peer-review confirmation, free, generous limits.
- **PubMed E-utilities** when biomedical entities are detected (a small NER classifier flags MeSH-adjacent terms and routes there).
- **Tavily** or **Exa** for credibility-filtered general web — both expose a `include_domains` allowlist and a `score` field; we use a curated allowlist of ~400 reputable outlets plus a domain-quality classifier as the front-line filter.

The credibility filter on the general-web layer is the riskiest piece. Recommendation: maintain a **two-tier allowlist** — a *primary* list (peer-reviewed journals, government statistical agencies, top-tier reference works, major news wires) whose results pass straight through, and a *secondary* list (industry publications, well-known blogs) whose results are summarized with explicit "[source]" attribution. Everything else is dropped.

### 4. Synthesis + HUD rendering
The synthesis LLM receives: (a) the last 30 seconds of transcript, (b) the top 3 Mem chunks, (c) any enrichment that arrived in time, and (d) a fixed system prompt that constrains output to **3–5 bullets, ≤8 words each, no preamble, no markdown other than `•`**. Recommended models by tier:

| Tier | Model | TTFT (p50) | Throughput | Cost (in/out per 1M) | Notes |
|------|-------|------------|------------|----------------------|-------|
| Best perceived speed | Claude Haiku 4.5 | ~597 ms (Ganglani 2026) | ~79 tok/s | ~$1 / ~$5 | Fastest first bullet on screen |
| Best total latency | Gemini 2.5 Flash-Lite | ~150–200 ms TTFT | ~214 tok/s (Artificial Analysis, May 2026) | $0.10 / $0.40 | Fastest end-to-end completion |
| Budget default | GPT-4o-mini | ~560 ms (Vellum) | ~97 tok/s | $0.15 / $0.60 | Reliable, mature tooling |
| On-device | Llama 3.1 8B Instruct (Q4) | ~400 ms | ~40 tok/s on M3 Pro | $0 | Privacy mode |

For a 15-second beat where the *user-perceived* moment is the bullet appearing on the lens, **Gemini 2.5 Flash-Lite** wins because total wall-clock to finished bullets is what triggers the render call. Claude Haiku 4.5 is preferable only if you stream tokens directly to the HUD, which the G2 doesn't natively support.

**HUD rendering** on the G2's monochrome green waveguide presents conflicting public specs (Notebookcheck cites 640×200 in one launch piece and 640×350 in another; some community docs reference a 576×288 per-eye canvas at 16 grey shades). Treat the safe design budget as **roughly 5 visible lines of 6–8pt text, ~30–40 characters per line** and verify on your specific frame variant (G2A vs G2B). Best practices, drawn from Google Glimmer's design guidance (per UploadVR's coverage) and ACM CHI work on glanceable AR interfaces (Lu et al., "Exploration of Techniques for Rapid Activation of Glanceable Information"):
- Light glyphs on the (transparent) dark background; maintain intensity, not saturation.
- Maximum 3 bullets visible at once. Truncate aggressively.
- No animations; no scrolling text. The eye should resolve the entire frame in <1 second.
- A persistent 1–2 character "session glyph" in the corner indicates the copilot is live.
- Refresh on a fixed 15 s beat (configurable 10–30 s); never mid-bullet.

### 5. R1 ring control
Per the Even Hub SDK input-events documentation (`hub.evenrealities.com/docs/guides/input-events`), R1 events arrive through `bridge.onEvenHubEvent` with `event.textEvent.eventType` taking values from `OsEventTypeList`: `CLICK_EVENT` (0), `SCROLL_TOP_EVENT` (1), `SCROLL_BOTTOM_EVENT` (2), `DOUBLE_CLICK_EVENT` (3), plus lifecycle events (`FOREGROUND_ENTER_EVENT`, `FOREGROUND_EXIT_EVENT`, `ABNORMAL_EXIT_EVENT`). **There is no `LONG_PRESS_EVENT` exposed** — long-press is reserved by the OS shell to open the main menu. The R1 ring and G2 temple touchpad fire the *same* event types, but the SDK lets you distinguish the input source so you can scope handlers to ring-only.

**Recommended gesture mapping**:
- **`DOUBLE_CLICK_EVENT` on R1** → STOP the copilot session (the canonical "decisive" non-scroll gesture).
- **`CLICK_EVENT` on R1** → pause/resume (toggle).
- **`SCROLL_TOP_EVENT` / `SCROLL_BOTTOM_EVENT`** → cycle between the current insight, the previous insight, and a "show source" mode.

If you build on MentraOS for cross-glasses portability, the equivalent is `session.events.onButtonPress((data) => …)` filtering on `data.pressType === 'long'` against `buttonId === 'main'` per the `cloud-docs.mentra.glass/cloud-overview/sdk-integration` examples — but as of May 2026 the MentraOS SDK does not document an R1-specific `buttonId`, so ring presses are not yet distinguishable from temple presses through the Mentra path. **For an R1-aware build today, use Even Hub SDK; for a future cross-glasses build, plan to migrate to Mentra once it surfaces R1.**

A raw-BLE fallback exists via the i-soxi/even-g2-protocol reverse engineering (base service UUID `00002760-08c2-11e1-9073-0e8ac72e0000`, write on `…5401`, notify on `…5402`, display on `…6402`, CRC-16/CCITT over payload with a 7-packet authentication handshake), but R1 ring opcodes are not yet publicly decoded and you would compete with the official Even app for the dual-BLE connection. Not recommended for production.

### 6. Latency budget
The 15-second beat decomposes as follows (median values, conservative):

| Stage | Latency | Notes |
|-------|---------|-------|
| Rolling transcript window close | 2,000 ms | Wait for natural pause / fixed window |
| Deepgram finalization | 250 ms | Sub-300 ms target, hit in ~90% of cases per Daily.co benchmark |
| Salience classifier (small LLM or rules) | 300 ms | GPT-4o-mini classify + extract entities |
| LanceDB top-k (k=5) | 60 ms | Local, embedded |
| **Mem fast-path total** | **~2.6 s** | Available to synthesis |
| OpenAlex query (p50) | 500 ms | Parallel to LanceDB |
| Semantic Scholar TLDR fetch | 600 ms | Parallel |
| Web enrichment (Tavily) | 1,200 ms | Parallel; often arrives after Mem |
| Synthesis (Flash-Lite, 80 output tokens) | 550 ms | TTFT 150 ms + 80 tok @ 214 tok/s |
| BLE render to G2 via Even Hub | 400 ms | Empirically observed for short text payloads |
| **End-to-end Mem fast-path** | **~3.8 s** | Inside the 3–5 s target |
| **End-to-end with enrichment** | **~5.5 s** | Inside the 15-s beat with ~9 s slack |

The slack absorbs (a) tail-latency outliers on any single API, (b) speculative pre-fetch of the *next* cycle's enrichment based on detected topic drift, and (c) human reading time — usability studies on glanceable HUDs consistently find that ~4–8 seconds is the *minimum* dwell needed for a bullet to be read, comprehended, and dismissed without cognitive overload.

### 7. Phased build roadmap
**Phase 0 — Spike (2 weeks):** Even Hub plugin skeleton + Deepgram WebSocket + hard-coded 5-bullet renderer. Goal: see *any* live insight on the lens. Mem mirror is a flat-file keyword search.

**Phase 1 — MVP (6 weeks):** Add LanceDB + nomic-embed-text-v1.5; one-time Mem Markdown export → embed → index. Wire `DOUBLE_CLICK_EVENT` STOP, `CLICK_EVENT` pause/resume, scroll-to-cycle-history. Hard-code Flash-Lite synthesis prompt. Single source per insight. Disclosure banner on session start.

**Phase 2 — Enrichment (4 weeks):** Add OpenAlex + Semantic Scholar + Crossref fan-out, with the salience layer (small LLM classifier informed by Beyond-RAG-style question identification from Agrawal et al., arXiv:2410.10136) deciding which APIs to call. Add Tavily for general web. Implement the credibility allowlist.

**Phase 3 — Sync + scale (4 weeks):** Incremental `GET /v2/notes` polling against Mem.ai. Add Qdrant migration path for users with >250k chunks. Add on-device Whisper option via faster-whisper. Add the speculative pre-fetch loop.

**Phase 4 — Cross-glasses (when MentraOS exposes R1):** Port the Even Hub plugin to a `@mentra/sdk` mini-app, reusing the phone-side synthesis pipeline as a hosted backend the mini-app calls. Adds Mentra Live, G1, Vuzix, Mach 1 compatibility.

## Recommendations
1. **Build on Even Hub SDK first, not MentraOS** — Even Hub is the only path that exposes R1-vs-G2 source distinction today and ships with `evenhub-cli` and a simulator. Migrate to a Mentra mini-app in Phase 4 once R1 events are documented in `@mentra/sdk`.
2. **Use `DOUBLE_CLICK_EVENT` on the R1 as the STOP primitive.** Do not design around a long-press; it is not surfaced to third-party plugins.
3. **Pair Deepgram Nova-3 streaming with on-device VAD gating** so only the *other* speaker's audio is pushed to STT — halves your API spend and improves perceived relevance.
4. **Mirror Mem.ai locally via Markdown export + 15-minute incremental `GET /v2/notes` polling.** Do not hit `/v2/search-notes` per cycle — it adds 500–1500 ms of unnecessary latency and burns rate limit.
5. **Embed with `nomic-embed-text-v1.5` (local) and store in LanceDB.** Reserve OpenAI embeddings for users who explicitly opt into cloud processing.
6. **Synthesize with Gemini 2.5 Flash-Lite by default**, Haiku 4.5 if streaming-to-HUD lands in the SDK, GPT-4o-mini as the procurement-safe fallback.
7. **Render exactly 3–5 bullets of ≤8 words each, monochrome, no animation, refresh on a strict 15-second beat.** Resist the urge to mid-cycle interrupt.
8. **Implement disclosure-first UX**: on every session start, the HUD shows a "Copilot listening" banner for 5 seconds and the user must `CLICK_EVENT` confirm. This is your legal shield in two-party-consent states.

### Decision thresholds that should change these recommendations
- If users will use the app in CA/IL/FL/MA/PA/WA/MD/MT/NH/DE/CT regularly, **switch to on-device `faster-whisper` by default** and require a per-session explicit "I have all-party consent" confirmation.
- If second-brain size exceeds 250k chunks, **migrate from LanceDB to Qdrant** with filterable HNSW; the 20–30 ms vs 60 ms query difference compounds at scale.
- If MentraOS ships R1-specific button IDs in `@mentra/sdk` before Phase 4, **skip the Even Hub-first detour** and build cross-glasses from day one.
- If Deepgram WER on your domain (measured on 100+ minutes of representative audio) exceeds 12%, **switch to Soniox** for the multilingual model (Soniox/Daily.co benchmarks place it within 2 ms of Deepgram on latency with lower WER).
- If the OpenAlex 10,000-list-calls/day free tier becomes binding, **upgrade to the OpenAlex premium plan or shift academic lookups to Semantic Scholar's bulk endpoint**.

## Caveats and not-currently-feasible items
- **MentraOS full G2 support shipped in stages around January 2026** per the Mentra blog post "Even Realities G2 Support Coming on MentraOS"; the SDK does not yet document R1-specific button IDs as of this report.
- **No `LONG_PRESS_EVENT` for third-party plugins** on either the R1 or G2 temple — this is a deliberate OS reservation and unlikely to change.
- **Mem.ai exposes no embeddings, no webhooks, no server-side "since timestamp" filter.** All sync is polling-based.
- **The G2 display canvas dimensions are reported inconsistently across sources** (640×200 in one Notebookcheck launch piece, 640×350 in another, 576×288 per-eye in some community docs). Treat 5 visible lines × ~30 characters as the safe design budget and verify against your specific frame variant.
- **OpenAlex retired its unauthenticated polite pool in February 2026** per Jason Priem's blog post and the OpenAlex changelog; all callers now need a free API key, and the free tier caps at 100,000 credits/day (~10,000 list calls).
- **Continuous in-person recording is legally restricted in 11 US states.** A "conversation copilot" that records audio without all-party consent in CA/IL/FL/MA/PA/WA/MD/MT/NH/DE/CT may expose the user to criminal liability under state wiretap statutes. On-device transcription with immediate audio discard reduces but does not eliminate this risk; consult counsel before shipping consumer SKUs. Note that some states' statutes (e.g., New Mexico per *State v. Hogervorst*) have been read to apply only to telephone/electronic communications and not face-to-face conversations — the legal landscape is genuinely jurisdiction-specific.
- **The salience layer is the unsolved research problem.** Beyond-RAG (Agrawal et al., arXiv:2410.10136) shows that question-identification gating reduces unnecessary retrieval and can return answers within 2 s in contact-center deployments, but no published system targets the specific "augment a free-flowing dialogue without distracting either party" use case at the cadence proposed here. Expect Phase 2 to be the longest phase and to require iterative tuning on real conversations.
- **The G2's monochrome green waveguide and ~20° FOV mean that anything beyond short bullets becomes a literal eye-strain hazard.** Resist feature requests for charts, images, or scrolling body text.
- **Battery on the G2 is rated up to 2 days "typical use"** per Even Realities' product page — a continuous-listen session will materially shorten that. Empirically expect 4–6 hours of continuous copilot use per charge; plan UX around session timeboxes.
- **Throughput numbers for hosted LLMs are moving targets.** The 214 tok/s figure cited for Gemini 2.5 Flash-Lite is from Artificial Analysis's May 2026 measurement of the stable Google AI Studio endpoint; the September 2025 preview reached 296 tok/s on the same harness. Re-benchmark before locking the design.