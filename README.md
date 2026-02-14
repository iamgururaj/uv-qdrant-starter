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

## Common commands

| Task | Command |
| --- | --- |
| Run script | `uv run python main.py` |
| Dev server | `uv run fastapi dev` |
| Prod server | `uv run fastapi run` |
| Lint | `uv run ruff check .` |
| Lint (fix) | `uv run ruff check . --fix` |
| Format | `uv run ruff format .` |
