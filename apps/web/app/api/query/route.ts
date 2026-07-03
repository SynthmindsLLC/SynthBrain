import type { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';

import { brainQuery } from '../../../lib/brain-http';

export const dynamic = 'force-dynamic';
export const runtime = 'nodejs';

interface Body {
  text: string;
  k?: number;
  layer?: string;
  project?: string;
}

export async function POST(req: NextRequest) {
  let body: Body;
  try {
    body = (await req.json()) as Body;
  } catch {
    return NextResponse.json({ error: 'invalid_json' }, { status: 400 });
  }
  if (!body.text || typeof body.text !== 'string' || !body.text.trim()) {
    return NextResponse.json({ error: 'text required' }, { status: 400 });
  }
  const k =
    typeof body.k === 'number' && Number.isFinite(body.k)
      ? Math.min(Math.max(Math.trunc(body.k), 1), 50)
      : 8;
  try {
    const result = await brainQuery({
      text: body.text.trim(),
      k,
      ...(typeof body.layer === 'string' && body.layer ? { layer: body.layer } : {}),
      ...(typeof body.project === 'string' && body.project ? { project: body.project } : {}),
    });
    return NextResponse.json(result);
  } catch (err) {
    const message = err instanceof Error ? err.message : 'unknown error';
    return NextResponse.json({ error: 'brain_unavailable', message }, { status: 503 });
  }
}
