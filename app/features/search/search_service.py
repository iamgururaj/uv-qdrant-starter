from __future__ import annotations

from threading import Lock

from app.embedding.local import LocalEmbeddingProvider
from app.vectordb.qdrant_store import QdrantStore

from .search_schema import SearchRequest

COLLECTION = "docs"

embedder = LocalEmbeddingProvider()
store = QdrantStore()


class SearchNotFoundError(Exception):
    pass


class SearchService:
    def __init__(self) -> None:
        self._lock = Lock()

    def search(self, request: SearchRequest):
        vec = embedder.embed([request.query])[0]
        results = store.search(COLLECTION, vec, limit=request.limit)
        return [
            {
                "score": r.score,
                "text": r.payload.get("text"),
                "id": r.id,
            }
            for r in results
        ]
