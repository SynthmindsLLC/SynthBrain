// Contracts the plugin satisfies. Independent of the Hub SDK so the loop is
// testable without it.

export interface STTSegment {
  speaker?: string;
  text: string;
  ts: number; // seconds since session start
}

export interface SalientCue {
  /** Person mention extracted by the salience layer (best guess). */
  mention: string;
  /** Optional event hint extracted alongside the mention. */
  event?: string;
  /** The surrounding text window the brain uses for disambiguation. */
  context: string;
  /** 0-1; below threshold, do NOT call the brain. */
  salience: number;
}

export interface RenderedCard {
  /** Bullet lines, already truncated to the HUD budget. */
  bullets: string[];
  /** Header line (e.g. "Jeff Torres - Acme VP"). */
  header: string;
  /** Where met line, if known. */
  subhead?: string;
  /** Brain confidence; below threshold, surface AMBIGUOUS prompt instead. */
  confidence: number;
  needsDisambiguation?: string[];
}

export const HUD_MAX_BULLETS = 5;
export const HUD_MAX_WORDS_PER_BULLET = 8;
