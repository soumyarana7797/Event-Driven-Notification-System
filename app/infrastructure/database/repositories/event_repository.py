import uuid
from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.event import Event
from app.domain.repositories.event_repository import EventRepository
from app.infrastructure.database.models.event import EventModel


class SQLAlchemyEventRepository(EventRepository):
    """Concrete adapter — translates between domain Event and EventModel."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, entity_id: uuid.UUID) -> Event | None:
        model = await self._session.get(EventModel, entity_id)
        return self._to_entity(model) if model else None

    async def list(self, *, limit: int = 20, offset: int = 0) -> Sequence[Event]:
        stmt = select(EventModel).order_by(EventModel.created_at.desc()).limit(limit).offset(offset)
        result = await self._session.execute(stmt)
        return [self._to_entity(m) for m in result.scalars().all()]

    async def add(self, entity: Event) -> Event:
        model = EventModel(
            id=entity.id,
            event_type=entity.event_type,
            payload=entity.payload,
        )
        self._session.add(model)
        await self._session.flush()
        await self._session.refresh(model)
        return self._to_entity(model)

    async def update(self, entity: Event) -> Event:
        # Events are immutable once written.
        raise NotImplementedError("Events cannot be updated after creation")

    async def delete(self, entity_id: uuid.UUID) -> None:
        model = await self._session.get(EventModel, entity_id)
        if model:
            await self._session.delete(model)

    def _to_entity(self, model: EventModel) -> Event:
        return Event(
            id=model.id,
            event_type=model.event_type,
            payload=model.payload,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
