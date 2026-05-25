import { describe, expect, it } from 'vitest';

import {
  NORMALIZE_PACKAGE,
  buildNoteContent,
  deriveTitle,
  escapeAngles,
  needsEscape,
  normalizeTag,
  splitFrontmatter,
} from './index';

describe('normalize', () => {
  it('exposes its package name', () => {
    expect(NORMALIZE_PACKAGE).toBe('@synthbrain/normalize');
  });

  it('derives titles and normalizes tags', () => {
    expect(deriveTitle('a/b/🧙 Pro.md')).toBe('🧙 Pro');
    expect(normalizeTag('#TextToImage')).toBe('texttoimage');
    expect(normalizeTag('Map of Content')).toBe('map-of-content');
  });

  it('detects and escapes angle brackets', () => {
    expect(needsEscape('<Agent>')).toBe(true);
    expect(needsEscape('[x]')).toBe(false);
    expect(escapeAngles('<a>&</a>')).toBe('&lt;a&gt;&&lt;/a&gt;');
  });

  it('splits frontmatter and collects tags', () => {
    const { body, tags } = splitFrontmatter('---\ntags:\n  - prompt\n  - "#blog"\n---\n# Hi');
    expect(body).toBe('# Hi');
    expect(tags).toContain('prompt');
    expect(tags).toContain('blog');
  });

  it('builds a Mem note: title, non-# tag line, body; escapes when needed', () => {
    const n = buildNoteContent({ title: 'T', tags: ['source/vault', 'prompt'], body: '<Agent>' });
    expect(n.content.startsWith('T\n\nTags: #source/vault #prompt\n\n')).toBe(true);
    expect(n.escaped).toBe(true);
    expect(n.content).toContain('&lt;Agent&gt;');
    expect(n.content).not.toContain('\n#'); // tag line must not start with #
  });
});
