import { describe, expect, it } from 'vitest';

import { NORMALIZE_PACKAGE } from './index';

describe('normalize', () => {
  it('exposes its package name', () => {
    expect(NORMALIZE_PACKAGE).toBe('@synthbrain/normalize');
  });
});
