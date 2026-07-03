'use client';

import { useCallback, useState } from 'react';

import { colorForSource } from '../../lib/source-colors';

import type { BrainCard, BrainQueryResult, QueryResponse } from './types';
import { Chip, LAYER_COLORS, Panel, SkeletonRows, StateNote, glass } from './ui';

interface DossierState {
  mention: string;
  loading: boolean;
  card: BrainCard | null;
  error: string | null;
}

/** "person:jeff-torres" -> "jeff torres"; raw names pass through unchanged. */
function mentionFromTag(tag: string): string {
  const match = /^(?:person|event|place|org):(.+)$/.exec(tag);
  if (match && match[1]) return match[1].replace(/-/g, ' ');
  return tag;
}

export function RecallPanel() {
  const [text, setText] = useState('');
  const [results, setResults] = useState<BrainQueryResult[] | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [dossier, setDossier] = useState<DossierState | null>(null);

  const runQuery = useCallback(async () => {
    const q = text.trim();
    if (!q || loading) return;
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('/api/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: q, k: 8 }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const json = (await res.json()) as QueryResponse;
      setResults(json.results);
    } catch {
      setError('brain unavailable');
    } finally {
      setLoading(false);
    }
  }, [text, loading]);

  const openDossier = useCallback(async (tag: string) => {
    const mention = mentionFromTag(tag);
    setDossier({ mention, loading: true, card: null, error: null });
    try {
      const res = await fetch('/api/dossier', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mention }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const card = (await res.json()) as BrainCard;
      setDossier({ mention, loading: false, card, error: null });
    } catch {
      setDossier({ mention, loading: false, card: null, error: 'brain unavailable' });
    }
  }, []);

  return (
    <Panel title="Recall" subtitle="query the brain">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          void runQuery();
        }}
        style={{ display: 'flex', gap: 8 }}
      >
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Ask the brain… e.g. why did we pick the enclosure?"
          style={{
            flex: 1,
            minWidth: 0,
            background: 'rgba(10,10,20,0.7)',
            border: '1px solid rgba(125,211,252,0.2)',
            borderRadius: 10,
            padding: '8px 12px',
            fontSize: 13,
            color: '#e8e8f0',
            outline: 'none',
          }}
        />
        <button
          type="submit"
          disabled={loading || !text.trim()}
          style={{
            background: loading || !text.trim() ? 'rgba(125,211,252,0.15)' : '#22d3ee',
            color: loading || !text.trim() ? '#7dd3fc' : '#0a0a14',
            border: '1px solid rgba(125,211,252,0.4)',
            borderRadius: 10,
            padding: '8px 16px',
            fontSize: 13,
            fontWeight: 600,
          }}
        >
          {loading ? '…' : 'Recall'}
        </button>
      </form>

      {loading ? (
        <SkeletonRows rows={4} />
      ) : error ? (
        <StateNote tone="error">{error}</StateNote>
      ) : results === null ? (
        <div style={{ fontSize: 12, color: '#94a3b8' }}>
          Results appear here. Click a person tag on a result to open their dossier.
        </div>
      ) : results.length === 0 ? (
        <StateNote tone="empty">no matches — brain empty? run an ingest</StateNote>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          {results.map((r, i) => (
            <div
              key={`${r.source_id}-${i}`}
              style={{
                border: '1px solid rgba(125,211,252,0.12)',
                borderRadius: 10,
                padding: 10,
                display: 'flex',
                flexDirection: 'column',
                gap: 6,
              }}
            >
              <div style={{ fontSize: 13, color: '#e8e8f0', lineHeight: 1.45 }}>
                {r.text.length > 280 ? `${r.text.slice(0, 280)}…` : r.text}
              </div>
              <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap', alignItems: 'center' }}>
                <Chip label={r.source} color={colorForSource(r.source)} />
                <Chip label={r.layer} color={LAYER_COLORS[r.layer] ?? '#94a3b8'} />
                {r.score !== null && (
                  <span style={{ fontSize: 11, color: '#94a3b8' }}>score {r.score.toFixed(3)}</span>
                )}
                {r.entity_tags.map((tag) => (
                  <button
                    key={tag}
                    type="button"
                    onClick={() => void openDossier(tag)}
                    title="Open dossier"
                    style={{
                      background: 'transparent',
                      border: '1px dashed rgba(34,211,238,0.5)',
                      color: '#22d3ee',
                      borderRadius: 999,
                      padding: '1px 8px',
                      fontSize: 11,
                    }}
                  >
                    {tag}
                  </button>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}

      {dossier && (
        <div style={{ ...glass, border: '1px solid rgba(34,211,238,0.35)', padding: 14 }}>
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'baseline',
              marginBottom: 8,
            }}
          >
            <strong style={{ color: '#22d3ee', fontSize: 14 }}>
              {dossier.card?.name || dossier.mention}
            </strong>
            <button
              type="button"
              onClick={() => setDossier(null)}
              style={{
                background: 'transparent',
                border: 'none',
                color: '#94a3b8',
                fontSize: 13,
              }}
            >
              ✕ close
            </button>
          </div>
          {dossier.loading ? (
            <SkeletonRows rows={3} />
          ) : dossier.error ? (
            <StateNote tone="error">{dossier.error}</StateNote>
          ) : dossier.card ? (
            <div
              style={{
                fontSize: 13,
                color: '#e8e8f0',
                display: 'flex',
                flexDirection: 'column',
                gap: 6,
              }}
            >
              {dossier.card.role && (
                <div>
                  <span style={{ color: '#94a3b8' }}>Role:</span> {dossier.card.role}
                </div>
              )}
              {dossier.card.relationship && (
                <div>
                  <span style={{ color: '#94a3b8' }}>Relationship:</span>{' '}
                  {dossier.card.relationship}
                </div>
              )}
              {dossier.card.where_met && (
                <div>
                  <span style={{ color: '#94a3b8' }}>Where met:</span> {dossier.card.where_met}
                </div>
              )}
              {dossier.card.discussed.length > 0 && (
                <div>
                  <div style={{ color: '#94a3b8', marginBottom: 4 }}>Discussed:</div>
                  <ul style={{ margin: 0, paddingLeft: 18 }}>
                    {dossier.card.discussed.map((d, i) => (
                      <li key={i} style={{ marginBottom: 2 }}>
                        {d}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
              <div style={{ color: '#94a3b8', fontSize: 12 }}>
                confidence {(dossier.card.confidence * 100).toFixed(0)}%
              </div>
            </div>
          ) : null}
        </div>
      )}
    </Panel>
  );
}
