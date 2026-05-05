"""
FastAPI dependency providers.

All shared dependencies (DB session, settings, service factories) are defined
here so routers stay slim and the wiring is swappable for tests.
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.services.event_service import EventService
from app.core.config import Settings, get_settings
from app.infrastructure.database.repositories.event_repository import SQLAlchemyEventRepository
from app.infrastructure.database.session import get_db_session

# ── Primitive dependencies ────────────────────────────────────────────────────

DBSession = Annotated[AsyncSession, Depends(get_db_session)]
AppSettings = Annotated[Settings, Depends(get_settings)]

# ── Service factories ─────────────────────────────────────────────────────────


def get_event_service(db: DBSession) -> EventService:
    return EventService(SQLAlchemyEventRepository(db))


EventServiceDep = Annotated[EventService, Depends(get_event_service)]
