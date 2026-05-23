import type { Collection, Note } from '@synthbrain/graph-schema';

// Mem.ai HTTP API surface — base URL inferred from public posts on get.mem.ai/blog
// and the MCP server's tool surface (list_notes, get_note, list_collections, search_notes).
// If the real endpoints differ in production, only this file needs to change.
const MEM_API_BASE = process.env['MEM_API_BASE'] ?? 'https://api.mem.ai/v0';

type MemListResponse<T> = { items?: T[]; data?: T[]; next_page?: string | null };

function authHeaders(apiKey: string): HeadersInit {
  return {
    Authorization: `ApiAccessToken ${apiKey}`,
    Accept: 'application/json',
  };
}

async function memFetch<T>(apiKey: string, path: string, query: Record<string, string> = {}): Promise<T> {
  const url = new URL(`${MEM_API_BASE}${path}`);
  for (const [k, v] of Object.entries(query)) url.searchParams.set(k, v);
  const res = await fetch(url, {
    headers: authHeaders(apiKey),
    signal: AbortSignal.timeout(10_000),
  });
  if (!res.ok) {
    throw new Error(`Mem ${res.status} on ${path}: ${(await res.text()).slice(0, 200)}`);
  }
  return (await res.json()) as T;
}

type MemNote = {
  id: string;
  title?: string;
  content?: string;
  markdown?: string;
  created_at: string;
  updated_at: string;
  collection_ids?: string[];
  tags?: string[] | { name: string }[];
};

type MemCollection = {
  id: string;
  title?: string;
  name?: string;
  created_at: string;
  updated_at: string;
};

function normalizeNote(m: MemNote): Note {
  const tags = Array.isArray(m.tags)
    ? m.tags.map((t) => (typeof t === 'string' ? t : t.name))
    : [];
  return {
    id: m.id,
    title: m.title ?? '(untitled)',
    content: m.content ?? m.markdown ?? '',
    created_at: m.created_at,
    updated_at: m.updated_at,
    collection_ids: m.collection_ids ?? [],
    tags,
    source: 'mem',
  };
}

function normalizeCollection(c: MemCollection): Collection {
  return {
    id: c.id,
    title: c.title ?? c.name ?? 'Untitled Collection',
    created_at: c.created_at,
    updated_at: c.updated_at,
  };
}

async function listAll<T, U>(
  apiKey: string,
  path: string,
  normalize: (raw: T) => U,
  maxPages = 50,
): Promise<U[]> {
  const out: U[] = [];
  let page: string | undefined;
  for (let i = 0; i < maxPages; i++) {
    const query: Record<string, string> = { limit: '100' };
    if (page) query['page'] = page;
    const resp = await memFetch<MemListResponse<T>>(apiKey, path, query);
    const items = resp.items ?? resp.data ?? [];
    for (const raw of items) out.push(normalize(raw));
    if (!resp.next_page) break;
    page = resp.next_page;
  }
  return out;
}

export async function fetchMemNotes(
  apiKey: string,
): Promise<{ notes: Note[]; collections: Collection[] }> {
  const [collections, notes] = await Promise.all([
    listAll<MemCollection, Collection>(apiKey, '/collections', normalizeCollection),
    listAll<MemNote, Note>(apiKey, '/mems', normalizeNote),
  ]);
  return { notes, collections };
}
