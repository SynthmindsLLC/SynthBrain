import { createHash } from 'node:crypto';
import { readdir, readFile, stat } from 'node:fs/promises';
import { join, relative } from 'node:path';

import { MemWriter } from './mem-write';
import { classify, toMemNote, type VaultFile } from './transform';

export interface RunOptions {
  /** absolute path to the vault folder to import */
  folder: string;
  /** Mem collection title */
  collection: string;
  /** actually write to Mem (default false = dry-run) */
  commit: boolean;
  /** base tags (without #) applied to every note */
  baseTags: string[];
  /** notes per batch */
  batchSize: number;
}

const WIP = /\bWIP\b|\(WIP\)/i;

export async function run(opts: RunOptions): Promise<void> {
  const apiKey = process.env['MEM_API_KEY'] ?? '';
  if (opts.commit && !apiKey) {
    throw new Error('MEM_API_KEY is required to --commit. Set it in .env.local.');
  }

  const files = await walkMarkdown(opts.folder);
  const writer = new MemWriter(apiKey, opts.commit);
  await writer.ensureCollection(opts.collection, `Imported from vault: ${opts.folder}`);

  const seen = new Set<string>();
  const counts = { created: 0, dryRun: 0, skipped: 0, failed: 0, excludedDrawing: 0, dropped: 0 };
  const drafts: ReturnType<typeof toMemNote>[] = [];

  for (const abs of files) {
    const raw = await readFile(abs, 'utf8');
    const hash = createHash('sha256').update(raw).digest('hex');
    const rel = relative(opts.folder, abs);
    const file: VaultFile = { path: rel, raw, hash };

    const verdict = classify(file, seen);
    if (verdict === 'exclude-drawing') {
      counts.excludedDrawing++;
      console.log(`[exclude] drawing: ${rel}`);
      continue;
    }
    if (verdict === 'drop-duplicate') {
      counts.dropped++;
      console.log(`[drop] duplicate: ${rel}`);
      continue;
    }

    const group = rel.includes('/') ? rel.split('/').slice(0, -1).join('-') : 'root';
    const status = WIP.test(rel) ? 'status/wip' : 'status/active';
    drafts.push(
      toMemNote(file, { collection: opts.collection, baseTags: opts.baseTags, group, status }),
    );
  }

  for (let i = 0; i < drafts.length; i += opts.batchSize) {
    const batch = drafts.slice(i, i + opts.batchSize);
    console.log(`\n--- batch ${i / opts.batchSize + 1} (${batch.length} notes) ---`);
    for (const draft of batch) {
      const r = await writer.createNote(draft);
      if (r.status === 'created') counts.created++;
      else if (r.status === 'dry-run') counts.dryRun++;
      else if (r.status === 'skipped') counts.skipped++;
      else if (r.status === 'failed') {
        counts.failed++;
        console.error(`[fail] ${r.title}: ${r.error}`);
      }
    }
  }

  console.log('\n=== summary ===');
  console.table(counts);
  if (!opts.commit) console.log('Dry-run only. Re-run with --commit to write to Mem.');
}

async function walkMarkdown(dir: string): Promise<string[]> {
  const out: string[] = [];
  for (const entry of await readdir(dir)) {
    const abs = join(dir, entry);
    const s = await stat(abs);
    if (s.isDirectory()) out.push(...(await walkMarkdown(abs)));
    else if (entry.toLowerCase().endsWith('.md')) out.push(abs);
  }
  return out.sort();
}
