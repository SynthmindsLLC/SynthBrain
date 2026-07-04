const PALETTE: Record<string, string> = {
  mem: '#7dd3fc',
  fieldy: '#22d3ee',
  granola: '#facc15',
  calendar: '#f472b6',
  drive: '#34d399',
  gmail: '#fb923c',
  tag: '#a3a3a3',
  imessage: '#4ade80',
  'icloud-notes': '#fbbf24',
  github: '#cbd5e1',
  m365: '#60a5fa',
  slack: '#e879f9',
  claude: '#d97757',
  chatgpt: '#2dd4bf',
  'claude-code': '#fb7185',
  filesystem: '#a78bfa',
  inbox: '#5eead4',
  agentmail: '#fda4af',
  bookmarks: '#c4b5fd',
  reddit: '#ff8b60',
  instagram: '#f0abfc',
  zoom: '#93c5fd',
  'browser-history': '#fde047',
};

export function colorForSource(source: string): string {
  return PALETTE[source] ?? '#94a3b8';
}

/** Brain entity-kind colors (matches the /dashboard graph panel + HUD chips). */
export const KIND_COLORS: Record<string, string> = {
  person: '#22d3ee', // cyan — people
  event: '#a855f7', // violet — events
  place: '#f59e0b', // amber — places
  org: '#34d399', // emerald — orgs
};

export function colorForKind(kind: string): string | undefined {
  return KIND_COLORS[kind];
}
