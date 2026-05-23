'use client';

import { useEffect, type MutableRefObject } from 'react';

type ForceGraphRef = {
  cameraPosition: (
    pos: { x?: number; y?: number; z?: number },
    lookAt?: { x: number; y: number; z: number } | null,
    ms?: number,
  ) => void;
  camera: () => { position: { x: number; y: number; z: number } };
};

const RADIUS = 300;

// Drives the ForceGraph3D camera from DeviceOrientation events.
// Phone tilt → camera position on a sphere of radius RADIUS, always looking at origin.
export function usePilotCamera(
  fgRef: MutableRefObject<ForceGraphRef | null>,
  enabled: boolean,
): void {
  useEffect(() => {
    if (!enabled) return;
    const handler = (event: DeviceOrientationEvent) => {
      const fg = fgRef.current;
      if (!fg) return;
      // Pull current camera position to preserve radius if we want to.
      // alpha: 0..360 (compass), beta: -180..180 (front/back tilt), gamma: -90..90 (side tilt)
      const beta = (event.beta ?? 0) * (Math.PI / 180);
      const gamma = (event.gamma ?? 0) * (Math.PI / 180);
      const alpha = (event.alpha ?? 0) * (Math.PI / 180);

      // Spherical coords driven by tilt; clamp beta so we don't flip past the pole.
      const phi = Math.max(0.1, Math.min(Math.PI - 0.1, Math.PI / 2 + beta));
      const theta = alpha + gamma;

      const x = RADIUS * Math.sin(phi) * Math.cos(theta);
      const z = RADIUS * Math.sin(phi) * Math.sin(theta);
      const y = RADIUS * Math.cos(phi);

      fg.cameraPosition({ x, y, z }, { x: 0, y: 0, z: 0 }, 80);
    };
    window.addEventListener('deviceorientation', handler);
    return () => window.removeEventListener('deviceorientation', handler);
  }, [enabled, fgRef]);
}
