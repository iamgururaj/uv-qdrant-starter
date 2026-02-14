from app.embedding.local import LocalEmbeddingProvider
from app.helper.hash_utils import make_id
from app.vectordb.qdrant_store import QdrantStore

from .chunker import chunk_text
from .loader import load_text

COLLECTION = "docs"


def ingest_file(path: str):
    embedder = LocalEmbeddingProvider()
    store = QdrantStore()

    text = load_text(path)
    chunks = chunk_text(text)

    vectors = embedder.embed(chunks)
    dim = len(vectors[0])

    store.ensure_collection(COLLECTION, dim)

    ids = [make_id(c) for c in chunks]
    payloads = [{"text": c, "source": path} for c in chunks]

    store.upsert(COLLECTION, ids, vectors, payloads)

    print(f"Inserted {len(chunks)} chunks")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m app.ingest.pipeline <file>")
        sys.exit(1)

    ingest_file(sys.argv[1])
