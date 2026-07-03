import type { Metadata } from 'next';

import { DashboardClient } from './DashboardClient';

export const metadata: Metadata = {
  title: 'SynthBrain — Dashboard',
  description: 'Ingest, classification, graph, and recall telemetry for the second brain.',
};

export default function DashboardPage() {
  return <DashboardClient />;
}
