'use client';

import type { Graph } from '@synthbrain/graph-schema';
import { useEffect, useRef, useState } from 'react';

type SourcedGraph = Graph & { graph_source?: 'brain' | 'mem' | 'seed' };

import { GraphCanvas } from '../../components/GraphCanvas';
import { KIND_COLORS } from '../../lib/source-colors';

import { Panel, Skeleton, StateNote } from './ui';

const GRAPH_HEIGHT = 380;

export function GraphPanel() {
  const [graph, setGraph] = useState<SourcedGraph | null>(null);
  const [error, setError] = useState<string | null>(null);
  const wrapRef = useRef<HTMLDivElement | null>(null);
  const [width, setWidth] = useState(0);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch('/api/graph', { cache: 'no-store' });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const g = (await res.json()) as SourcedGraph;
        if (!cancelled) setGraph(g);
      } catch (err) {
        if (!cancelled) setError(err instanceof Error ? err.message : 'fetch failed');
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    const el = wrapRef.current;
    if (!el) return;
    const observer = new ResizeObserver((entries) => {
      const entry = entries[0];
      if (entry) setWidth(Math.floor(entry.contentRect.width));
    });
    observer.observe(el);
    return () => observer.disconnect();
  }, []);

  return (
    <Panel title="Graph" subtitle="entity graph">
      <div
        style={{ display: 'flex', gap: 10, flexWrap: 'wrap', alignItems: 'center', fontSize: 12 }}
      >
        {Object.entries(KIND_COLORS).map(([kind, color]) => (
          <span
            key={kind}
            style={{ display: 'inline-flex', alignItems: 'center', gap: 5, color: '#94a3b8' }}
          >
            <span
              style={{
                width: 8,
                height: 8,
                borderRadius: '50%',
                background: color,
                display: 'inline-block',
              }}
            />
            {kind}
          </span>
        ))}
        <a
          href="/"
          style={{ marginLeft: 'auto', color: '#7dd3fc', textDecoration: 'none', fontSize: 12 }}
        >
          Open full graph →
        </a>
      </div>

      {/* Gesture capture is scoped to this container (D10) so the page keeps scrolling. */}
      <div
        ref={wrapRef}
        style={{
          height: GRAPH_HEIGHT,
          borderRadius: 10,
          overflow: 'hidden',
          touchAction: 'none',
          overscrollBehavior: 'contain',
          border: '1px solid rgba(125,211,252,0.15)',
          background: '#0a0a14',
        }}
      >
        {error ? (
          <div style={{ padding: 16 }}>
            <StateNote tone="error">brain unavailable</StateNote>
          </div>
        ) : !graph || width === 0 ? (
          <div style={{ padding: 16 }}>
            <Skeleton height={GRAPH_HEIGHT - 32} />
          </div>
        ) : graph.graph_source && graph.graph_source !== 'brain' ? (
          // Never pass mem/seed data off as the entity graph — say what it is.
          <div style={{ padding: 16 }}>
            <StateNote tone="empty">
              {graph.graph_source === 'seed'
                ? 'showing bundled demo data — brain not connected (set BRAIN_URL / USE_BRAIN=1)'
                : 'showing Mem.ai notes graph — brain not connected'}
            </StateNote>
          </div>
        ) : graph.nodes.length === 0 ? (
          <div style={{ padding: 16 }}>
            <StateNote tone="empty">brain empty — run an ingest</StateNote>
          </div>
        ) : (
          <GraphCanvas graph={graph} pilotEnabled={false} width={width} height={GRAPH_HEIGHT} />
        )}
      </div>
    </Panel>
  );
}
