import { describe, expect, it } from 'vitest';

import { extractCues } from './salience.js';
import { enforceBudget, renderCard } from './hud.js';

describe('extractCues', () => {
  it('picks names with event-key boost', () => {
    const cues = extractCues({
      segments: [
        { text: 'Hey Jeff, long time. The Fall Block Party was last year.' },
      ],
    });
    expect(cues[0]?.mention).toBe('Jeff');
    expect(cues[0]?.event).toBe('party');
    expect(cues[0]?.salience).toBeGreaterThan(0);
  });

  it('boosts known names', () => {
    const known = new Set(['Jeff Torres']);
    const cues = extractCues({
      segments: [{ text: 'Jeff Torres said hi.' }],
      knownNames: known,
    });
    expect(cues[0]?.mention).toBe('Jeff Torres');
    expect(cues[0]?.salience).toBeGreaterThan(0.3);
  });

  it('emits nothing on a text with no Capitalized name', () => {
    const cues = extractCues({ segments: [{ text: 'we should grab lunch sometime' }] });
    expect(cues).toEqual([]);
  });
});

describe('enforceBudget', () => {
  it('truncates to <= 8 words per bullet, max 5 bullets', () => {
    const out = enforceBudget([
      'one two three four five six seven eight nine ten',
      'short',
      '',
      'three',
      'four',
      'five',
      'never shown',
    ]);
    expect(out).toHaveLength(5);
    expect(out[0]?.endsWith('...')).toBe(true);
    expect(out[0]?.split(' ').length).toBeLessThanOrEqual(9); // 8 words + "..."
    expect(out).not.toContain('never shown');
  });
});

describe('renderCard', () => {
  it('renders disambiguation chooser when needed', () => {
    const rendered = renderCard({
      name: 'Jeff',
      role: '',
      relationship: '',
      where_met: '',
      discussed: [],
      confidence: 0.5,
      needs_disambiguation: ['Jeff Torres', 'Jeff Brennan'],
      rationale: 'low confidence',
    });
    expect(rendered.bullets).toEqual(['or Jeff Torres?', 'or Jeff Brennan?']);
    expect(rendered.needsDisambiguation).toEqual(['Jeff Torres', 'Jeff Brennan']);
  });

  it('renders a normal card', () => {
    const rendered = renderCard({
      name: 'Jeff Torres',
      role: 'VP @ Acme',
      relationship: 'Married to Dana; two kids',
      where_met: 'Fall Block Party — Groton',
      discussed: ['conservation roadmap', 'kids soccer schedule'],
      confidence: 0.8,
      needs_disambiguation: [],
      rationale: '',
    });
    expect(rendered.header).toContain('Jeff Torres');
    expect(rendered.header).toContain('VP @ Acme');
    expect(rendered.subhead).toContain('Groton');
    expect(rendered.bullets.length).toBeGreaterThan(0);
  });
});
