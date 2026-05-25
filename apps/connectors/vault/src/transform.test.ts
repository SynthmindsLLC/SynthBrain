import { describe, expect, it } from 'vitest';

import {
  classify,
  deriveTitle,
  escapeAngles,
  needsEscape,
  normalizeTag,
  toMemNote,
  type VaultFile,
} from './transform';

const opts = {
  collection: 'Reference/Prompts',
  baseTags: ['source/vault', 'type/reference', 'prompt'],
  group: 'root',
  status: 'status/active',
};

describe('deriveTitle', () => {
  it('drops extension and keeps emoji', () => {
    expect(deriveTitle('foo/🧙 Professor Synapse.md')).toBe('🧙 Professor Synapse');
  });
});

describe('normalizeTag', () => {
  it('strips leading # and lowercases', () => {
    expect(normalizeTag('#ProfessorSynapse')).toBe('professorsynapse');
    expect(normalizeTag('Text To Image')).toBe('text-to-image');
  });
});

describe('needsEscape / escapeAngles', () => {
  it('detects XML-style tags', () => {
    expect(needsEscape('use <Agent> here')).toBe(true);
    expect(needsEscape('plain [bracket] text')).toBe(false);
  });
  it('escapes angle brackets', () => {
    expect(escapeAngles('<Agent>x</Agent>')).toBe('&lt;Agent&gt;x&lt;/Agent&gt;');
  });
});

describe('classify', () => {
  it('excludes excalidraw drawings', () => {
    const f: VaultFile = { path: 'a.md', raw: '---\nexcalidraw-plugin: parsed\n---\n{}', hash: 'h1' };
    expect(classify(f, new Set())).toBe('exclude-drawing');
  });
  it('drops exact duplicates on second sight', () => {
    const seen = new Set<string>();
    const a: VaultFile = { path: 'a.md', raw: 'same', hash: 'dup' };
    const b: VaultFile = { path: 'a 1.md', raw: 'same', hash: 'dup' };
    expect(classify(a, seen)).toBe('migrate');
    expect(classify(b, seen)).toBe('drop-duplicate');
  });
});

describe('toMemNote', () => {
  it('builds title + Tags line + body, merges frontmatter tags', () => {
    const f: VaultFile = {
      path: 'Meeting Notes.md',
      raw: '---\ntags:\n  - prompt\n  - meeting\n---\n# MISSION\nSummarize.',
      hash: 'h',
    };
    const note = toMemNote(f, opts);
    expect(note.title).toBe('Meeting Notes');
    expect(note.content.startsWith('Meeting Notes\n\nTags: #')).toBe(true);
    expect(note.tags).toContain('meeting');
    expect(note.tags).toContain('source/vault');
    expect(note.tags).toContain('status/active');
    expect(note.escaped).toBe(false);
    // tag line must not start with a hashtag (Mem treats #... at line start as H1)
    expect(note.content).toContain('\nTags: #');
  });

  it('escapes angle-bracket content', () => {
    const f: VaultFile = { path: 'EvaLuate.md', raw: '<Agent>do x</Agent>', hash: 'h' };
    const note = toMemNote(f, opts);
    expect(note.escaped).toBe(true);
    expect(note.content).toContain('&lt;Agent&gt;');
    expect(note.content).not.toContain('<Agent>');
  });
});
