// 15-second beat windowing. The G2 reference doc pins ~15s as the cadence
// that balances HUD freshness vs noise; one heuristic-pre-filter + at most
// one brain call per beat keeps cost predictable.

import type { STTSegment } from './types.js';

export interface Beat {
  startTs: number;
  endTs: number;
  segments: STTSegment[];
}

export interface BeatStream {
  push(seg: STTSegment): Beat | null;
  flush(): Beat | null;
}

export function makeBeatStream(windowSeconds = 15): BeatStream {
  let current: STTSegment[] = [];
  let windowStart: number | null = null;

  const close = (endTs: number): Beat | null => {
    if (current.length === 0 || windowStart === null) return null;
    const beat: Beat = { startTs: windowStart, endTs, segments: current };
    current = [];
    windowStart = null;
    return beat;
  };

  return {
    push(seg: STTSegment): Beat | null {
      if (windowStart === null) windowStart = seg.ts;
      current.push(seg);
      if (seg.ts - windowStart >= windowSeconds) {
        return close(seg.ts);
      }
      return null;
    },
    flush(): Beat | null {
      const lastTs = current[current.length - 1]?.ts ?? windowStart ?? 0;
      return close(lastTs);
    },
  };
}
