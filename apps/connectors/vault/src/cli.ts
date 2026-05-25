#!/usr/bin/env tsx
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';

import { run } from './run';

const argv = await yargs(hideBin(process.argv))
  .scriptName('synthbrain-vault')
  .usage('$0 --folder <path> --collection <name> [--commit]')
  .option('folder', {
    type: 'string',
    demandOption: true,
    describe: 'Vault folder to import (absolute path)',
  })
  .option('collection', {
    type: 'string',
    default: 'Reference/Prompts',
    describe: 'Mem collection title',
  })
  .option('commit', {
    type: 'boolean',
    default: false,
    describe: 'Actually write to Mem (default: dry-run)',
  })
  .option('base-tags', {
    type: 'string',
    default: 'source/vault,type/reference,domain/prompt-engineering,prompt',
    describe: 'Comma-separated base tags (without #)',
  })
  .option('batch-size', { type: 'number', default: 10, describe: 'Notes per batch' })
  .strict()
  .help()
  .parse();

await run({
  folder: argv.folder,
  collection: argv.collection,
  commit: argv.commit,
  baseTags: argv['base-tags'].split(',').map((s) => s.trim()).filter(Boolean),
  batchSize: argv['batch-size'],
});
