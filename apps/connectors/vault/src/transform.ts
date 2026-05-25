import {
  buildNoteContent,
  deriveTitle,
  escapeAngles,
  needsEscape,
  normalizeTag,
  splitFrontmatter,
} from '@synthbrain/normalize';

// Re-export shared helpers so existing imports/tests keep working.
export { deriveTitle, escapeAngles, needsEscape, normalizeTag };

export type Classification = 'migrate' | 'exclude-drawing' | 'drop-duplicate';

export interface VaultFile {
  /** absolute or vault-relative path */
  path: string;
  /** raw file contents */
  raw: string;
  /** stable hash of raw contents, for dedupe */
  hash: string;
}

export interface TransformOptions {
  collection: string;
  /** base tags applied to every note (without leading #) */
  baseTags: string[];
  /** group tag value (without the "group/" prefix), e.g. "random" */
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

/**
 * Classify a vault file. `seenHashes` accumulates content hashes so exact
 * duplicates (e.g. Obsidian's " 1.md" copies) are dropped on second sight.
 */
export function classify(file: VaultFile, seenHashes: Set<string>): Classification {
  if (/^---[\s\S]*?excalidraw/m.test(file.raw) || file.raw.includes('excalidraw-plugin')) {
    return 'exclude-drawing';
  }
  if (seenHashes.has(file.hash)) return 'drop-duplicate';
  seenHashes.add(file.hash);
  return 'migrate';
}

/** Build a Mem note draft from a vault file using the shared normalize transform. */
export function toMemNote(file: VaultFile, opts: TransformOptions): MemNoteDraft {
  const { body, tags: fmTags } = splitFrontmatter(file.raw);
  const title = deriveTitle(file.path);
  const status = opts.status.startsWith('status/') ? opts.status : `status/${opts.status}`;
  const allTags = [...opts.baseTags, `group/${opts.group}`, status, ...fmTags];
  const built = buildNoteContent({ title, tags: allTags, body });
  return {
    title,
    content: built.content,
    collection: opts.collection,
    tags: [...new Set(allTags.map(normalizeTag))].filter(Boolean),
    escaped: built.escaped,
  };
}
