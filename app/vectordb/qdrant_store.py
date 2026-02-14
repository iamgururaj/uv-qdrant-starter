from typing import Any

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from .base import VectorStore


class QdrantStore(VectorStore):
    def __init__(self, host: str = "localhost", port: int = 6333):
        self.client = QdrantClient(host=host, port=port)

    def create_collection(self, name: str, dim: int):
        self.client.recreate_collection(
            collection_name=name,
            vectors_config=VectorParams(
                size=dim,
                distance=Distance.COSINE,
            ),
        )

    def ensure_collection(self, name: str, dim: int):
        collections = self.client.get_collections().collections
        exists = any(c.name == name for c in collections)

        if not exists:
            self.client.create_collection(
                collection_name=name,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
            )

    def upsert(
        self,
        collection: str,
        ids: list[int],
        vectors: list[list[float]],
        payloads: list[dict[str, Any]],
    ):
        points = [
            PointStruct(
                id=ids[i],
                vector=vectors[i],
                payload=payloads[i],
            )
            for i in range(len(ids))
        ]

        self.client.upsert(collection_name=collection, points=points)

    def search(self, collection: str, vector: list[float], limit: int = 5):
        response = self.client.query_points(
            collection_name=collection,
            query=vector,
            limit=limit,
        )
        return response.points
