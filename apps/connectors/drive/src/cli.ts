#!/usr/bin/env tsx
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';

import { organize } from './organize';

const argv = await yargs(hideBin(process.argv))
  .scriptName('synthbrain-drive')
  .usage('$0 [--commit] [--dedupe]')
  .option('commit', {
    type: 'boolean',
    default: false,
    describe: 'Apply changes to Drive (default: dry-run, no writes)',
  })
  .option('dedupe', {
    type: 'boolean',
    default: false,
    describe: 'Trash exact-content duplicate files (keeps largest), Drive trash is reversible',
  })
  .option('ingest', {
    type: 'boolean',
    default: false,
    describe: 'Ingest relocated text docs (Google Docs/.md/.txt) into Mem (needs MEM_API_KEY)',
  })
  .strict()
  .help()
  .parse();

await organize({ commit: argv.commit, dedupe: argv.dedupe, ingest: argv.ingest });
