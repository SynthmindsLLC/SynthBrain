import { describe, expect, it } from 'vitest';

import { GraphLinkSchema, GraphNodeSchema, GraphSchema, NoteSchema } from './index';

describe('graph-schema', () => {
  it('parses a valid note', () => {
    const note = NoteSchema.parse({
      id: 'n1',
      title: 'Hello',
      created_at: '2026-01-01T00:00:00Z',
      updated_at: '2026-01-01T00:00:00Z',
    });
    expect(note.collection_ids).toEqual([]);
    expect(note.tags).toEqual([]);
    expect(note.source).toBe('mem');
  });

  it('parses a graph node with source coloring', () => {
    const node = GraphNodeSchema.parse({ id: 'n1', label: 'A', kind: 'note' });
    expect(node.size).toBe(1);
    expect(node.source).toBe('mem');
  });

  it('parses a link', () => {
    const link = GraphLinkSchema.parse({ source: 'n1', target: 'c1', kind: 'in_collection' });
    expect(link.kind).toBe('in_collection');
  });

  it('parses an empty graph', () => {
    const g = GraphSchema.parse({
      nodes: [],
      links: [],
      generated_at: '2026-01-01T00:00:00Z',
      note_count: 0,
      collection_count: 0,
    });
    expect(g.nodes).toHaveLength(0);
  });
});
