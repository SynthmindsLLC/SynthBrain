import { z } from 'zod';

export const NoteSchema = z.object({
  id: z.string(),
  title: z.string(),
  content: z.string().optional(),
  created_at: z.string(),
  updated_at: z.string(),
  collection_ids: z.array(z.string()).default([]),
  tags: z.array(z.string()).default([]),
  source: z.string().default('mem'),
});
export type Note = z.infer<typeof NoteSchema>;

export const CollectionSchema = z.object({
  id: z.string(),
  title: z.string(),
  created_at: z.string(),
  updated_at: z.string(),
});
export type Collection = z.infer<typeof CollectionSchema>;

export const GraphNodeSchema = z.object({
  id: z.string(),
  label: z.string(),
  // note/collection/tag come from Mem-shaped sources; person/event/place/org
  // come from the Python brain's entity graph.
  kind: z.enum(['note', 'collection', 'tag', 'person', 'event', 'place', 'org']),
  source: z.string().default('mem'),
  color: z.string().optional(),
  size: z.number().default(1),
  degree: z.number().optional(),
  // Network-science features from the brain's graph-metrics run (graphlab):
  // eigenvector/pagerank/betweenness centralities + Louvain community index.
  eigenvector: z.number().optional(),
  pagerank: z.number().optional(),
  betweenness: z.number().optional(),
  community: z.number().optional(),
  updated_at: z.string().optional(),
});
export type GraphNode = z.infer<typeof GraphNodeSchema>;

export const GraphLinkSchema = z.object({
  source: z.string(),
  target: z.string(),
  // in_collection/has_tag/mention are Mem-shaped; the rest are brain edge rels.
  kind: z.enum([
    'in_collection',
    'has_tag',
    'mention',
    'attended',
    'mentioned_in',
    'discussed_with',
    'works_at',
    'family_of',
    // graphlab-derived rels (Newman-weighted co-attendance projection,
    // PMI-weighted chunk co-occurrence):
    'co_attended',
    'co_mentioned',
  ]),
});
export type GraphLink = z.infer<typeof GraphLinkSchema>;

export const GraphSchema = z.object({
  nodes: z.array(GraphNodeSchema),
  links: z.array(GraphLinkSchema),
  generated_at: z.string(),
  note_count: z.number(),
  collection_count: z.number(),
});
export type Graph = z.infer<typeof GraphSchema>;
