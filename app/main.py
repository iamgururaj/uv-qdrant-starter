from app.embedding.local import LocalEmbeddingProvider
from app.vectordb.qdrant_store import QdrantStore


COLLECTION = "demo"


def main():
    embedder = LocalEmbeddingProvider()
    store = QdrantStore()

    texts = [
        "Python is a programming language",
        "Qdrant stores vectors",
        "Bengaluru is in India",
    ]

    vectors = embedder.embed(texts)

    dim = len(vectors[0])
    store.create_collection(COLLECTION, dim)

    store.upsert(
        COLLECTION,
        ids=list(range(len(texts))),
        vectors=vectors,
        payloads=[{"text": t} for t in texts],
    )

    q = "Where is Bengaluru?"
    qvec = embedder.embed([q])[0]

    results = store.search(COLLECTION, qvec)

    for r in results:
        print(f"score={r.score:.4f} id={r.id} text={r.payload['text']}")



if __name__ == "__main__":
    main()
