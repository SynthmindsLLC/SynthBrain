import { describe, expect, it } from 'vitest';

import { GRAPH_SCHEMA_PACKAGE } from './index';

describe('graph-schema', () => {
  it('exposes its package name', () => {
    expect(GRAPH_SCHEMA_PACKAGE).toBe('@synthbrain/graph-schema');
  });
});
