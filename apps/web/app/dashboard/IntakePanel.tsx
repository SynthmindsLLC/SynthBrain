'use client';

import { basename, formatDuration, formatRelative } from '../../lib/format';
import { colorForSource } from '../../lib/source-colors';

import type { BrainIngestRun } from './types';
import { Chip, HBar, Panel, SkeletonRows, StateNote, errorLabel } from './ui';

const STATUS_COLORS: Record<string, string> = {
  ok: '#34d399',
  success: '#34d399',
  completed: '#34d399',
  running: '#f59e0b',
  partial: '#f59e0b',
  error: '#fb7185',
  failed: '#fb7185',
};

export function IntakePanel({
  runs,
  loading,
  error,
  bySource,
}: {
  runs: BrainIngestRun[] | null;
  loading: boolean;
  error: string | null;
  /** breakdown.by_source; null when /stats/breakdown is unavailable. */
  bySource: Record<string, number> | null;
}) {
  const sources = bySource
    ? Object.entries(bySource)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10)
    : [];
  const maxSource = sources.reduce((m, [, v]) => Math.max(m, v), 0);

  return (
    <Panel title="Intake" subtitle="ingest runs">
      {loading ? (
        <SkeletonRows rows={5} />
      ) : error ? (
        <StateNote tone="error">{errorLabel(error)}</StateNote>
      ) : !runs || runs.length === 0 ? (
        <StateNote tone="empty">brain empty — run an ingest</StateNote>
      ) : (
        <div style={{ overflowX: 'auto' }}>
          <table style={{ borderCollapse: 'collapse', width: '100%', fontSize: 12, minWidth: 560 }}>
            <thead>
              <tr style={{ color: '#94a3b8', textAlign: 'left' }}>
                {[
                  'Adapter',
                  'Source',
                  'Status',
                  'Docs',
                  'Chunks',
                  'Err',
                  'Skip',
                  'Duration',
                  'When',
                ].map((h) => (
                  <th key={h} style={{ padding: '4px 8px', fontWeight: 500, whiteSpace: 'nowrap' }}>
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {runs.map((r) => (
                <tr key={r.run_id} style={{ borderTop: '1px solid rgba(125,211,252,0.1)' }}>
                  <td style={{ padding: '5px 8px', color: '#7dd3fc', whiteSpace: 'nowrap' }}>
                    {r.adapter}
                  </td>
                  <td
                    style={{
                      padding: '5px 8px',
                      color: '#e8e8f0',
                      maxWidth: 160,
                      overflow: 'hidden',
                      textOverflow: 'ellipsis',
                      whiteSpace: 'nowrap',
                    }}
                    title={r.source}
                  >
                    {basename(r.source)}
                  </td>
                  <td style={{ padding: '5px 8px' }}>
                    <Chip label={r.status} color={STATUS_COLORS[r.status] ?? '#94a3b8'} />
                  </td>
                  <td style={{ padding: '5px 8px', color: '#e8e8f0' }}>{r.docs}</td>
                  <td style={{ padding: '5px 8px', color: '#e8e8f0' }}>{r.chunks}</td>
                  <td style={{ padding: '5px 8px', color: r.errors > 0 ? '#fb7185' : '#94a3b8' }}>
                    {r.errors}
                  </td>
                  <td style={{ padding: '5px 8px', color: '#94a3b8' }}>{r.skipped}</td>
                  <td style={{ padding: '5px 8px', color: '#94a3b8', whiteSpace: 'nowrap' }}>
                    {formatDuration(r.started_at, r.finished_at)}
                  </td>
                  <td style={{ padding: '5px 8px', color: '#94a3b8', whiteSpace: 'nowrap' }}>
                    {formatRelative(r.started_at)}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {sources.length > 0 && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          <div style={{ fontSize: 12, color: '#94a3b8' }}>Chunks by source</div>
          {sources.map(([source, count]) => (
            <HBar
              key={source}
              label={source}
              value={count}
              max={maxSource}
              color={colorForSource(source)}
            />
          ))}
        </div>
      )}
    </Panel>
  );
}
