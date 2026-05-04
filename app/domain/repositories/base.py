"""
Repository port (abstract interface) for the domain layer.

Concrete adapters live in app/infrastructure/database/repositories/.
Application services import from here — never from infrastructure.
"""

import uuid
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Generic, TypeVar

EntityT = TypeVar("EntityT")


class Repository(ABC, Generic[EntityT]):
    @abstractmethod
    async def get_by_id(self, entity_id: uuid.UUID) -> EntityT | None: ...

    @abstractmethod
    async def list(self, *, limit: int = 20, offset: int = 0) -> Sequence[EntityT]: ...

    @abstractmethod
    async def add(self, entity: EntityT) -> EntityT: ...

    @abstractmethod
    async def update(self, entity: EntityT) -> EntityT: ...

    @abstractmethod
    async def delete(self, entity_id: uuid.UUID) -> None: ...
