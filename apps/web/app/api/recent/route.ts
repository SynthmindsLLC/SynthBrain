import type { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';

import { brainRecentChunks } from '../../../lib/brain-http';

export const dynamic = 'force-dynamic';
export const runtime = 'nodejs';

export async function GET(req: NextRequest) {
  const raw = Number(req.nextUrl.searchParams.get('limit') ?? 20);
  const limit = Number.isFinite(raw) ? Math.min(Math.max(Math.trunc(raw), 1), 200) : 20;
  const source = req.nextUrl.searchParams.get('source');
  const layer = req.nextUrl.searchParams.get('layer');
  try {
    return NextResponse.json(
      await brainRecentChunks({
        limit,
        ...(source ? { source } : {}),
        ...(layer ? { layer } : {}),
      }),
    );
  } catch (err) {
    const message = err instanceof Error ? err.message : 'unknown error';
    const outdated = message.includes('HTTP 404');
    return NextResponse.json(
      { error: outdated ? 'brain_outdated' : 'brain_unavailable', message },
      { status: 503 },
    );
  }
}
