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
  kind: z.enum(['note', 'collection', 'tag']),
  source: z.string().default('mem'),
  color: z.string().optional(),
  size: z.number().default(1),
  updated_at: z.string().optional(),
});
export type GraphNode = z.infer<typeof GraphNodeSchema>;

export const GraphLinkSchema = z.object({
  source: z.string(),
  target: z.string(),
  kind: z.enum(['in_collection', 'has_tag', 'mention']),
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
