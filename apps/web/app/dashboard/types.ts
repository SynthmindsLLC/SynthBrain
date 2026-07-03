// Client-safe response shapes for the dashboard's /api/* proxies.
// Type-only imports from brain-http are erased at compile time, so the
// 'server-only' guard inside it never reaches the client bundle.
import type {
  BrainCard,
  BrainIngestRun,
  BrainQueryResult,
  BrainStats,
  BrainStatsBreakdown,
} from '../../lib/brain-http';

/** GET /api/stats — merged /stats + /stats/breakdown. */
export interface StatsResponse {
  stats: BrainStats;
  /** null when the running brain predates GET /stats/breakdown. */
  breakdown: BrainStatsBreakdown | null;
  generated_at: string;
}

/** GET /api/runs */
export interface RunsResponse {
  runs: BrainIngestRun[];
}

/** POST /api/query */
export interface QueryResponse {
  text: string;
  results: BrainQueryResult[];
}

export type { BrainCard, BrainIngestRun, BrainQueryResult, BrainStats, BrainStatsBreakdown };
