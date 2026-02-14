# uv-qdrant-starter

Small template to learn embeddings, vector storage, and semantic search locally.

---

## Dependencies

* Python
* uv
* sentence-transformers
* Qdrant (Docker)

---

## Init project

```
uv init --app .
```

---

## Start Qdrant

```
docker run -d --name qdrant-local -p 6333:6333 \
  -v $(pwd)/qdrant_data:/qdrant/storage \
  qdrant/qdrant
```

Open:

```
http://localhost:6333
```

---

## Run

```
uv run python -m app.main
```

---

## Direct commands

Ingest:

```
uv run python -m app.ingest.pipeline sample.txt
```

Console:

```
uv run python -m app.cli.console
```
