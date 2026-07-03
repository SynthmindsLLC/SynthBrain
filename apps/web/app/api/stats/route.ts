import { NextResponse } from 'next/server';

import { brainStats, brainStatsBreakdown } from '../../../lib/brain-http';

export const dynamic = 'force-dynamic';
export const runtime = 'nodejs';

/**
 * Merges the brain's GET /stats + GET /stats/breakdown into one payload.
 * `breakdown` is null when the brain predates /stats/breakdown (404) so the
 * dashboard can render base stats and flag the rest as "brain outdated".
 */
export async function GET() {
  const [stats, breakdown] = await Promise.allSettled([brainStats(), brainStatsBreakdown()]);
  if (stats.status === 'rejected') {
    const message = stats.reason instanceof Error ? stats.reason.message : 'unknown error';
    return NextResponse.json({ error: 'brain_unavailable', message }, { status: 503 });
  }
  return NextResponse.json({
    stats: stats.value,
    breakdown: breakdown.status === 'fulfilled' ? breakdown.value : null,
    generated_at: new Date().toISOString(),
  });
}
