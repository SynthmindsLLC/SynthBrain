import { NextResponse } from 'next/server';

import { brainStats, brainStatsBreakdown } from '../../../lib/brain-http';

export const dynamic = 'force-dynamic';
export const runtime = 'nodejs';

/**
 * Merges the brain's GET /stats + GET /stats/breakdown into one payload.
 * `breakdown` is null ONLY when the brain predates /stats/breakdown (HTTP
 * 404 = "brain outdated"); any other breakdown failure is transient and is
 * reported via `breakdown_error` so the panel doesn't claim "outdated"
 * against a healthy brain that hiccuped once.
 */
export async function GET() {
  const [stats, breakdown] = await Promise.allSettled([brainStats(), brainStatsBreakdown()]);
  if (stats.status === 'rejected') {
    const message = stats.reason instanceof Error ? stats.reason.message : 'unknown error';
    return NextResponse.json({ error: 'brain_unavailable', message }, { status: 503 });
  }
  let breakdownValue = null;
  let breakdownError: string | null = null;
  if (breakdown.status === 'fulfilled') {
    breakdownValue = breakdown.value;
  } else {
    const message = breakdown.reason instanceof Error ? breakdown.reason.message : 'unknown error';
    if (!message.includes('HTTP 404')) breakdownError = message;
  }
  return NextResponse.json({
    stats: stats.value,
    breakdown: breakdownValue,
    ...(breakdownError ? { breakdown_error: breakdownError } : {}),
    generated_at: new Date().toISOString(),
  });
}
