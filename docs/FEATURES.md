# SynthBrain — Feature Spec

> Living roadmap. Sources: `Synthminds/Neural-Graph` (existing prototype to port from) and `nomic-ai` (Atlas / deepscatter / embedding models — patterns and OSS models to integrate).

## What Ships Today (Phase A.3 — PR #4)

Already in `apps/web` and rendering:

- Next.js 15 App Router PWA on `apps/web`, dark theme (`#0a0a14`), Apple-touch-icon manifest, service worker (caches static, never `/api/*`).
- 3D force-directed graph via `react-force-graph-3d` + `three-spritetext`. Dynamic-imported with `ssr:false`.
- Node coloring by `#source/*` tag (`fieldy=cyan`, `calendar=magenta`, `granola=yellow`, `drive=green`, `gmail=orange`, `mem=cyan`).
- Distance-faded sprite labels (mitigates >1000-node label soup).
- Tap-to-focus camera (`onNodeClick` → smooth `cameraPosition` transition with `lookAt`).
- iOS Pilot Mode: `DeviceOrientationEvent.requestPermission()` user-gesture-gated, quaternion → camera rig via `lib/use-pilot-camera.ts`.
- HUD: filter by source tag + collection.
- Mem.ai HTTP client (`lib/mem-http.ts`) against `api.mem.ai/v0` with `ApiAccessToken` auth. Falls back to bundled `data/seed.json` when `MEM_API_KEY` missing so first deploy renders without config.
- Shared `@synthbrain/graph-schema` Zod contract for `Note`, `Collection`, `GraphNode`, `GraphLink`, `Graph`.

---

## Source Inventory

### Neural-Graph (`Synthminds/Neural-Graph`)

Stack: Flask 3.1 + SQLAlchemy + PostgreSQL backend, Three.js + `3d-force-graph` frontend, Anthropic Claude (Opus 4.6) + OpenAI (GPT-4o-mini + Whisper). Socket.IO for real-time. Multi-source ingestion (PDF/DOCX, email, SMS, iOS Shortcuts, CSV, audio). Currently deployed at `neural-graph.vercel.app` but returns 404 (project paused).

**Synthminds-owned**, no upstream GPL/AGPL contamination. Port code patterns by hand to TypeScript; keep no Flask/Python in the SynthBrain runtime.

### Nomic AI

- **`nomic-ai/nomic-embed-text-v1.5`** (Apache 2.0, 16M+ HF downloads): 768-dim sentence embeddings, runs in browser via `transformers.js` or server via Nomic API. **Use for semantic clustering and similarity links.**
- **`nomic-ai/nomic-embed-text-v2-moe`** (Apache 2.0, multilingual MoE, 100+ langs).
- **`nomic-ai/deepscatter`** (TypeScript + WebGL + REGL, Apache Arrow feather quadtree tiling, >1B-point scale). **License NC-CC-BY-SA — cannot vendor for commercial use. Patterns only.**
- **Atlas** (atlas.nomic.ai, hosted): UMAP semantic maps, topic auto-labels per cluster, lasso multi-select, vector search, color-by-attribute, smooth animated layout transitions.

---

## Roadmap

Priority tags: **[NOW]** PR #5 immediately after Vercel goes green · **[NEXT]** PR #6–7 · **[LATER]** PR #8+ · **[SKIP]** explicit non-goals.

### Graph rendering

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 1.1 | Node size by centrality | NOW | Neural-Graph `network_analysis.py` | S | Compute degree centrality server-side in `/api/graph`; `r = base + log(centrality)`. Helps Wes spot hubs immediately. |
| 1.2 | Edge type → stroke style | NOW | Neural-Graph `models.py` `Edge.type` | S | 17 relationship types; map to `linkColor` + `linkWidth`. `in_collection` solid teal, `has_tag` thin gray, `mention` dashed amber. |
| 1.3 | Node glow / bloom post-processing | NEXT | Neural-Graph aesthetic (referenced in styles) | M | Three.js `UnrealBloomPass`. Bumps "wow" factor on iPhone. |
| 1.4 | Particles between linked nodes | LATER | None | M | Subtle traveling-dot effect. Pure visual polish. |
| 1.5 | Color-by-attribute toggle | NEXT | Nomic Atlas | S | Cycle: source / collection / tag / cluster / recency. Already have `lib/source-colors.ts` skeleton. |

