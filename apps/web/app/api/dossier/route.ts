import type { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';

import { brainDossier, brainResolve } from '../../../lib/brain-http';

export const dynamic = 'force-dynamic';
export const runtime = 'nodejs';

interface Body {
  mention: string;
  event?: string;
  context?: string;
  use_chunks?: boolean;
  k?: number;
  resolve_only?: boolean;
}

export async function POST(req: NextRequest) {
  let body: Body;
  try {
    body = (await req.json()) as Body;
  } catch {
    return NextResponse.json({ error: 'invalid_json' }, { status: 400 });
  }
  if (!body.mention || typeof body.mention !== 'string') {
    return NextResponse.json({ error: 'mention required' }, { status: 400 });
  }
  try {
    if (body.resolve_only) {
      const res = await brainResolve({
        mention: body.mention,
        ...(body.context !== undefined ? { context: body.context } : {}),
        kind: 'person',
      });
      return NextResponse.json(res);
    }
    const card = await brainDossier({
      mention: body.mention,
      event: body.event ?? '',
      context: body.context ?? '',
      use_chunks: body.use_chunks ?? true,
      k: body.k ?? 6,
    });
    return NextResponse.json(card);
  } catch (err) {
    const message = err instanceof Error ? err.message : 'unknown error';
    return NextResponse.json({ error: 'brain_unavailable', message }, { status: 503 });
  }
}
