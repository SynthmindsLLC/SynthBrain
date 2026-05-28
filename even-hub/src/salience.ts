// Lightweight TS port of brain/core/salience.py — the on-device pre-filter.
// Don't call the brain on every transcript line; only when something looks
// like a salient person/event cue.

const NAME_RE = /\b([A-Z][a-z]{2,})(?:\s+([A-Z][a-z]{2,}))?\b/g;
const EVENT_KEYS = [
  'party', 'gala', 'meeting', 'lunch', 'dinner', 'conference', 'wedding',
  'reception', 'demo', 'review', 'standup', 'sync', 'event',
];

export interface SalienceInput {
  /** Recent transcript window, in time order. */
  segments: { text: string }[];
  /** Optional known-entity names to bias toward (from the brain's /graph). */
  knownNames?: Set<string>;
}

export interface SalientCueDraft {
  mention: string;
  event?: string;
  context: string;
  salience: number;
}

export function extractCues(input: SalienceInput): SalientCueDraft[] {
  const context = input.segments.map((s) => s.text).join(' ').trim();
  if (!context) return [];

  const mentions = new Map<string, number>(); // name -> occurrence count
  for (const m of context.matchAll(NAME_RE)) {
    const full = m[2] ? `${m[1]} ${m[2]}` : m[1];
    if (!full) continue;
    mentions.set(full, (mentions.get(full) ?? 0) + 1);
  }

  const lower = context.toLowerCase();
  const event = EVENT_KEYS.find((k) => lower.includes(k));

  const draft: SalientCueDraft[] = [];
  for (const [mention, count] of mentions) {
    const knownBoost = input.knownNames?.has(mention) ? 0.4 : 0;
    const eventBoost = event ? 0.25 : 0;
    const countSignal = 1 - Math.exp(-count / 2);
    const salience = clamp01(noisyOr([countSignal, knownBoost, eventBoost]));
    if (salience <= 0) continue;
    draft.push({
      mention,
      event,
      context,
      salience: round(salience),
    });
  }
  draft.sort((a, b) => b.salience - a.salience);
  return draft;
}

function noisyOr(signals: number[]): number {
  let p = 1.0;
  for (const s of signals) p *= 1.0 - clamp01(s);
  return 1.0 - p;
}

function clamp01(v: number): number {
  if (Number.isNaN(v)) return 0;
  return v < 0 ? 0 : v > 1 ? 1 : v;
}

function round(v: number): number {
  return Math.round(v * 10000) / 10000;
}
