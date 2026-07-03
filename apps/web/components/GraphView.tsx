'use client';

import type { Graph } from '@synthbrain/graph-schema';
import { useMemo, useState } from 'react';

import { GraphCanvas } from './GraphCanvas';
import { HUD } from './HUD';
import { PilotMode } from './PilotMode';

export function GraphView({ initialGraph }: { initialGraph: Graph }) {
  const [pilotEnabled, setPilotEnabled] = useState(false);
  const [filter, setFilter] = useState<{
    source?: string | undefined;
    collection?: string | undefined;
    kind?: string | undefined;
  }>({});

  const filtered = useMemo(() => {
    if (!filter.source && !filter.collection && !filter.kind) return initialGraph;

    const keep = new Set<string>();
    for (const n of initialGraph.nodes) {
      if (filter.source && n.source === filter.source) keep.add(n.id);
      // Kind filtering covers brain entity graphs (person/event/place/org);
      // collection filtering only ever matches Mem-shaped graphs (c:* ids).
      if (filter.kind && n.kind === filter.kind) keep.add(n.id);
      if (filter.collection && n.id === `c:${filter.collection}`) keep.add(n.id);
    }
    if (filter.collection) {
      for (const l of initialGraph.links) {
        if (l.target === `c:${filter.collection}` && l.kind === 'in_collection') {
          keep.add(typeof l.source === 'string' ? l.source : (l.source as { id: string }).id);
        }
      }
    }
    const nodes = initialGraph.nodes.filter((n) => keep.has(n.id));
    const links = initialGraph.links.filter(
      (l) =>
        keep.has(typeof l.source === 'string' ? l.source : (l.source as { id: string }).id) &&
        keep.has(typeof l.target === 'string' ? l.target : (l.target as { id: string }).id),
    );
    return { ...initialGraph, nodes, links };
  }, [initialGraph, filter]);

  return (
    <>
      <GraphCanvas graph={filtered} pilotEnabled={pilotEnabled} />
      <HUD graph={initialGraph} filter={filter} onFilter={setFilter} pilotEnabled={pilotEnabled} />
      <PilotMode enabled={pilotEnabled} onToggle={setPilotEnabled} />
    </>
  );
}
