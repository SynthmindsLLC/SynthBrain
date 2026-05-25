import type { DriveFile } from './drive-client';

/**
 * Classification rules from docs/organization/google-drive-audit.md.
 * Maps a root-level file or folder to a destination folder path.
 * Returns null when no confident rule matches (left in place, flagged for review).
 */

export type Target = string[]; // folder path segments, e.g. ["Projects", "PBTV"]

const FOLDER_MIME = 'application/vnd.google-apps.folder';

/** Dormant desktop-app folders (auto-created by installers, untouched since 2022–23). */
const APP_CRUFT = new Set([
  'Adobe',
  'WhirlwindFX',
  'Syncios Data Recovery',
  'Syncios Mobile Manager',
  'WindowsPowerShell',
  'iZotope',
  'Custom Office Templates',
  'ATEM Autosave',
  'Zoom',
  'vMixStorage',
  'TASCAM Podcast Editor',
  'SOLIDWORKSComposer',
  'SOLIDWORKS Downloads',
  'Wolow Companion',
  'dr.fone restored file',
  'JoyToKey',
  'STAR WARS Squadrons Steam',
  'My Games',
  'Horizon Zero Dawn',
  'Topaz',
  'Picsio',
  'Outlook',
  'Outlook Files',
  'Box Import',
  'Box import',
  'SOLIDWORKS Downloads',
]);

const VIDEO_MIME = /^video\//;
const ARCHIVE_EXT = /\.(zip|rar)$/i;

/** Decide a destination for a root-level item. */
export function classifyToTarget(f: DriveFile): Target | null {
  const name = f.name;
  const lower = name.toLowerCase();

  if (f.mimeType === FOLDER_MIME) {
    if (APP_CRUFT.has(name)) return ['_Archive', '_AppData'];
    if (/^pbtv|plants by the village/i.test(name)) return ['Projects', 'PBTV'];
    if (/obsidian/i.test(name)) return ['Knowledge', 'Obsidian'];
    if (/excalidraw/i.test(name)) return ['Knowledge', 'excalidraw'];
    if (/fireflies|meet recordings|meeting/i.test(name)) return ['Knowledge', 'Meetings'];
    if (/statements|bank|invoices|taxes/i.test(name)) return ['Finance'];
    if (/pitches|brandprofiles/i.test(name)) return ['Clients', '_Proposals'];
    return null; // unknown folder — leave, flag for review
  }

  // Files
  if (/^pbtv|plants by the village|tara-lynn|lady cove/i.test(lower)) return ['Projects', 'PBTV'];
  if (/navsup|isoc|cno fighting|navy_platform|north div|day\d|accountability|jram/i.test(lower))
    return ['Clients', 'ISOC-Navy'];
  if (/prompt|metaprompt|scribe|feynman|recursive reprompt|prompting principles/i.test(lower))
    return ['Reference', 'Prompts'];
  if (/proposal|vecorsen|star support|district proposal|retainer|term_sheet|moa/i.test(lower))
    return ['Clients', '_Proposals'];
  if (/resume|cover letter|bio slide|brandeis/i.test(lower)) return ['Personal'];
  if (/statement|invoice|pricelist|wes_synthminds_llc|\btax\b/i.test(lower)) return ['Finance'];
  if (VIDEO_MIME.test(f.mimeType) || /recording|gmt\d/i.test(lower)) return ['Media', 'Recordings'];
  if (ARCHIVE_EXT.test(lower) || /onedrive_|export_session|files\.zip/i.test(lower))
    return ['Media', 'Recordings'];
  if (/brand book|fact sheet|service offering|logos|style guide|midjourney/i.test(lower))
    return ['Reference', 'BrandProfiles'];

  return null; // unmatched — leave in place
}

/** Suggested rename for naming-hygiene fixes (null = no change). */
export function suggestRename(f: DriveFile): string | null {
  // Trim Obsidian " 1" duplicate suffix on the title (extension preserved by Drive).
  const m = f.name.match(/^(.*) 1(\.[A-Za-z0-9]+)?$/);
  if (m) return `${m[1]}${m[2] ?? ''}`;
  return null;
}
