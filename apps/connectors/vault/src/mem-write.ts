import type { MemNoteDraft } from './transform';

/**
 * Mem.ai write client (HTTP). Mirrors apps/web/lib/mem-http.ts (read side) but
 * for the create path. Defaults to dry-run: nothing is written unless `commit`
 * is explicitly set. Endpoint shape matches the Mem MCP tool surface
 * (create_collection, create_note with collection_titles).
 */

const MEM_API_BASE = process.env['MEM_API_BASE'] ?? 'https://api.mem.ai/v0';

export interface WriteResult {
  title: string;
  status: 'created' | 'skipped' | 'dry-run' | 'failed';
  id?: string;
  error?: string;
}

export class MemWriter {
  constructor(
    private readonly apiKey: string,
    private readonly commit: boolean,
  ) {}

  private headers(): Record<string, string> {
    return {
      Authorization: `ApiAccessToken ${this.apiKey}`,
      'Content-Type': 'application/json',
      Accept: 'application/json',
    };
  }

  async ensureCollection(title: string, description?: string): Promise<void> {
    if (!this.commit) {
      console.log(`[dry-run] ensureCollection("${title}")`);
      return;
    }
    const res = await fetch(`${MEM_API_BASE}/collections`, {
      method: 'POST',
      headers: this.headers(),
      body: JSON.stringify({ title, description }),
      signal: AbortSignal.timeout(15_000),
    });
    // 409 = already exists, which is fine.
    if (!res.ok && res.status !== 409) {
      throw new Error(`ensureCollection ${res.status}: ${(await res.text()).slice(0, 200)}`);
    }
  }

  async createNote(draft: MemNoteDraft): Promise<WriteResult> {
    if (!this.commit) {
      console.log(
        `[dry-run] create "${draft.title}" → ${draft.collection} ` +
          `(${draft.tags.length} tags${draft.escaped ? ', escaped' : ''})`,
      );
      return { title: draft.title, status: 'dry-run' };
    }
    try {
      const res = await fetch(`${MEM_API_BASE}/mems`, {
        method: 'POST',
        headers: this.headers(),
        body: JSON.stringify({
          content: draft.content,
          collection_titles: [draft.collection],
        }),
        signal: AbortSignal.timeout(30_000),
      });
      if (!res.ok) {
        return {
          title: draft.title,
          status: 'failed',
          error: `${res.status}: ${(await res.text()).slice(0, 200)}`,
        };
      }
      const body = (await res.json()) as { id?: string };
      return {
        title: draft.title,
        status: 'created',
        ...(body.id !== undefined ? { id: body.id } : {}),
      };
    } catch (err) {
      return {
        title: draft.title,
        status: 'failed',
        error: err instanceof Error ? err.message : String(err),
      };
    }
  }
}
