import { DriveClient, type DriveFile } from './drive-client';
import { ingestToMem } from './mem-ingest';
import { classifyToTarget, suggestRename } from './taxonomy';

export interface OrganizeOptions {
  commit: boolean;
  /** also trash exact-duplicate files (same md5Checksum), keeping the largest/newest */
  dedupe: boolean;
  /** ingest relocated text docs into Mem (Reference/Knowledge targets) */
  ingest: boolean;
}

export async function organize(opts: OrganizeOptions): Promise<void> {
  const drive = new DriveClient(opts.commit);
  const root = await drive.listChildren('root');
  console.log(`Root contains ${root.length} items.`);

  const counts = {
    moved: 0,
    archived: 0,
    renamed: 0,
    trashed: 0,
    unmatched: 0,
    ingested: 0,
    ingestSkipped: 0,
  };

  // 1) Dedupe exact-content files (md5) before moving, so we don't relocate junk.
  if (opts.dedupe) {
    const byHash = new Map<string, DriveFile[]>();
    for (const f of root) {
      if (!f.md5Checksum) continue;
      const group = byHash.get(f.md5Checksum);
      if (group) group.push(f);
      else byHash.set(f.md5Checksum, [f]);
    }
    for (const group of byHash.values()) {
      if (group.length < 2) continue;
      // Keep the largest (then newest); trash the rest.
      group.sort((a, b) => Number(b.size ?? 0) - Number(a.size ?? 0));
      for (const dup of group.slice(1)) {
        await drive.trashFile(dup, `exact duplicate of "${group[0]!.name}"`);
        counts.trashed++;
      }
    }
  }

  // 2) Classify + move + rename.
  for (const f of root) {
    const rename = suggestRename(f);
    if (rename) {
      await drive.renameFile(f, rename);
      counts.renamed++;
    }
    const target = classifyToTarget(f);
    if (!target) {
      counts.unmatched++;
      console.log(`[review] no rule: "${f.name}" (${f.mimeType})`);
      continue;
    }
    const folderId = await drive.ensureFolderPath(target);
    await drive.moveFile(f, folderId, target.join('/'));
    if (target[0] === '_Archive') counts.archived++;
    else counts.moved++;

    if (opts.ingest) {
      const r = await ingestToMem(f, target, drive, opts.commit);
      if (r.status === 'ingested' || r.status === 'dry-run') counts.ingested++;
      else if (r.status === 'skipped-binary') counts.ingestSkipped++;
      else if (r.status === 'failed') console.error(`[ingest-fail] ${f.name}: ${r.detail}`);
    }
  }

  console.log('\n=== summary ===');
  console.table(counts);
  if (!opts.commit) console.log('Dry-run only. Re-run with --commit to apply to Drive.');
}
