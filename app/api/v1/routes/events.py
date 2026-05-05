from fastapi import APIRouter

from app.api.dependencies import EventServiceDep
from app.schemas.event import EventCreate, EventResponse

router = APIRouter(prefix="/events", tags=["events"])


@router.post("/", response_model=EventResponse, status_code=201, summary="Ingest a new event")
async def create_event(data: EventCreate, service: EventServiceDep) -> EventResponse:
    event = await service.create_event(
        event_type=data.event_type,
        payload=data.payload,
    )
    return EventResponse.model_validate(event)
