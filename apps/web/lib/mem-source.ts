import 'server-only';

import type { Collection, Graph, GraphLink, GraphNode, Note } from '@synthbrain/graph-schema';

import { buildGraph } from './build-graph';
import { fetchMemNotes } from './mem-http';
import seed from '../data/seed.json';

type SeedFile = { notes: Note[]; collections: Collection[]; generated_at: string };

export async function getGraphData(): Promise<Graph> {
  const apiKey = process.env['MEM_API_KEY'];

  if (apiKey) {
    try {
      const live = await fetchMemNotes(apiKey);
      if (live.notes.length > 0) {
        return buildGraph(live.notes, live.collections);
      }
    } catch (err) {
      console.warn('[mem-source] live fetch failed, falling back to seed:', err);
    }
  }

  const s = seed as SeedFile;
  return buildGraph(s.notes, s.collections);
}

export type { Note, Collection, Graph, GraphNode, GraphLink };
