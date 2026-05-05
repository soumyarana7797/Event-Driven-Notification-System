import uuid
from datetime import datetime, timezone
from typing import Any

from app.domain.models.event import Event
from app.domain.repositories.event_repository import EventRepository


class EventService:
    """
    Orchestrates event ingestion.

    Receives raw primitives from the API layer — no Pydantic or HTTP imports here.
    Delegates persistence entirely to the repository port.
    """

    def __init__(self, repository: EventRepository) -> None:
        self._repository = repository

    async def create_event(self, event_type: str, payload: dict[str, Any]) -> Event:
        now = datetime.now(timezone.utc)
        event = Event(
            id=uuid.uuid4(),
            event_type=event_type,
            payload=payload,
            # Placeholder timestamps; the real server-side values come back
            # after repository.add() flushes and refreshes from the DB.
            created_at=now,
            updated_at=now,
        )
        return await self._repository.add(event)
