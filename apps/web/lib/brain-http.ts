import 'server-only';

/**
 * Thin HTTP client for the Python brain's FastAPI surface.
 *
 * The Python brain is the source of truth (LanceDB chunks + SQLite entity
 * graph). This web app talks to it server-side via these routes:
 *
 *   GET  /healthz
 *   GET  /stats
 *   GET  /stats/breakdown
 *   GET  /ingest/runs?limit=N
 *   GET  /chunks/recent?limit=N&source=&layer=
 *   GET  /graph?limit=N&kind=&min_degree=
 *   GET  /who/{name}
 *   POST /resolve   { mention, context, kind }
 *   POST /dossier   { mention, event, context, use_chunks, k }
 *   POST /query     { text, k, layer, project, salience, salience_threshold }
 *
 * Env:
 *   BRAIN_URL           default http://127.0.0.1:8088
 *   BRAIN_BEARER_TOKEN  optional; sent as Authorization: Bearer ... when set
 */

const DEFAULT_BRAIN_URL = 'http://127.0.0.1:8088';

export interface BrainGraphNode {
  id: string;
  name: string;
  kind: 'person' | 'event' | 'place' | 'org';
  label: string;
  degree?: number;
  /** Network-science features from `brain graph-metrics`; null until run. */
  eigenvector?: number | null;
  pagerank?: number | null;
  betweenness?: number | null;
  community?: number | null;
}

export interface BrainGraphLink {
  source: string;
  target: string;
  rel: string;
}

export interface BrainGraph {
  nodes: BrainGraphNode[];
  links: BrainGraphLink[];
}

export interface BrainCard {
  name: string;
  role: string;
  relationship: string;
  where_met: string;
  discussed: string[];
  confidence: number;
  needs_disambiguation: string[];
  rationale: string;
}

export interface BrainQueryResult {
  text: string;
  source: string;
  source_id: string;
  url: string;
  layer: string;
  project_tags: string[];
  entity_tags: string[];
  score: number | null;
  salience?: {
    total: number;
    tfidf: number;
    recency: number;
    entity: number;
    layer_score: number;
    context: number;
  };
}

export interface BrainResolveResult {
  status: 'resolved' | 'ambiguous' | 'no_match';
  confidence: number;
  rationale: string;
  entity: {
    id: string;
    kind: string;
    name: string;
    aliases: string[];
    attributes: Record<string, unknown>;
  } | null;
  candidates: Array<{
    id: string;
    kind: string;
    name: string;
    aliases: string[];
    attributes: Record<string, unknown>;
  }>;
  scores: Array<{ id: string; score: number }>;
}

export interface BrainStats {
  chunks: number;
  graph: { entities: number; edges: number };
  db: string;
  entdb: string;
  embedder: string;
}

export interface BrainStatsBreakdown {
  chunks_total: number;
  by_source: Record<string, number>;
  by_layer: Record<string, number>;
  by_project: Record<string, number>;
  by_day: Array<{ date: string; chunks: number }>;
  entities: { total: number; by_kind: Record<string, number> };
  edges: { total: number; by_rel: Record<string, number> };
  generated_at: string;
}

export interface BrainIngestRun {
  run_id: string;
  adapter: string;
  source: string;
  started_at: string;
  finished_at: string | null;
  status: string;
  docs: number;
  chunks: number;
  errors: number;
  skipped: number;
  llm_classified: number;
  heuristic_classified: number;
  error_samples: string[];
  meta: Record<string, unknown>;
}

export interface BrainRecentChunk {
  id: string;
  text: string;
  source: string;
  source_id: string;
  url: string;
  layer: string;
  project_tags: string[];
  entity_tags: string[];
  created_at: string;
}

function brainUrl(): string {
  return (process.env['BRAIN_URL'] || DEFAULT_BRAIN_URL).replace(/\/$/, '');
}

function authHeaders(): Record<string, string> {
  const token = process.env['BRAIN_BEARER_TOKEN'];
  if (!token) return {};
  return { Authorization: `Bearer ${token}` };
}

async function brainGet<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(brainUrl() + path, {
    ...init,
    headers: { Accept: 'application/json', ...authHeaders(), ...(init?.headers ?? {}) },
    cache: 'no-store',
  });
  if (!res.ok) throw new Error(`brain ${path} -> HTTP ${res.status}`);
  return (await res.json()) as T;
}

async function brainPost<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(brainUrl() + path, {
    method: 'POST',
    body: JSON.stringify(body),
    headers: { 'Content-Type': 'application/json', Accept: 'application/json', ...authHeaders() },
    cache: 'no-store',
  });
  if (!res.ok) throw new Error(`brain ${path} -> HTTP ${res.status}`);
  return (await res.json()) as T;
}

export async function brainHealthz(): Promise<{ ok: boolean }> {
  return brainGet('/healthz');
}

export async function brainStats(): Promise<BrainStats> {
  return brainGet('/stats');
}

export async function brainStatsBreakdown(): Promise<BrainStatsBreakdown> {
  return brainGet('/stats/breakdown');
}

export async function brainIngestRuns(limit = 20): Promise<{ runs: BrainIngestRun[] }> {
  return brainGet(`/ingest/runs?limit=${encodeURIComponent(limit)}`);
}

export async function brainRecentChunks(
  args: { limit?: number; source?: string; layer?: string } = {},
): Promise<{ chunks: BrainRecentChunk[] }> {
  const params = new URLSearchParams();
  params.set('limit', String(args.limit ?? 20));
  if (args.source) params.set('source', args.source);
  if (args.layer) params.set('layer', args.layer);
  return brainGet(`/chunks/recent?${params.toString()}`);
}

export async function brainGraph(
  limit = 500,
  opts: { kind?: 'person' | 'event' | 'place' | 'org'; minDegree?: number } = {},
): Promise<BrainGraph> {
  const params = new URLSearchParams();
  params.set('limit', String(limit));
  if (opts.kind) params.set('kind', opts.kind);
  if (opts.minDegree !== undefined) params.set('min_degree', String(opts.minDegree));
  return brainGet(`/graph?${params.toString()}`);
}

export async function brainWho(name: string): Promise<unknown> {
  return brainGet(`/who/${encodeURIComponent(name)}`);
}

export async function brainResolve(args: {
  mention: string;
  context?: string;
  kind?: 'person' | 'event' | 'place' | 'org';
}): Promise<BrainResolveResult> {
  return brainPost('/resolve', args);
}

export async function brainDossier(args: {
  mention: string;
  event?: string;
  context?: string;
  use_chunks?: boolean;
  k?: number;
}): Promise<BrainCard> {
  return brainPost('/dossier', args);
}

export async function brainQuery(args: {
  text: string;
  k?: number;
  layer?: string;
  project?: string;
  salience?: boolean;
  salience_threshold?: number;
}): Promise<{ text: string; results: BrainQueryResult[] }> {
  return brainPost('/query', args);
}
