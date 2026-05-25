import { buildNoteContent, splitFrontmatter } from '@synthbrain/normalize';

import type { DriveClient, DriveFile } from './drive-client';
import type { Target } from './taxonomy';

/**
 * Second pass: ingest relocated docs into Mem. Only text-extractable files
 * (Google Docs → markdown export, native .md/.txt) bound for a Mem-mapped
 * target are ingested. Binary types (PDF/docx/video) are skipped and reported
 * for a later extraction pass.
 *
 * Mem-mapped targets and their collection + tags:
 */
const TARGET_TO_MEM: Record<string, { collection: string; tags: string[] }> = {
  'Reference/Prompts': {
    collection: 'Reference/Prompts',
    tags: ['source/drive', 'type/reference', 'domain/prompt-engineering', 'prompt'],
  },
  'Reference/BrandProfiles': {
    collection: 'Reference/BrandProfiles',
    tags: ['source/drive', 'type/reference', 'domain/brand'],
  },
  'Knowledge/Meetings': {
    collection: 'Sources/Meetings',
    tags: ['source/drive', 'type/meeting'],
  },
};

const MEM_API_BASE = process.env['MEM_API_BASE'] ?? 'https://api.mem.ai/v0';

export interface IngestResult {
  status: 'ingested' | 'skipped-binary' | 'dry-run' | 'failed' | 'not-mem-bound';
  detail?: string;
}

export async function ingestToMem(
  file: DriveFile,
  target: Target,
  drive: DriveClient,
  commit: boolean,
): Promise<IngestResult> {
  const key = target.join('/');
  const map = TARGET_TO_MEM[key];
  if (!map) return { status: 'not-mem-bound' };

  const text = await drive.exportText(file);
  if (text === null) return { status: 'skipped-binary', detail: file.mimeType };

  const { body, tags: fmTags } = splitFrontmatter(text);
  const { content } = buildNoteContent({
    title: file.name.replace(/\.[A-Za-z0-9]+$/, ''),
    tags: [...map.tags, ...fmTags],
    body,
  });

  if (!commit) {
    console.log(`[dry-run] ingest "${file.name}" → Mem ${map.collection}`);
    return { status: 'dry-run' };
  }

  const apiKey = process.env['MEM_API_KEY'];
  if (!apiKey) return { status: 'failed', detail: 'MEM_API_KEY not set' };

  try {
    const res = await fetch(`${MEM_API_BASE}/mems`, {
      method: 'POST',
      headers: {
        Authorization: `ApiAccessToken ${apiKey}`,
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: JSON.stringify({ content, collection_titles: [map.collection] }),
      signal: AbortSignal.timeout(30_000),
    });
    if (!res.ok) return { status: 'failed', detail: `${res.status}` };
    console.log(`[ingest] "${file.name}" → Mem ${map.collection}`);
    return { status: 'ingested' };
  } catch (err) {
    return { status: 'failed', detail: err instanceof Error ? err.message : String(err) };
  }
}
