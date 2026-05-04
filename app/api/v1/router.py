from fastapi import APIRouter

from app.api.v1.routes import events, rules

api_router = APIRouter()

api_router.include_router(events.router)
api_router.include_router(rules.router)


@api_router.get("/health", tags=["health"], summary="Liveness probe")
async def health() -> dict[str, str]:
    return {"status": "ok"}
