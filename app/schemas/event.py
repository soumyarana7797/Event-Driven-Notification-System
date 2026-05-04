import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EventBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class EventResponse(EventBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
