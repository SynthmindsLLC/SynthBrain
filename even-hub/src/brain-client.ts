// Talks to the Python brain's FastAPI surface from the plugin.

const DEFAULT_URL = 'http://127.0.0.1:8088';

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

export interface DossierArgs {
  mention: string;
  event?: string;
  context?: string;
  k?: number;
}

function url(): string {
  return (process.env['BRAIN_URL'] ?? DEFAULT_URL).replace(/\/$/, '');
}

function headers(): Record<string, string> {
  const h: Record<string, string> = {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  };
  const token = process.env['BRAIN_BEARER_TOKEN'];
  if (token) h['Authorization'] = `Bearer ${token}`;
  return h;
}

export async function fetchDossier(args: DossierArgs): Promise<BrainCard> {
  const res = await fetch(url() + '/dossier', {
    method: 'POST',
    headers: headers(),
    body: JSON.stringify({
      mention: args.mention,
      event: args.event ?? '',
      context: args.context ?? '',
      use_chunks: true,
      k: args.k ?? 6,
    }),
  });
  if (!res.ok) throw new Error(`brain /dossier -> HTTP ${res.status}`);
  return (await res.json()) as BrainCard;
}

export async function fetchKnownNames(): Promise<Set<string>> {
  const res = await fetch(url() + '/graph?limit=500', { headers: headers() });
  if (!res.ok) return new Set();
  const body = (await res.json()) as { nodes: Array<{ kind: string; name: string }> };
  const out = new Set<string>();
  for (const n of body.nodes) if (n.kind === 'person') out.add(n.name);
  return out;
}
