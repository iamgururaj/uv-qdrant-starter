from abc import ABC, abstractmethod
from typing import Any


class VectorStore(ABC):
    @abstractmethod
    def create_collection(self, name: str, dim: int):
        pass

    @abstractmethod
    def upsert(
        self,
        collection: str,
        ids: list[int],
        vectors: list[list[float]],
        payloads: list[dict[str, Any]],
    ):
        pass

    @abstractmethod
    def search(self, collection: str, vector: list[float], limit: int = 5):
        pass
