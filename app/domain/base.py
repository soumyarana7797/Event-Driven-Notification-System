"""
Domain-layer base entity.

Pure Python — zero infrastructure or framework dependencies.
Repository interfaces (ports) live in app/domain/repositories/base.py.
"""

import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Entity:
    """Immutable base for all domain entities."""

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
