import 'server-only';

import type { Collection, Graph, GraphLink, GraphNode, Note } from '@synthbrain/graph-schema';

import seed from '../data/seed.json';

import type { BrainGraph } from './brain-http';
import { brainGraph } from './brain-http';
import { buildGraph } from './build-graph';
import { fetchMemNotes } from './mem-http';
import { colorForKind, colorForSource } from './source-colors';

type SeedFile = { notes: Note[]; collections: Collection[]; generated_at: string };

/**
 * Resolution order:
 *   1. Python brain HTTP API (BRAIN_URL set, or default http://127.0.0.1:8088)
 *      — the entity graph: people + events + edges. This is now canonical.
 *   2. Mem.ai HTTP API (MEM_API_KEY set) — legacy notes-as-graph view.
 *   3. Bundled seed.json — demo data so first deploy renders something.
 */
export async function getGraphData(): Promise<Graph> {
  if (process.env['BRAIN_URL'] || process.env['USE_BRAIN'] === '1') {
    try {
      const g = await brainGraph(800);
      if (g.nodes.length > 0) {
        return brainGraphToWebGraph(g);
      }
    } catch (err) {
      console.warn('[mem-source] brain fetch failed, falling back:', err);
    }
  }

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

function brainGraphToWebGraph(g: BrainGraph): Graph {
  // Brain kinds (person/event/place/org) and rels (attended/mentioned_in/…)
  // are first-class in the graph schema — pass them through natively instead
  // of lossily mapping onto Mem's note/collection shapes.
  const nodes: GraphNode[] = g.nodes.map((n) => ({
    id: n.id,
    label: n.label || n.name,
    kind: n.kind,
    source: 'brain',
    color: colorForKind(n.kind) ?? colorForSource('brain'),
    size: n.kind === 'event' ? 2.2 : 1.2,
    ...(n.degree !== undefined ? { degree: n.degree } : {}),
  }));
  const links: GraphLink[] = g.links.map((l) => ({
    source: l.source,
    target: l.target,
    kind: l.rel as GraphLink['kind'],
  }));
  return {
    nodes,
    links,
    generated_at: new Date().toISOString(),
    note_count: nodes.filter((n) => n.kind === 'note').length,
    collection_count: nodes.filter((n) => n.kind === 'collection').length,
  };
}

export type { Note, Collection, Graph, GraphNode, GraphLink };
