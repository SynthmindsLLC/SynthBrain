'use client';

import type { ReactNode } from 'react';

import { colorForSource } from '../../lib/source-colors';

import type { BrainStatsBreakdown } from './types';
import { HBar, LAYER_COLORS, Panel, SkeletonRows, StateNote, errorLabel } from './ui';

const LAYERS = ['artifact', 'decision', 'reasoning', 'workaround'] as const;

export function ClassificationPanel({
  breakdown,
  breakdownError,
  loading,
  error,
}: {
  breakdown: BrainStatsBreakdown | null;
  /** Transient (non-404) breakdown failure — distinct from "brain outdated". */
  breakdownError?: string | undefined;
  loading: boolean;
  error: string | null;
}) {
  let body: ReactNode;
  if (loading) {
    body = <SkeletonRows rows={6} />;
  } else if (error) {
    body = <StateNote tone="error">{errorLabel(error)}</StateNote>;
  } else if (!breakdown && breakdownError) {
    body = <StateNote tone="error">breakdown temporarily unavailable — retrying</StateNote>;
  } else if (!breakdown) {
    body = <StateNote tone="error">brain outdated — /stats/breakdown unavailable</StateNote>;
  } else if (breakdown.chunks_total === 0) {
    body = <StateNote tone="empty">brain empty — run an ingest</StateNote>;
  } else {
    const layerMax = LAYERS.reduce((m, l) => Math.max(m, breakdown.by_layer[l] ?? 0), 0);
    const projects = Object.entries(breakdown.by_project)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10);
    const projectMax = projects.reduce((m, [, v]) => Math.max(m, v), 0);
    const days = breakdown.by_day.slice(-30);

    body = (
      <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          <div style={{ fontSize: 12, color: '#94a3b8' }}>Context-graph layers</div>
          {LAYERS.map((layer) => (
            <HBar
              key={layer}
              label={layer}
              value={breakdown.by_layer[layer] ?? 0}
              max={layerMax}
              color={LAYER_COLORS[layer] ?? '#94a3b8'}
            />
          ))}
        </div>

        {projects.length > 0 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            <div style={{ fontSize: 12, color: '#94a3b8' }}>Top projects</div>
            {projects.map(([project, count]) => (
              <HBar key={project} label={project} value={count} max={projectMax} color="#22d3ee" />
            ))}
          </div>
        )}

        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
          <div style={{ fontSize: 12, color: '#94a3b8' }}>Chunks per day (last 30d)</div>
          <Sparkline days={days} />
        </div>

        <SourceDonut bySource={breakdown.by_source} />
      </div>
    );
  }

  return (
    <Panel title="Classification" subtitle="layers · projects · volume">
      {body}
    </Panel>
  );
}

function Sparkline({ days }: { days: Array<{ date: string; chunks: number }> }) {
  if (days.length === 0) {
    return <StateNote tone="empty">no ingest activity yet</StateNote>;
  }
  const w = 300;
  const h = 56;
  const pad = 4;
  const max = days.reduce((m, d) => Math.max(m, d.chunks), 1);
  const stepX = days.length > 1 ? (w - pad * 2) / (days.length - 1) : 0;
  const pts = days.map(
    (d, i) => [pad + i * stepX, h - pad - (d.chunks / max) * (h - pad * 2)] as const,
  );
  const line = pts.map((p) => `${p[0].toFixed(1)},${p[1].toFixed(1)}`).join(' ');
  const lastX = pad + (days.length - 1) * stepX;
  const area = `${pad},${h - pad} ${line} ${lastX.toFixed(1)},${h - pad}`;
  const last = pts[pts.length - 1];
  return (
    <svg
      viewBox={`0 0 ${w} ${h}`}
      preserveAspectRatio="none"
      style={{ width: '100%', height: h, display: 'block' }}
      role="img"
      aria-label="Chunks ingested per day"
    >
      <polygon points={area} fill="rgba(125,211,252,0.12)" />
      <polyline points={line} fill="none" stroke="#7dd3fc" strokeWidth={1.5} />
      {last && <circle cx={last[0]} cy={last[1]} r={2.5} fill="#22d3ee" />}
    </svg>
  );
}

function SourceDonut({ bySource }: { bySource: Record<string, number> }) {
  const entries = Object.entries(bySource).sort((a, b) => b[1] - a[1]);
  if (entries.length === 0) return null;
  const top = entries.slice(0, 7);
  const restTotal = entries.slice(7).reduce((sum, [, v]) => sum + v, 0);
  const segments = restTotal > 0 ? [...top, ['other', restTotal] as [string, number]] : top;
  const total = segments.reduce((sum, [, v]) => sum + v, 0);
  const r = 40;
  const c = 2 * Math.PI * r;
  let cumulative = 0;

  return (
    <div style={{ display: 'flex', gap: 16, alignItems: 'center', flexWrap: 'wrap' }}>
      <svg viewBox="0 0 100 100" width={110} height={110} role="img" aria-label="Chunks by source">
        {segments.map(([name, value]) => {
          const dash = (value / total) * c;
          const offset = cumulative;
          cumulative += dash;
          return (
            <circle
              key={name}
              cx={50}
              cy={50}
              r={r}
              fill="none"
              stroke={name === 'other' ? '#94a3b8' : colorForSource(name)}
              strokeWidth={12}
              strokeDasharray={`${dash} ${c - dash}`}
              strokeDashoffset={-offset}
              transform="rotate(-90 50 50)"
            />
          );
        })}
      </svg>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 4, fontSize: 12 }}>
        {segments.map(([name, value]) => (
          <div key={name} style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <span
              style={{
                width: 8,
                height: 8,
                borderRadius: 2,
                background: name === 'other' ? '#94a3b8' : colorForSource(name),
                display: 'inline-block',
              }}
            />
            <span style={{ color: '#e8e8f0' }}>{name}</span>
            <span style={{ color: '#94a3b8' }}>{value.toLocaleString('en-US')}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
