# @synthbrain/web

Next.js PWA that renders Mem.ai notes as a navigable 3D graph with iOS pilot mode (tilt-to-fly).

## Local dev

```bash
pnpm install
pnpm --filter @synthbrain/web dev
# DeviceOrientation requires HTTPS — for iPhone testing, use:
pnpm --filter @synthbrain/web dev:https
```

## Environment

Copy `../../.env.example` to `.env.local` and set:

- `MEM_API_KEY` — required for live note fetching. Get from Mem.ai → Settings → API. Without it, the app renders bundled `data/seed.json` demo data.
- `MEM_API_BASE` — optional override. Defaults to `https://api.mem.ai/v0`.

## Deploy

Vercel auto-detects this Next.js app via the root `vercel.json`. Set `MEM_API_KEY` in Vercel project env vars before the first deploy.

## Data flow

```
[Mem.ai HTTP API]                ┐
   ↓ (lib/mem-http.ts)            │
[lib/mem-source.ts] ── falls back ─→ [data/seed.json]
   ↓ (lib/build-graph.ts)
[/api/graph route] ── server-side fetch
   ↓
[components/GraphView] ── client orchestrator
   ├─ GraphCanvas (react-force-graph-3d + three-spritetext)
   ├─ HUD (filter by source/collection)
   └─ PilotMode (DeviceOrientation, iOS permission-gated)
```
