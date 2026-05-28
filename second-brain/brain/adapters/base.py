"""The adapter contract. Every source — Drive, M365, Granola, Claude, ChatGPT,
Fieldy, the hard drive, the G2 mic — implements exactly this.

This mirrors the SynthOS adapter pattern: behavior in the core, identity in the
adapter. The core pipeline only knows `name` and `fetch()`.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from ..core.pipeline import RawDoc


class Adapter(ABC):
    name: str

    @abstractmethod
    def fetch(self) -> Iterable[RawDoc]:
        """Yield RawDocs from this source. Pull-based; the pipeline drives it."""
        raise NotImplementedError
