# uv-qdrant-starter
uv init --app .

docker run -d --name qdrant-local \
  -p 6333:6333 \
  -v $(pwd)/qdrant_data:/qdrant/storage \
  qdrant/qdrant

  http://localhost:6333

touch .env
touch .env.template

uv add qdrant-client
uv add sentence-transformers

