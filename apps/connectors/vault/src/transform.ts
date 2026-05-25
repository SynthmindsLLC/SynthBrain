import matter from 'gray-matter';

/**
 * Vault → Mem note transform. Encodes the rules proven in the 04-Prompts pilot:
 * - strip Obsidian frontmatter, merge its tags into the inline tag line
 * - escape angle-bracket / XML-style content so Mem stores it verbatim
 *   (Mem's markdown sanitizer otherwise strips `<tag>` and mangles HTML comments)
 * - first line of the Mem note is the title; tags live on a `Tags:` line
 *   (a leading `#` at line-start is treated as an H1 by Mem, so never start
 *   the tag line with a hashtag)
 */

export type Classification = 'migrate' | 'exclude-drawing' | 'drop-duplicate';

export interface VaultFile {
  /** absolute or vault-relative path */
  path: string;
  /** raw file contents */
  raw: string;
  /** sha256 (or any stable hash) of raw contents, for dedupe */
  hash: string;
}

export interface TransformOptions {
  /** collection this note belongs to, e.g. "Reference/Prompts" */
  collection: string;
  /** base tags applied to every note (without the leading #) */
  baseTags: string[];
  /** group tag derived from subfolder, e.g. "group/random" */
  group: string;
  /** status tag, e.g. "status/active" or "status/wip" */
  status: string;
}

export interface MemNoteDraft {
  title: string;
  content: string;
  collection: string;
  tags: string[];
  escaped: boolean;
}

const ANGLE_TAG = /<[A-Za-z/!]/;

/** Title from filename: drop extension, trim, keep emoji. */
export function deriveTitle(path: string): string {
  const base = path.split('/').pop() ?? path;
  return base.replace(/\.md$/i, '').trim();
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

/** Escape angle brackets so Mem preserves them verbatim. */
export function escapeAngles(body: string): string {
  return body.replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

/**
 * Classify a vault file. `seenHashes` accumulates content hashes so exact
 * duplicates (e.g. Obsidian's " 1.md" copies) are dropped on second sight.
 */
export function classify(file: VaultFile, seenHashes: Set<string>): Classification {
  // Excalidraw drawings are .md files but contain canvas JSON, not prose.
  if (/^---[\s\S]*?excalidraw/m.test(file.raw) || file.raw.includes('excalidraw-plugin')) {
    return 'exclude-drawing';
  }
  if (seenHashes.has(file.hash)) return 'drop-duplicate';
  seenHashes.add(file.hash);
  return 'migrate';
}

/** Build a Mem note draft from a vault file. */
export function toMemNote(file: VaultFile, opts: TransformOptions): MemNoteDraft {
  const parsed = matter(file.raw);
  const fmTags = extractFrontmatterTags(parsed.data);
  let body = parsed.content.replace(/^\n+/, '');

  const escaped = needsEscape(body);
  if (escaped) body = escapeAngles(body);

  const tags = dedupe([
    ...opts.baseTags.map(normalizeTag),
    `group/${opts.group.replace(/^group\//, '')}`.replace(/^group\/group\//, 'group/'),
    opts.status.startsWith('status/') ? opts.status : `status/${opts.status}`,
    ...fmTags.map(normalizeTag),
  ]).filter(Boolean);

  const title = deriveTitle(file.path);
  const tagLine = `Tags: ${tags.map((t) => `#${t}`).join(' ')}`;
  const content = `${title}\n\n${tagLine}\n\n${body}`;

  return { title, content, collection: opts.collection, tags, escaped };
}

function extractFrontmatterTags(data: Record<string, unknown>): string[] {
  const t = data['tags'];
  if (Array.isArray(t)) return t.map(String);
  if (typeof t === 'string') return t.split(/[\s,]+/);
  return [];
}

function dedupe(arr: string[]): string[] {
  return [...new Set(arr)];
}
