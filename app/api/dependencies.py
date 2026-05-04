"""
FastAPI dependency providers.

All shared dependencies (DB session, settings, auth) are defined here
so routers stay slim and swappable.
"""

from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.infrastructure.database.session import get_db_session

# ── Typed aliases (use these in route signatures) ─────────────────────────────

DBSession = Annotated[AsyncSession, Depends(get_db_session)]
AppSettings = Annotated[Settings, Depends(get_settings)]
