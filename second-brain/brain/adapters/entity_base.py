"""Entity adapters emit Entity and Edge objects (not text chunks).

Same swappable spirit as the chunk adapters, different output type: Contacts and
Calendar describe *who/what/when*, which lands in the graph store, not the vector
index. The pipeline routes a mixed stream.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from ..core.entities import Edge, Entity, EntityStore


class EntityAdapter(ABC):
    name: str

    @abstractmethod
    def fetch(self) -> Iterable[Entity | Edge]:
        """Yield Entity and/or Edge objects from this source."""
        raise NotImplementedError


def ingest_entities(store: EntityStore, adapter: EntityAdapter) -> dict[str, int]:
    ents = edges = 0
    # Two passes so edges can reference entities regardless of stream order.
    deferred_edges: list[Edge] = []
    for item in adapter.fetch():
        if isinstance(item, Entity):
            store.upsert_entity(item)
            ents += 1
        else:
            deferred_edges.append(item)
    for edge in deferred_edges:
        store.add_edge(edge)
        edges += 1
    return {"entities": ents, "edges": edges}
