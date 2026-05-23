import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: false,
    environment: 'node',
    include: ['**/src/**/*.{test,spec}.{ts,tsx}'],
    exclude: ['**/node_modules/**', '**/dist/**', '**/.next/**'],
    coverage: {
      reporter: ['text', 'html'],
      include: ['packages/*/src/**/*.ts', 'apps/connectors/*/src/**/*.ts'],
      exclude: ['**/*.test.ts', '**/__fixtures__/**'],
    },
  },
});