### Camera & navigation

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 2.1 | Reset to home button | NOW | Neural-Graph | XS | Store initial camera; one button in HUD restores it. |
| 2.2 | First-person mode | LATER | None / new | L | "Walk through" the graph at node scale. Separate camera rig from pilot mode. |
| 2.3 | Cinematic auto-tour | LATER | None | M | Auto-orbit + auto-focus through top-centrality nodes. Idle screensaver mode. |
| 2.4 | Path animation between two nodes | NEXT | Neural-Graph traversal | M | Pick A + B → camera flies A → intermediate nodes → B. Pairs with graph agent. |

### Interaction

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 3.1 | Node hover tooltip | NOW | Neural-Graph | S | Raycaster + DOM overlay. Show title + first line of content. |
| 3.2 | Node detail bottom sheet (mobile) / right panel (desktop) | NOW | Neural-Graph right panel | M | Full metadata, tags, "Open in Mem.ai" deep link. Bottom sheet on touch screens. |
| 3.3 | Node drag to reposition | NEXT | Neural-Graph | S | Set `node.fx/fy/fz`; persist if user saves. |
| 3.4 | Lasso multi-select | NEXT | Nomic Atlas | M | 2D screen-space lasso → 3D selection. Used for bulk tag, bulk move-to-collection, bulk delete. |
| 3.5 | Search-to-focus | NOW | Neural-Graph + Nomic | S | Already partially in HUD; wire to camera focus on result click. |
| 3.6 | Vector search box | NEXT | Nomic Atlas | M | Embed query with `nomic-embed-text-v1.5`; cosine-match against pre-embedded note vectors; focus camera on top result. |

### AI features

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 4.1 | Auto-tagging on ingest | NOW | Neural-Graph `ai_tagger.py` (port) | M | Claude analyses note → 3–7 tags + category + entities. Background job from connector ingest. Reuse Neural-Graph's 12-category ontology + colors. |
| 4.2 | Relationship classification | NEXT | Neural-Graph `classify_edge_relationship` | M | Claude scores pairs of related notes against 17 relationship types (`related_to`, `implements`, `contradicts`, etc.) with confidence. |
| 4.3 | Suggested edges (3 per node) | NEXT | Neural-Graph `suggest_edges` | M | On node hover/click, surface 3 AI-recommended new connections. Reduces graph manual-editing friction. |
| 4.4 | **Graph Agent** (Claude tool-use) | NEXT | Neural-Graph `agent.py` | L | Natural-language queries answered via tool-using Claude loop. Tools: `search_notes`, `traverse_edges`, `get_centrality`, `get_communities`. Stream responses via SSE. **High-value: makes the graph queryable in English.** |
| 4.5 | Semantic clustering (UMAP) | NEXT | Nomic Atlas + `nomic-embed-text-v1.5` | L | Embed every note → UMAP to 3D → cluster with HDBSCAN. Render as a *Semantic Map* mode (toggle in HUD). Auto-label each cluster via Claude one-line summary. |
| 4.6 | Topic auto-labels above clusters | NEXT | Nomic Atlas | M | Sprite text floating above cluster centroid: "Customer feedback (n=23)". Visible from any zoom level. |
| 4.7 | Smooth animated layout transition | NEXT | Nomic Atlas / deepscatter | M | Force-directed ↔ semantic-map ↔ hierarchical: animate positions over 1.5s rather than snap. Uses `react-spring` or vanilla `requestAnimationFrame`. |
| 4.8 | Daily "What's new + what shifted" digest | LATER | None | M | Claude summarises notes added since last visit + clusters that grew. Notification on PWA open. |

