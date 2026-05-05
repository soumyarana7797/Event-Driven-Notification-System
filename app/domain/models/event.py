import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class Event:
    """Immutable domain entity representing a single ingested event."""

    id: uuid.UUID
    event_type: str
    payload: dict[str, Any]
    created_at: datetime
    updated_at: datetime
