'use client';

import type { Graph } from '@synthbrain/graph-schema';
import dynamic from 'next/dynamic';

const GraphCanvasInner = dynamic(() => import('./GraphCanvasInner'), {
  ssr: false,
  loading: () => (
    <div style={{ padding: 24, color: '#7dd3fc', fontSize: 13 }}>Loading 3D engine…</div>
  ),
});

export function GraphCanvas(props: { graph: Graph; pilotEnabled: boolean }) {
  return <GraphCanvasInner {...props} />;
}
