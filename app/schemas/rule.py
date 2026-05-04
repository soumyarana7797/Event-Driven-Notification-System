import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RuleBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class RuleCreate(RuleBase):
    pass


class RuleUpdate(RuleBase):
    pass


class RuleResponse(RuleBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
