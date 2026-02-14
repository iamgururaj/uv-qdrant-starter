from fastapi import FastAPI

from app.features.search.search_api import router as SearchRouter

app = FastAPI()

app.include_router(SearchRouter)


@app.get("/")
def read_root():
    return {"status": "success", "app": "uv-qdrant-starter", "tool": "uv", "framework": "FastAPI"}
