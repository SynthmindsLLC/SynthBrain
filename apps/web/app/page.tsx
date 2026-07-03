import { Suspense } from 'react';

import { GraphView } from '../components/GraphView';
import { getGraphData } from '../lib/mem-source';

export const dynamic = 'force-dynamic';
export const revalidate = 60;

export default async function Home() {
  const graph = await getGraphData();
  return (
    <main className="graph-viewport">
      <Suspense fallback={<div style={{ padding: 16 }}>Loading graph…</div>}>
        <GraphView initialGraph={graph} />
      </Suspense>
    </main>
  );
}
