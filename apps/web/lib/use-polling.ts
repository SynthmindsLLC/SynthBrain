'use client';

import { useCallback, useEffect, useRef, useState } from 'react';

export interface PollState<T> {
  data: T | null;
  /** Error code/message from the last failed fetch; cleared on success. */
  error: string | null;
  /** True until the first fetch settles. */
  loading: boolean;
  /** Wall-clock time of the last successful fetch. */
  lastUpdated: Date | null;
  refresh: () => void;
}

/**
 * Poll a JSON endpoint on an interval (D9). Plain setInterval + fetch — no
 * SWR/react-query. Pauses while the tab is hidden and fires immediately on
 * return to visibility.
 */
export function usePolling<T>(url: string, intervalMs = 5000): PollState<T> {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [lastUpdated, setLastUpdated] = useState<Date | null>(null);
  const inFlight = useRef(false);

  const tick = useCallback(async () => {
    if (typeof document !== 'undefined' && document.hidden) return;
    if (inFlight.current) return;
    inFlight.current = true;
    try {
      const res = await fetch(url, { cache: 'no-store' });
      if (!res.ok) {
        let message = `HTTP ${res.status}`;
        try {
          const j = (await res.json()) as { error?: string; message?: string };
          message = j.error ?? message;
        } catch {
          // non-JSON error body; keep the status message
        }
        setError(message);
      } else {
        setData((await res.json()) as T);
        setError(null);
        setLastUpdated(new Date());
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'fetch failed');
    } finally {
      inFlight.current = false;
      setLoading(false);
    }
  }, [url]);

  useEffect(() => {
    void tick();
    const id = setInterval(() => void tick(), intervalMs);
    const onVisibility = () => {
      if (!document.hidden) void tick();
    };
    document.addEventListener('visibilitychange', onVisibility);
    return () => {
      clearInterval(id);
      document.removeEventListener('visibilitychange', onVisibility);
    };
  }, [tick, intervalMs]);

  const refresh = useCallback(() => {
    void tick();
  }, [tick]);

  return { data, error, loading, lastUpdated, refresh };
}
