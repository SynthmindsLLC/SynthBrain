# even-hub — G2 glasses plugin (Phase 4 scaffold)

The G2 glasses' end-to-end loop:

```
mic 16kHz PCM
  -> STT (Deepgram Nova-3 cloud OR local Whisper-tiny)
  -> 15-second beat aggregator
  -> salience layer (entity-density + context-token filter)
  -> brain.dossier({ mention, event, context })   <-- our FastAPI surface
  -> HUD render (3-5 bullets, <=8 words each)
  -> R1 DOUBLE_CLICK_EVENT = dismiss
```

The plugin **only** does I/O and the recall round-trip. Resolution,
disambiguation, and synthesis live in the brain (`brain/core/`) so the same
logic runs from chat, web, and glasses.

## Status

**Scaffold only.** This phase is gated on:
1. CT all-party-consent + Navy OPSEC review (see `second-brain/CLAUDE.md`).
2. Even Hub SDK access (paid program; SDK installer not in this repo).
3. Hardware-on-device validation of the chosen STT path.

What's in here is the architecture in code: TypeScript types for the
contracts the plugin needs to satisfy, a deterministic mock that proves the
end-to-end loop against the running brain, and the HUD-budget enforcement
logic that mirrors `brain/core/dossier.py`.

## Run the deterministic loop against the brain

```bash
# in second-brain/:
python -m brain.cli serve --port 8088

# in another shell:
cd even-hub
pnpm install
pnpm tsx src/replay.ts samples/jeff-party.json
```

The replay tool reads a JSON transcript (speaker + line + ts), runs the
salience filter, calls the brain, and renders the bullets the HUD would
show. The same code path the real plugin will run once the Hub SDK
lands.

## Files

```
src/
  types.ts              # contracts: STTSegment, SalientCue, RenderedCard
  salience.ts           # pure-TS port of brain.core.salience signals
  beat.ts               # 15-second windowing
  brain-client.ts       # talks to /dossier, /resolve on the FastAPI surface
  hud.ts                # bullet truncation + render formatter
  replay.ts             # deterministic e2e tool (CLI)
samples/
  jeff-party.json       # canonical demo transcript
```
