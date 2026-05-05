import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class EventBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class EventCreate(EventBase):
    event_type: str = Field(..., max_length=255, examples=["user.signed_up"])
    payload: dict[str, Any] = Field(default_factory=dict)


class EventResponse(EventBase):
    id: uuid.UUID
    event_type: str
    payload: dict[str, Any]
    created_at: datetime
    updated_at: datetime
