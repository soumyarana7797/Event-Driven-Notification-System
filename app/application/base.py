"""
Application-layer base classes.

Use cases (a.k.a. interactors) extend BaseUseCase and receive their
repository port via constructor injection — never the ORM session directly.
"""

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

RequestT = TypeVar("RequestT")
ResponseT = TypeVar("ResponseT")


class BaseUseCase(ABC, Generic[RequestT, ResponseT]):
    """
    Template for a single-responsibility use case.

    Usage:
        class CreateUser(BaseUseCase[CreateUserRequest, UserResponse]):
            def __init__(self, repo: UserRepository) -> None:
                self._repo = repo

            async def execute(self, request: CreateUserRequest) -> UserResponse:
                ...
    """

    @abstractmethod
    async def execute(self, request: RequestT) -> ResponseT: ...
