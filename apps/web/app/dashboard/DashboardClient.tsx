'use client';

import { formatClock, formatNumber, formatRelative } from '../../lib/format';
import { usePolling } from '../../lib/use-polling';

import { ClassificationPanel } from './ClassificationPanel';
import { GraphPanel } from './GraphPanel';
import { IntakePanel } from './IntakePanel';
import { RecallPanel } from './RecallPanel';
import type { RunsResponse, StatsResponse } from './types';
import { Skeleton, glass } from './ui';

export function DashboardClient() {
  const stats = usePolling<StatsResponse>('/api/stats', 5000);
  const runs = usePolling<RunsResponse>('/api/runs?limit=20', 5000);

  const base = stats.data?.stats ?? null;
  const breakdown = stats.data?.breakdown ?? null;
  const latestRun = runs.data?.runs[0] ?? null;

  const kpis: Array<{ label: string; value: string }> = [
    { label: 'Chunks', value: formatNumber(breakdown?.chunks_total ?? base?.chunks) },
    { label: 'Entities', value: formatNumber(breakdown?.entities.total ?? base?.graph.entities) },
    { label: 'Edges', value: formatNumber(breakdown?.edges.total ?? base?.graph.edges) },
    {
      label: 'Last ingest',
      value: latestRun ? formatRelative(latestRun.finished_at ?? latestRun.started_at) : '—',
    },
    { label: 'Embedder', value: base?.embedder ?? '—' },
  ];

  return (
    <main
      style={{
        minHeight: '100vh',
        padding:
          'calc(env(safe-area-inset-top) + 20px) 20px calc(env(safe-area-inset-bottom) + 32px)',
        maxWidth: 1440,
        margin: '0 auto',
        display: 'flex',
        flexDirection: 'column',
        gap: 16,
      }}
    >
      {/* Skeleton pulse for the dashboard's loading states. */}
      <style>{`
        @keyframes dash-pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.45; } }
        .dash-skeleton { animation: dash-pulse 1.6s ease-in-out infinite; }
      `}</style>

      <header
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          gap: 12,
          flexWrap: 'wrap',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 12 }}>
          <h1 style={{ margin: 0, fontSize: 18, color: '#e8e8f0', fontWeight: 600 }}>
            <span style={{ color: '#7dd3fc' }}>SynthBrain</span> · Dashboard
          </h1>
          <a href="/" style={{ color: '#94a3b8', fontSize: 12, textDecoration: 'none' }}>
            3D graph →
          </a>
        </div>
        <div style={{ fontSize: 12, color: stats.error ? '#fb7185' : '#94a3b8' }}>
          {stats.error ? 'brain unavailable' : `Last updated ${formatClock(stats.lastUpdated)}`}
        </div>
      </header>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
          gap: 12,
        }}
      >
        {kpis.map((k) => (
          <div key={k.label} style={{ ...glass, padding: '12px 14px' }}>
            <div
              style={{
                fontSize: 11,
                color: '#94a3b8',
                textTransform: 'uppercase',
                letterSpacing: 0.5,
              }}
            >
              {k.label}
            </div>
            {stats.loading && runs.loading ? (
              <Skeleton height={24} width="60%" />
            ) : (
              <div style={{ fontSize: 22, color: '#e8e8f0', fontWeight: 600, marginTop: 2 }}>
                {k.value}
              </div>
            )}
          </div>
        ))}
      </div>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(min(440px, 100%), 1fr))',
          gap: 16,
          alignItems: 'start',
        }}
      >
        <IntakePanel
          runs={runs.data?.runs ?? null}
          loading={runs.loading}
          error={runs.error}
          bySource={breakdown?.by_source ?? null}
        />
        <ClassificationPanel
          breakdown={breakdown}
          breakdownError={stats.data?.breakdown_error}
          loading={stats.loading}
          error={stats.error}
        />
        <GraphPanel />
        <RecallPanel />
      </div>
    </main>
  );
}
