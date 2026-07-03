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

  it('parses brain entity node kinds', () => {
    for (const kind of ['person', 'event', 'place', 'org'] as const) {
      const node = GraphNodeSchema.parse({ id: `e:${kind}`, label: kind, kind, source: 'brain' });
      expect(node.kind).toBe(kind);
    }
  });

  it('parses an optional degree on nodes', () => {
    const withDegree = GraphNodeSchema.parse({
      id: 'p:jeff',
      label: 'Jeff Torres',
      kind: 'person',
      source: 'brain',
      degree: 4,
    });
    expect(withDegree.degree).toBe(4);

    const withoutDegree = GraphNodeSchema.parse({ id: 'n1', label: 'A', kind: 'note' });
    expect(withoutDegree.degree).toBeUndefined();
  });

  it('rejects unknown node kinds', () => {
    expect(() => GraphNodeSchema.parse({ id: 'x', label: 'X', kind: 'galaxy' })).toThrow();
  });

  it('parses brain link rels', () => {
    for (const kind of [
      'attended',
      'mentioned_in',
      'discussed_with',
      'works_at',
      'family_of',
    ] as const) {
      const link = GraphLinkSchema.parse({ source: 'p:jeff', target: 'e:party', kind });
      expect(link.kind).toBe(kind);
    }
  });

  it('rejects unknown link kinds', () => {
    expect(() => GraphLinkSchema.parse({ source: 'a', target: 'b', kind: 'married_to' })).toThrow();
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
