import type { Collection, Graph, GraphLink, GraphNode, Note } from '@synthbrain/graph-schema';

import { colorForSource } from './source-colors';

export function buildGraph(notes: Note[], collections: Collection[]): Graph {
  const nodes: GraphNode[] = [];
  const links: GraphLink[] = [];

  for (const c of collections) {
    nodes.push({
      id: `c:${c.id}`,
      label: c.title || 'Untitled Collection',
      kind: 'collection',
      source: 'mem',
      color: '#ffffff',
      size: 2.5,
      updated_at: c.updated_at,
    });
  }

  for (const n of notes) {
    nodes.push({
      id: `n:${n.id}`,
      label: n.title || '(untitled)',
      kind: 'note',
      source: n.source ?? 'mem',
      color: colorForSource(n.source ?? 'mem'),
      size: 1,
      updated_at: n.updated_at,
    });
    for (const cid of n.collection_ids ?? []) {
      links.push({ source: `n:${n.id}`, target: `c:${cid}`, kind: 'in_collection' });
    }
    for (const tag of n.tags ?? []) {
      const tagId = `t:${tag.toLowerCase()}`;
      if (!nodes.find((x) => x.id === tagId)) {
        nodes.push({
          id: tagId,
          label: `#${tag}`,
          kind: 'tag',
          source: 'tag',
          color: '#777',
          size: 0.6,
        });
      }
      links.push({ source: `n:${n.id}`, target: tagId, kind: 'has_tag' });
    }
  }

  return {
    nodes,
    links,
    generated_at: new Date().toISOString(),
    note_count: notes.length,
    collection_count: collections.length,
  };
}
