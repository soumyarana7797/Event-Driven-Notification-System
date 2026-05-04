from fastapi import APIRouter

from app.api.dependencies import DBSession

router = APIRouter(prefix="/events", tags=["events"])


# Endpoints will be added here once domain models and use cases are defined.
# Example:
#   @router.get("/", response_model=list[EventResponse])
#   async def list_events(db: DBSession) -> list[EventResponse]:
#       ...
