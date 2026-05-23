import type { Metadata, Viewport } from 'next';

import { SWRegister } from '../components/SWRegister';
import './globals.css';

export const metadata: Metadata = {
  title: 'SynthBrain',
  description: 'Your Mem.ai notes as a navigable 3D knowledge graph.',
  manifest: '/manifest.webmanifest',
  appleWebApp: {
    capable: true,
    statusBarStyle: 'black-translucent',
    title: 'SynthBrain',
  },
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  themeColor: '#0a0a14',
  viewportFit: 'cover',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        {children}
        <SWRegister />
      </body>
    </html>
  );
}
