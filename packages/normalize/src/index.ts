/**
 * Shared vault/doc → Mem normalization. Used by both connector-vault and
 * connector-drive so the transform rules (tag normalization, angle-bracket
 * escaping, Mem note assembly) live in exactly one place.
 */

export const NORMALIZE_PACKAGE = '@synthbrain/normalize';

const ANGLE_TAG = /<[A-Za-z/!]/;

/** Title from a filename or path: drop extension, trim, keep emoji. */
export function deriveTitle(pathOrName: string): string {
  const base = pathOrName.split('/').pop() ?? pathOrName;
  return base.replace(/\.[A-Za-z0-9]+$/, '').trim();
}

/** Normalize a raw tag token to Mem inline-tag form (no leading #, no spaces). */
export function normalizeTag(t: string): string {
  return t
    .replace(/^#+/, '')
    .trim()
    .replace(/\s+/g, '-')
    .toLowerCase();
}

/** True if the body contains XML/HTML-style angle-bracket constructs. */
export function needsEscape(body: string): boolean {
  return ANGLE_TAG.test(body);
}

/** Escape angle brackets so Mem preserves them verbatim (Mem strips raw <tags>). */
export function escapeAngles(body: string): string {
  return body.replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

/** Strip a leading YAML frontmatter block, returning the body and any `tags`. */
export function splitFrontmatter(raw: string): { body: string; tags: string[] } {
  if (!raw.startsWith('---')) return { body: raw, tags: [] };
  const end = raw.indexOf('\n---', 3);
  if (end < 0) return { body: raw, tags: [] };
  const fm = raw.slice(3, end);
  const body = raw.slice(end + 4).replace(/^\n+/, '');
  const tags: string[] = [];
  const tagBlock = fm.match(/tags:\s*((?:\n\s*-\s*.+)+|\[.*\]|.+)/);
  if (tagBlock) {
    for (const m of tagBlock[1]!.matchAll(/["'#]*([A-Za-z0-9_\-/]+)["']*/g)) {
      if (m[1] && m[1] !== 'tags') tags.push(m[1]);
    }
  }
  return { body, tags };
}

export interface BuildNoteInput {
  title: string;
  /** tag tokens without leading # */
  tags: string[];
  body: string;
  /** escape angle brackets (auto-detected if omitted) */
  escape?: boolean;
}

export interface BuiltNote {
  content: string;
  escaped: boolean;
}

/**
 * Assemble a Mem note body: first line = title, second block = `Tags:` line
 * (never starts with `#`, which Mem would treat as an H1), then the body.
 */
export function buildNoteContent(input: BuildNoteInput): BuiltNote {
  const escape = input.escape ?? needsEscape(input.body);
  const body = escape ? escapeAngles(input.body) : input.body;
  const tags = [...new Set(input.tags.map(normalizeTag))].filter(Boolean);
  const tagLine = `Tags: ${tags.map((t) => `#${t}`).join(' ')}`;
  return { content: `${input.title}\n\n${tagLine}\n\n${body}`, escaped: escape };
}
