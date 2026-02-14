from app.embedding.local import LocalEmbeddingProvider
from app.vectordb.qdrant_store import QdrantStore

COLLECTION = "docs"
MIN_SCORE = 0.50


def run_console():
    embedder = LocalEmbeddingProvider()
    store = QdrantStore()

    while True:
        q = input("\nAsk something (or 'exit'): ")

        if q.lower() == "exit":
            break

        vec = embedder.embed([q])[0]
        results = store.search(COLLECTION, vec, limit=1)

        for r in results:
            if r.score < MIN_SCORE:
                continue
            print(f"\nscore={r.score:.3f}")
            print(r.payload["text"])


if __name__ == "__main__":
    run_console()
