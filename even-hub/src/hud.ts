// HUD render formatter — mirrors the truncation in brain/core/dossier.py
// so what the lens shows always matches what the brain returns.

import type { BrainCard } from './brain-client.js';
import { HUD_MAX_BULLETS, HUD_MAX_WORDS_PER_BULLET, type RenderedCard } from './types.js';

export const RESOLVE_CONFIDENCE_FLOOR = 0.6;

export function renderCard(card: BrainCard): RenderedCard {
  if (card.needs_disambiguation && card.needs_disambiguation.length > 0) {
    return {
      header: `${card.name}?`,
      bullets: card.needs_disambiguation.map((n) => `or ${n}?`),
      confidence: card.confidence,
      needsDisambiguation: card.needs_disambiguation,
    };
  }

  const headerParts = [card.name];
  if (card.role) headerParts.push(card.role);
  const header = headerParts.join(' - ');
  const subhead = card.where_met || undefined;
  const bullets = enforceBudget([
    ...(card.relationship ? [card.relationship] : []),
    ...card.discussed,
  ]);

  return { header, subhead, bullets, confidence: card.confidence };
}

export function enforceBudget(lines: string[]): string[] {
  const out: string[] = [];
  for (const raw of lines) {
    if (out.length >= HUD_MAX_BULLETS) break;
    const trimmed = raw.trim();
    if (!trimmed) continue;
    const words = trimmed.split(/\s+/);
    const truncated = words.slice(0, HUD_MAX_WORDS_PER_BULLET).join(' ');
    out.push(words.length > HUD_MAX_WORDS_PER_BULLET ? truncated + '...' : truncated);
  }
  return out;
}
