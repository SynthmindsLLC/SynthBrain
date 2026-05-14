import { describe, expect, it } from 'vitest';

import { MEM_CLIENT_PACKAGE } from './index';

describe('mem-client', () => {
  it('exposes its package name', () => {
    expect(MEM_CLIENT_PACKAGE).toBe('@synthbrain/mem-client');
  });
});