### Data layer

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 5.1 | Real `@synthbrain/mem-client` package | NOW | New + Neural-Graph DB patterns | M | Extract HTTP logic from `apps/web/lib/mem-http.ts` into the shared package. Reusable by web + connectors. |
| 5.2 | Fieldy connector | NEXT | New | M | Phase A.2 of the original plan. Pulls Fieldy transcripts via REST or official MCP; writes to Mem `Sources/Fieldy`. |
| 5.3 | Calendar / Granola / Drive / Gmail connectors | LATER | New | M each | Phase B of original plan. Each writes to its own `Sources/*` collection. |
| 5.4 | CSV bulk import | NEXT | Neural-Graph `documents.py` | S | Drop a CSV in the web app → preview → commit to Mem. Useful for migrating existing spreadsheets. |
| 5.5 | PDF/DOCX ingestion | NEXT | Neural-Graph `documents.py` | M | Web-based: `pdf-parse` + `mammoth` (no PyMuPDF). Chunk by heading. Each chunk → Mem note linked to source. |
| 5.6 | API keys for programmatic ingest | LATER | Neural-Graph `APIKey` model | M | Bearer tokens scoped to write. Enables browser extension, Slack bot, mobile share-sheet. |
| 5.7 | Real-time updates via SSE | NEXT | Neural-Graph Socket.IO | M | Replace Socket.IO with SSE / Vercel Edge Functions. Push graph diffs to all connected clients when notes change. |
| 5.8 | Ingest log + audit trail | LATER | Neural-Graph `IngestLog` | S | Append-only Mem collection `Sources/_AuditLog`. Source, user, timestamp, status. |

### HUD / UI overlays

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 6.1 | Filter panel: tags / collections / date range | NOW | Neural-Graph | S | Already partial; finalize with chip-style multi-select. |
| 6.2 | Stats panel | NEXT | Neural-Graph `all-metrics` | S | Node count, edge count, density, top tags. Fold under HUD. |
| 6.3 | Community legend | NEXT | Neural-Graph `communities` | S | After Louvain runs, show coloured swatches + cluster size. |
| 6.4 | Settings: AI instructions per graph | NEXT | Neural-Graph `ai-prompt` | S | Wes can customise Claude's tagging prompt without redeploy. |
| 6.5 | Board view (alternative card grid) | LATER | Neural-Graph board view | M | Non-3D mode for one-handed phone use or low-power devices. |

### Layout algorithms

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 7.1 | Force-directed (current) | NOW | `react-force-graph-3d` native | — | Already shipping. |
| 7.2 | Hierarchical (tree) | NEXT | Neural-Graph | M | When notes have parent/child relationships (e.g. ADR threads), show as a tree. |
| 7.3 | Semantic map (UMAP) | NEXT | Nomic Atlas | L | Embed notes → UMAP to 3D coords. Pair with cluster auto-labels (4.6). |
| 7.4 | Radial / circular / spectral | LATER | Neural-Graph `network_analysis.py` | S each | Nice toggles for specific views. Skip until force + hierarchical + semantic are solid. |

### Network analysis

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 8.1 | Louvain community detection | NEXT | Neural-Graph `network_analysis.py` | M | Compute server-side, cache by filter hash. Drives community legend (6.3) and color-by-cluster (1.5). |
| 8.2 | Centrality (degree, betweenness) | NEXT | Neural-Graph | M | Sizes nodes (1.1) and highlights "hub" notes in stats panel. |
| 8.3 | Pathfinding A→B | LATER | Neural-Graph (Dijkstra, A*, BFS) | M | Pairs with path animation (2.4). |
| 8.4 | "Notes most likely to surprise" | LATER | Novel | M | Outlier detection in embedding space + low centrality. Surfaces forgotten gems. |

### Performance

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 9.1 | LRU cache `/api/graph` by filter hash | NOW | New | S | Already partial; verify 60s TTL doesn't stale. |
| 9.2 | Server-side cluster compute | NEXT | New | S | Phase C of original plan. Never recompute on phone main thread. |
| 9.3 | Frustum-aware label fade | NEXT | Three.js | S | Already partial via distance fade; add screen-space density check. |
| 9.4 | Lazy load for >5000 nodes | LATER | Neural-Graph idea | L | Fetch only nodes in camera neighborhood; stream more on zoom-out. Mirrors deepscatter's quadtree tiling concept (the OSS lib itself is NC-licensed). |
| 9.5 | Cluster collapse (folder semantics) | LATER | Novel | M | Tap a cluster centroid to collapse it into a single super-node; tap again to expand. |

### Mobile / PWA

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 10.1 | Pilot mode (DeviceOrientation) | NOW | — | — | Already shipping. |
| 10.2 | Haptic feedback on focus | NEXT | Web Vibration API | XS | 10ms tap on node-focus. iOS PWA only fires inside user gesture. |
| 10.3 | Pinch-to-zoom on the graph | NEXT | Native via `three-orbit-controls` | S | Already partial via mouse wheel; tune touch pinch sensitivity. |
| 10.4 | "Add to home screen" prompt | NEXT | beforeinstallprompt | XS | Show banner on second visit. iOS doesn't fire the event, so a static "Tap Share → Add to Home Screen" hint stays. |
| 10.5 | Joystick fallback for no-gyro devices | LATER | `nipplejs` | M | Phase D of original plan. Accessibility safety net. |
| 10.6 | Voice query (Web Speech API) | LATER | New + Graph Agent (4.4) | M | "Show me notes about Verizon from last week" → agent runs → camera flies to results. |

