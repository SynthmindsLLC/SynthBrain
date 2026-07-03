'use client';

import type { Graph } from '@synthbrain/graph-schema';
import { useMemo, useState } from 'react';

import { colorForKind, colorForSource } from '../lib/source-colors';

type Filter = {
  source?: string | undefined;
  collection?: string | undefined;
  kind?: string | undefined;
};

export function HUD({
  graph,
  filter,
  onFilter,
  pilotEnabled,
}: {
  graph: Graph;
  filter: Filter;
  onFilter: (f: Filter) => void;
  pilotEnabled: boolean;
}) {
  const [open, setOpen] = useState(false);

  const sources = useMemo(() => {
    const counts = new Map<string, number>();
    for (const n of graph.nodes) {
      if (n.kind !== 'note') continue;
      counts.set(n.source, (counts.get(n.source) ?? 0) + 1);
    }
    return Array.from(counts.entries()).sort((a, b) => b[1] - a[1]);
  }, [graph]);

  const collections = useMemo(() => graph.nodes.filter((n) => n.kind === 'collection'), [graph]);

  // Brain entity graphs carry person/event/place/org kinds instead of
  // note/collection/tag; offer kind chips when any are present.
  const entityKinds = useMemo(() => {
    const counts = new Map<string, number>();
    for (const n of graph.nodes) {
      if (n.kind === 'note' || n.kind === 'collection' || n.kind === 'tag') continue;
      counts.set(n.kind, (counts.get(n.kind) ?? 0) + 1);
    }
    return Array.from(counts.entries()).sort((a, b) => b[1] - a[1]);
  }, [graph]);

  const isBrainGraph = entityKinds.length > 0;

  return (
    <div
      style={{
        position: 'fixed',
        top: 'calc(env(safe-area-inset-top) + 12px)',
        left: 12,
        right: 12,
        zIndex: 10,
        display: 'flex',
        flexDirection: 'column',
        gap: 8,
        pointerEvents: 'none',
      }}
    >
      <div
        style={{
          display: 'flex',
          gap: 8,
          alignItems: 'center',
          justifyContent: 'space-between',
          pointerEvents: 'auto',
        }}
      >
        <div
          style={{
            background: 'rgba(10,10,20,0.6)',
            backdropFilter: 'blur(8px)',
            WebkitBackdropFilter: 'blur(8px)',
            border: '1px solid rgba(125,211,252,0.2)',
            borderRadius: 12,
            padding: '6px 12px',
            fontSize: 12,
            color: '#94a3b8',
          }}
        >
          <strong style={{ color: '#7dd3fc' }}>SynthBrain</strong>
          {isBrainGraph ? (
            <>
              {' '}
              · {graph.nodes.length} entities · {graph.links.length} links
            </>
          ) : (
            <>
              {' '}
              · {graph.note_count} notes · {graph.collection_count} collections
            </>
          )}
          {pilotEnabled && <span style={{ color: '#22d3ee' }}> · pilot</span>}
        </div>
        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          style={{
            background: 'rgba(10,10,20,0.6)',
            backdropFilter: 'blur(8px)',
            WebkitBackdropFilter: 'blur(8px)',
            border: '1px solid rgba(125,211,252,0.2)',
            borderRadius: 12,
            padding: '6px 10px',
            color: '#7dd3fc',
            fontSize: 12,
            cursor: 'pointer',
          }}
          aria-expanded={open}
        >
          {open ? 'Close' : 'Filter'}
        </button>
      </div>

      {open && (
        <div
          style={{
            background: 'rgba(10,10,20,0.7)',
            backdropFilter: 'blur(12px)',
            WebkitBackdropFilter: 'blur(12px)',
            border: '1px solid rgba(125,211,252,0.2)',
            borderRadius: 12,
            padding: 12,
            pointerEvents: 'auto',
            maxHeight: '60vh',
            overflowY: 'auto',
            fontSize: 13,
          }}
        >
          {entityKinds.length > 0 && (
            <div style={{ marginBottom: 12 }}>
              <div style={{ color: '#7dd3fc', marginBottom: 6, fontWeight: 600 }}>By kind</div>
              <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                <FilterChip
                  label="All"
                  active={!filter.kind}
                  onClick={() => onFilter({ ...filter, kind: undefined })}
                />
                {entityKinds.map(([kind, count]) => (
                  <FilterChip
                    key={kind}
                    label={`${kind} (${count})`}
                    color={colorForKind(kind) ?? '#7dd3fc'}
                    active={filter.kind === kind}
                    onClick={() => onFilter({ ...filter, kind })}
                  />
                ))}
              </div>
            </div>
          )}

          {sources.length > 0 && (
            <div style={{ marginBottom: 12 }}>
              <div style={{ color: '#7dd3fc', marginBottom: 6, fontWeight: 600 }}>By source</div>
              <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                <FilterChip
                  label="All"
                  active={!filter.source}
                  onClick={() => onFilter({ ...filter, source: undefined })}
                />
                {sources.map(([source, count]) => (
                  <FilterChip
                    key={source}
                    label={`${source} (${count})`}
                    color={colorForSource(source)}
                    active={filter.source === source}
                    onClick={() => onFilter({ ...filter, source })}
                  />
                ))}
              </div>
            </div>
          )}

          {collections.length > 0 && (
            <div>
              <div style={{ color: '#7dd3fc', marginBottom: 6, fontWeight: 600 }}>
                By collection
              </div>
              <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                <FilterChip
                  label="All"
                  active={!filter.collection}
                  onClick={() => onFilter({ ...filter, collection: undefined })}
                />
                {collections.map((c) => {
                  const cid = c.id.replace(/^c:/, '');
                  return (
                    <FilterChip
                      key={c.id}
                      label={c.label}
                      active={filter.collection === cid}
                      onClick={() => onFilter({ ...filter, collection: cid })}
                    />
                  );
                })}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function FilterChip({
  label,
  active,
  color,
  onClick,
}: {
  label: string;
  active: boolean;
  color?: string;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      style={{
        background: active ? (color ?? '#7dd3fc') : 'transparent',
        color: active ? '#0a0a14' : (color ?? '#e8e8f0'),
        border: `1px solid ${color ?? '#7dd3fc'}`,
        borderRadius: 999,
        padding: '4px 10px',
        fontSize: 12,
        cursor: 'pointer',
      }}
    >
      {label}
    </button>
  );
}
