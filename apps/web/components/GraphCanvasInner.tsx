'use client';

import type { Graph } from '@synthbrain/graph-schema';
import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import ForceGraph3D from 'react-force-graph-3d';
import SpriteText from 'three-spritetext';

import { usePilotCamera } from '../lib/use-pilot-camera';

type ForceGraphRef = {
  cameraPosition: (
    pos: { x?: number; y?: number; z?: number },
    lookAt?: { x: number; y: number; z: number } | null,
    ms?: number,
  ) => void;
  camera: () => { position: { x: number; y: number; z: number } };
};

export default function GraphCanvasInner({
  graph,
  pilotEnabled,
}: {
  graph: Graph;
  pilotEnabled: boolean;
}) {
  const fgRef = useRef<ForceGraphRef | null>(null);
  const [size, setSize] = useState<[number, number]>([
    typeof window !== 'undefined' ? window.innerWidth : 1024,
    typeof window !== 'undefined' ? window.innerHeight : 768,
  ]);

  useEffect(() => {
    const update = () => setSize([window.innerWidth, window.innerHeight]);
    update();
    window.addEventListener('resize', update);
    window.addEventListener('orientationchange', update);
    return () => {
      window.removeEventListener('resize', update);
      window.removeEventListener('orientationchange', update);
    };
  }, []);

  const data = useMemo(() => ({ nodes: graph.nodes, links: graph.links }), [graph]);

  const nodeThreeObject = useCallback((node: unknown) => {
    const n = node as { label: string; color?: string; size: number; kind: string };
    const sprite = new SpriteText(n.label);
    sprite.color = n.color ?? '#e8e8f0';
    sprite.textHeight = n.kind === 'collection' ? 6 : 3;
    sprite.fontWeight = n.kind === 'collection' ? '600' : '400';
    sprite.backgroundColor = 'rgba(10,10,20,0.5)';
    sprite.padding = 2;
    return sprite as unknown as object;
  }, []);

  const handleNodeClick = useCallback((node: unknown) => {
    const n = node as { x?: number; y?: number; z?: number };
    if (!fgRef.current || n.x === undefined || n.y === undefined || n.z === undefined) return;
    const distance = 80;
    const distRatio = 1 + distance / Math.hypot(n.x, n.y, n.z || 1);
    fgRef.current.cameraPosition(
      { x: n.x * distRatio, y: n.y * distRatio, z: n.z * distRatio },
      { x: n.x, y: n.y, z: n.z },
      900,
    );
  }, []);

  usePilotCamera(fgRef, pilotEnabled);

  return (
    <ForceGraph3D
      ref={fgRef as unknown as never}
      graphData={data}
      width={size[0]}
      height={size[1]}
      backgroundColor="#0a0a14"
      nodeId="id"
      nodeLabel="label"
      nodeColor="color"
      nodeRelSize={4}
      nodeThreeObject={nodeThreeObject}
      nodeThreeObjectExtend={false}
      linkColor={() => 'rgba(140,160,200,0.25)'}
      linkWidth={0.4}
      linkDirectionalParticles={0}
      enableNodeDrag={false}
      onNodeClick={handleNodeClick}
      cooldownTime={4000}
      warmupTicks={60}
      controlType="orbit"
    />
  );
}
