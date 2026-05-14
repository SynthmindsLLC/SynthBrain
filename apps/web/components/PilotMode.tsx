'use client';

import { useCallback, useEffect, useState } from 'react';

type IOSDeviceOrientationEventCtor = typeof DeviceOrientationEvent & {
  requestPermission?: () => Promise<'granted' | 'denied'>;
};

export function PilotMode({
  enabled,
  onToggle,
}: {
  enabled: boolean;
  onToggle: (next: boolean) => void;
}) {
  const [needsPermission, setNeedsPermission] = useState(false);

  useEffect(() => {
    const ctor = (window.DeviceOrientationEvent as IOSDeviceOrientationEventCtor | undefined);
    if (ctor && typeof ctor.requestPermission === 'function') {
      setNeedsPermission(true);
    }
  }, []);

  const handleClick = useCallback(async () => {
    if (enabled) {
      onToggle(false);
      return;
    }
    const ctor = window.DeviceOrientationEvent as IOSDeviceOrientationEventCtor | undefined;
    if (ctor && typeof ctor.requestPermission === 'function') {
      try {
        const state = await ctor.requestPermission();
        if (state !== 'granted') {
          onToggle(false);
          return;
        }
      } catch {
        onToggle(false);
        return;
      }
    }
    onToggle(true);
  }, [enabled, onToggle]);

  return (
    <button
      type="button"
      onClick={handleClick}
      style={{
        position: 'fixed',
        bottom: 'calc(env(safe-area-inset-bottom) + 16px)',
        left: '50%',
        transform: 'translateX(-50%)',
        background: enabled ? '#22d3ee' : 'rgba(125,211,252,0.15)',
        color: enabled ? '#0a0a14' : '#7dd3fc',
        border: '1px solid #7dd3fc',
        borderRadius: 999,
        padding: '12px 24px',
        fontSize: 14,
        fontWeight: 600,
        letterSpacing: 0.5,
        backdropFilter: 'blur(8px)',
        WebkitBackdropFilter: 'blur(8px)',
        zIndex: 10,
      }}
      aria-pressed={enabled}
    >
      {enabled
        ? '⏸  Pilot mode on'
        : needsPermission
          ? '✈  Tap to enable pilot mode'
          : '✈  Enable pilot mode'}
    </button>
  );
}
