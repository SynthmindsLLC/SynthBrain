import { NextResponse } from 'next/server';

import { getGraphData } from '../../../lib/mem-source';

export const dynamic = 'force-dynamic';
export const runtime = 'nodejs';

export async function GET() {
  try {
    const graph = await getGraphData();
    return NextResponse.json(graph, {
      headers: { 'Cache-Control': 'private, max-age=60' },
    });
  } catch (error) {
    const message = error instanceof Error ? error.message : 'unknown error';
    return NextResponse.json({ error: 'graph_unavailable', message }, { status: 503 });
  }
}
