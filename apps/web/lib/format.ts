/** Small display formatters shared by the dashboard panels. */

export function formatNumber(n: number | null | undefined): string {
  if (n === null || n === undefined || !Number.isFinite(n)) return '—';
  return n.toLocaleString('en-US');
}

/** "just now" / "4m ago" / "3h ago" / "2d ago" from an ISO timestamp. */
export function formatRelative(iso: string | null | undefined): string {
  if (!iso) return '—';
  const t = Date.parse(iso);
  if (Number.isNaN(t)) return '—';
  const deltaMs = Date.now() - t;
  if (deltaMs < 0) return 'just now';
  const s = Math.floor(deltaMs / 1000);
  if (s < 60) return 'just now';
  const m = Math.floor(s / 60);
  if (m < 60) return `${m}m ago`;
  const h = Math.floor(m / 60);
  if (h < 24) return `${h}h ago`;
  const d = Math.floor(h / 24);
  return `${d}d ago`;
}

/** "4.2s" / "1m 12s" between two ISO timestamps; "—" when unfinished. */
export function formatDuration(
  startIso: string | null | undefined,
  endIso: string | null | undefined,
): string {
  if (!startIso || !endIso) return '—';
  const start = Date.parse(startIso);
  const end = Date.parse(endIso);
  if (Number.isNaN(start) || Number.isNaN(end) || end < start) return '—';
  const seconds = (end - start) / 1000;
  if (seconds < 60) return `${seconds.toFixed(1)}s`;
  const m = Math.floor(seconds / 60);
  const s = Math.round(seconds % 60);
  return `${m}m ${s}s`;
}

/** "14:03:22" local wall clock. */
export function formatClock(date: Date | null | undefined): string {
  if (!date) return '—';
  return date.toLocaleTimeString('en-US', { hour12: false });
}

/** Trailing path segment: "/Users/wes/Downloads/x.md" -> "x.md". */
export function basename(path: string): string {
  const trimmed = path.replace(/\/+$/, '');
  const seg = trimmed.split('/').pop();
  return seg || trimmed || path;
}
