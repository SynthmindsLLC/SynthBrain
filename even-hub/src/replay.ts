#!/usr/bin/env tsx
// Deterministic e2e: feed a transcript JSON through beat -> salience -> brain -> HUD.
// Run with `pnpm replay samples/jeff-party.json` against a live brain.

import { readFileSync } from 'node:fs';

import { makeBeatStream } from './beat.js';
import { fetchDossier, fetchKnownNames } from './brain-client.js';
import { renderCard } from './hud.js';
import { extractCues } from './salience.js';
import type { STTSegment } from './types.js';

const SALIENCE_THRESHOLD = 0.5;

interface SampleFile {
  segments: STTSegment[];
}

async function main() {
  const path = process.argv[2];
  if (!path) {
    console.error('usage: tsx src/replay.ts <transcript.json>');
    process.exit(2);
  }
  const file = JSON.parse(readFileSync(path, 'utf-8')) as SampleFile;
  const known = await fetchKnownNames().catch(() => new Set<string>());

  const beat = makeBeatStream(15);
  for (const seg of file.segments) {
    const closed = beat.push(seg);
    if (closed) await handleBeat(closed.segments, known);
  }
  const tail = beat.flush();
  if (tail) await handleBeat(tail.segments, known);
}

async function handleBeat(segments: STTSegment[], known: Set<string>) {
  const cues = extractCues({ segments, knownNames: known });
  const top = cues[0];
  if (!top || top.salience < SALIENCE_THRESHOLD) {
    console.log(`-- beat: no salient cue (top=${top ? top.salience.toFixed(2) : 'none'})`);
    return;
  }
  try {
    const card = await fetchDossier({
      mention: top.mention,
      event: top.event ?? '',
      context: top.context,
    });
    const rendered = renderCard(card);
    console.log('\n=== HUD ===');
    console.log(rendered.header);
    if (rendered.subhead) console.log(`  ${rendered.subhead}`);
    for (const b of rendered.bullets) console.log(`  - ${b}`);
    console.log(`  [confidence ${card.confidence.toFixed(2)}]`);
  } catch (err) {
    console.warn('brain call failed:', err);
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
