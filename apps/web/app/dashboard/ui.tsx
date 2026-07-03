'use client';

import type { CSSProperties, ReactNode } from 'react';

/** Shared glassmorphism shell used by every dashboard surface. */
export const glass: CSSProperties = {
  background: 'rgba(10,10,20,0.6)',
  backdropFilter: 'blur(10px)',
  WebkitBackdropFilter: 'blur(10px)',
  border: '1px solid rgba(125,211,252,0.2)',
  borderRadius: 12,
};

export const LAYER_COLORS: Record<string, string> = {
  artifact: '#7dd3fc',
  decision: '#34d399',
  reasoning: '#a855f7',
  workaround: '#f59e0b',
};

export function Panel({
  title,
  subtitle,
  children,
}: {
  title: string;
  subtitle?: string;
  children: ReactNode;
}) {
  return (
    <section
      style={{
        ...glass,
        padding: 16,
        display: 'flex',
        flexDirection: 'column',
        gap: 12,
        minWidth: 0,
      }}
    >
      <header style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
        <h2
          style={{
            margin: 0,
            fontSize: 14,
            fontWeight: 600,
            color: '#7dd3fc',
            letterSpacing: 0.5,
            textTransform: 'uppercase',
          }}
        >
          {title}
        </h2>
        {subtitle && <span style={{ fontSize: 12, color: '#94a3b8' }}>{subtitle}</span>}
      </header>
      {children}
    </section>
  );
}

export function Skeleton({
  height = 16,
  width = '100%',
}: {
  height?: number;
  width?: number | string;
}) {
  return (
    <div
      className="dash-skeleton"
      style={{ height, width, borderRadius: 8, background: 'rgba(125,211,252,0.08)' }}
    />
  );
}

export function SkeletonRows({ rows = 4 }: { rows?: number }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
      {Array.from({ length: rows }, (_, i) => (
        <Skeleton key={i} height={14} width={`${100 - i * 12}%`} />
      ))}
    </div>
  );
}

export function StateNote({ tone, children }: { tone: 'empty' | 'error'; children: ReactNode }) {
  const color = tone === 'error' ? '#fda4af' : '#94a3b8';
  const border = tone === 'error' ? 'rgba(251,113,133,0.3)' : 'rgba(148,163,184,0.25)';
  return (
    <div
      style={{
        border: `1px dashed ${border}`,
        borderRadius: 10,
        padding: '14px 12px',
        fontSize: 13,
        color,
        textAlign: 'center',
      }}
    >
      {children}
    </div>
  );
}

/** Human copy for a failed /api/* poll. */
export function errorLabel(error: string): string {
  if (error === 'brain_outdated')
    return 'brain outdated — restart the brain API to enable this panel';
  return 'brain unavailable';
}

export function Chip({ label, color }: { label: string; color: string }) {
  return (
    <span
      style={{
        border: `1px solid ${color}`,
        color,
        borderRadius: 999,
        padding: '1px 8px',
        fontSize: 11,
        whiteSpace: 'nowrap',
      }}
    >
      {label}
    </span>
  );
}

export function HBar({
  label,
  value,
  max,
  color,
}: {
  label: string;
  value: number;
  max: number;
  color: string;
}) {
  const pct = max > 0 ? Math.max((value / max) * 100, value > 0 ? 2 : 0) : 0;
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12 }}>
        <span
          style={{
            color: '#e8e8f0',
            overflow: 'hidden',
            textOverflow: 'ellipsis',
            whiteSpace: 'nowrap',
          }}
        >
          {label}
        </span>
        <span style={{ color: '#94a3b8', marginLeft: 8 }}>{value.toLocaleString('en-US')}</span>
      </div>
      <div style={{ height: 6, borderRadius: 999, background: 'rgba(125,211,252,0.08)' }}>
        <div style={{ height: 6, borderRadius: 999, width: `${pct}%`, background: color }} />
      </div>
    </div>
  );
}
