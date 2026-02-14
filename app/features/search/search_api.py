from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends

from app.features.search.search_schema import SearchRequest

from .search_service import SearchService

router = APIRouter(prefix="/qdrant", tags=["qdrant"])

_service = SearchService()


def get_search_service() -> SearchService:
    return _service


@router.post("/search")
async def search(
    req: SearchRequest,
    service: Annotated[SearchService, Depends(get_search_service)],
):
    return service.search(req)
