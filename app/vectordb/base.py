from abc import ABC, abstractmethod
from typing import List, Dict, Any


class VectorStore(ABC):

    @abstractmethod
    def create_collection(self, name: str, dim: int):
        pass

    @abstractmethod
    def upsert(
        self,
        collection: str,
        ids: List[int],
        vectors: List[List[float]],
        payloads: List[Dict[str, Any]],
    ):
        pass

    @abstractmethod
    def search(self, collection: str, vector: List[float], limit: int = 5):
        pass
