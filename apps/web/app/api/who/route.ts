import { NextRequest, NextResponse } from 'next/server';

import { brainWho } from '../../../lib/brain-http';

export const dynamic = 'force-dynamic';
export const runtime = 'nodejs';

export async function GET(req: NextRequest) {
  const name = req.nextUrl.searchParams.get('name');
  if (!name) return NextResponse.json({ error: 'name required' }, { status: 400 });
  try {
    return NextResponse.json(await brainWho(name));
  } catch (err) {
    const message = err instanceof Error ? err.message : 'unknown error';
    return NextResponse.json({ error: 'brain_unavailable', message }, { status: 503 });
  }
}