### Visual polish

| # | Feature | Priority | Source | Effort | Notes |
|---|---|---|---|---|---|
| 11.1 | Glassmorphism on HUD panels | NOW | Neural-Graph | XS | `backdrop-filter: blur(8px)`; already on the Pilot Mode button. Apply to filter panel + bottom sheet. |
| 11.2 | Gradient accent | NEXT | Neural-Graph (purple→blue) | XS | Apply to primary button + selection ring. Single-source brand colour. |
| 11.3 | Animated transitions on state changes | NEXT | Neural-Graph + Nomic | S | 300ms easing on filter changes, panel opens, color-mode swaps. |
| 11.4 | Background starfield / particles | LATER | None | M | Subtle. Don't overdo. |

---

## Explicit Non-Goals

- **No Flask/Python in the SynthBrain runtime.** Port algorithms to TypeScript; if a model needs Python (e.g. heavy embedding inference), call it as an HTTP service.
- **No `deepscatter` vendoring** (NC-CC-BY-SA license). Patterns only — implement WebGL tiling ourselves if/when we hit >100k notes.
- **No Twilio SMS / email / iOS Shortcuts ingestion** until the core connector set (Fieldy, Calendar, Granola, Drive, Gmail) is solid. Synthminds-specific surface area for later.
- **No Whisper transcription in-app.** Mem.ai / Fieldy already handle audio. We consume their transcripts.
- **No multi-user / admin dashboard.** Single-user (Wes) for now. Auth becomes a question only if SynthBrain ever serves others.
- **No Spectral / radial / circular layouts** until force-directed + hierarchical + semantic-map are all solid.
- **No Socket.IO.** Use SSE or Vercel Edge Functions.

---

## License Notes

- All ported code is rewritten from `Synthminds/Neural-Graph` (Synthminds-owned, Wes-controlled). No upstream GPL/AGPL contamination.
- Nomic embedding models (`nomic-embed-text-v1.5`, `v2-moe`) are **Apache 2.0** — safe to use commercially.
- `deepscatter` is **NC-CC-BY-SA** — *do not* vendor. Patterns and ideas only.
- `react-force-graph-3d`, `three`, `three-spritetext`, `nipplejs` — all MIT.

---

## Suggested PR Order

Each PR is independently deployable; live site stays usable throughout.

| PR | Title | Features | Why this order |
|---|---|---|---|
| PR #4 | Phase A.3 PWA (this PR) | 1.1*, 1.5*, 2.1*, 3.5*, 6.1*, 10.1, 11.1 (*partial) | Lands the visible product. |
| PR #5 | Real `mem-client` + Fieldy connector + bottom sheet + hover tooltips | 5.1, 5.2, 3.1, 3.2, 2.1 | First write path; user experience now feels complete. |
| PR #6 | AI tagging + relationship classification + suggested edges | 4.1, 4.2, 4.3, 6.4 | Makes the graph self-organize as new notes arrive. |
| PR #7 | Graph Agent (Claude tool-use, SSE) | 4.4, 10.6 | Natural-language queries. The "wow" feature. |
| PR #8 | Semantic map mode + topic labels + smooth transitions | 4.5, 4.6, 4.7, 7.3 | Nomic Atlas-style view. Requires embeddings infrastructure. |
| PR #9 | Network analysis (centrality, communities) + animated paths | 1.1, 8.1, 8.2, 2.4, 6.2, 6.3 | Power-user analytics. |
| PR #10 | CSV / PDF / DOCX import + real-time SSE + audit log | 5.4, 5.5, 5.7, 5.8 | Onboard existing content. |
| PR #11 | Lasso multi-select + cluster collapse + bulk actions | 3.4, 9.5 | Scale-out interactions for >500 nodes. |
| PR #12 | Polish: bloom, gradient, particles, board view | 1.3, 1.4, 6.5, 11.2, 11.3 | Last 20% visual layer. |

Defer everything in the **LATER** column until the **NOW + NEXT** columns are shipping and used.
