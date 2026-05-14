const PALETTE: Record<string, string> = {
  mem: '#7dd3fc',
  fieldy: '#22d3ee',
  granola: '#facc15',
  calendar: '#f472b6',
  drive: '#34d399',
  gmail: '#fb923c',
  tag: '#a3a3a3',
};

export function colorForSource(source: string): string {
  return PALETTE[source] ?? '#94a3b8';
}
