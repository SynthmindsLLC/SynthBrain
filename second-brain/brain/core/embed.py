"""Embedders are swappable. The spine never imports a specific model directly.

Three implementations:
  - openai:  text-embedding-3-small (1536-d). Cloud. Needs OPENAI_API_KEY.
  - local:   sentence-transformers (bge-small / nomic). On-device, private.
  - fake:    deterministic hashing embedder. Zero deps, offline, for tests/demo.

For the glasses' strict-private mode you'll run `local`. For convenience you can
run `openai`. The smoke test runs `fake` so the plumbing is provable without
downloading a model or spending a cent.
"""

from __future__ import annotations

import hashlib
import math
import os
from typing import Protocol


class Embedder(Protocol):
    dim: int
    def embed(self, texts: list[str]) -> list[list[float]]: ...


class FakeEmbedder:
    """Deterministic bag-of-hashed-tokens vector. Not semantic-grade, but stable
    and good enough that overlapping text retrieves overlapping text in a demo."""

    def __init__(self, dim: int = 64) -> None:
        self.dim = dim

    def embed(self, texts: list[str]) -> list[list[float]]:
        out: list[list[float]] = []
        for t in texts:
            vec = [0.0] * self.dim
            for tok in t.lower().split():
                h = int(hashlib.md5(tok.encode()).hexdigest(), 16)
                vec[h % self.dim] += 1.0
            norm = math.sqrt(sum(v * v for v in vec)) or 1.0
            out.append([v / norm for v in vec])
        return out


class OpenAIEmbedder:
    def __init__(self, model: str = "text-embedding-3-small") -> None:
        from openai import OpenAI  # lazy import; optional dependency

        key = os.environ.get("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("OPENAI_API_KEY not set; required for the openai embedder")
        self._client = OpenAI(api_key=key)
        self.model = model
        self.dim = 1536

    def embed(self, texts: list[str]) -> list[list[float]]:
        resp = self._client.embeddings.create(model=self.model, input=texts)
        return [d.embedding for d in resp.data]


class LocalEmbedder:
    def __init__(self, model: str = "BAAI/bge-small-en-v1.5") -> None:
        from sentence_transformers import SentenceTransformer  # lazy; optional

        self._model = SentenceTransformer(model)
        self.dim = self._model.get_sentence_embedding_dimension()

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [v.tolist() for v in self._model.encode(texts, normalize_embeddings=True)]


def get_embedder(name: str = "fake") -> Embedder:
    name = name.lower()
    if name == "fake":
        return FakeEmbedder()
    if name == "openai":
        return OpenAIEmbedder()
    if name == "local":
        return LocalEmbedder()
    raise ValueError(f"unknown embedder {name!r}; use fake|openai|local")
