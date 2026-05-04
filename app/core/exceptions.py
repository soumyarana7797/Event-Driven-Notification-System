"""
Domain-neutral exception hierarchy.

Raise these from the domain/application layers; the API layer maps them
to HTTP responses via exception handlers registered in main.py.
"""

from typing import Any


class AppError(Exception):
    """Base for all application-level errors."""

    def __init__(self, message: str, code: str = "APP_ERROR") -> None:
        super().__init__(message)
        self.message = message
        self.code = code


class NotFoundError(AppError):
    def __init__(self, resource: str, identifier: Any = None) -> None:
        detail = (
            f"{resource} not found"
            if identifier is None
            else f"{resource} '{identifier}' not found"
        )
        super().__init__(detail, code="NOT_FOUND")


class ConflictError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="CONFLICT")


class ValidationError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="VALIDATION_ERROR")


class UnauthorizedError(AppError):
    def __init__(self, message: str = "Authentication required") -> None:
        super().__init__(message, code="UNAUTHORIZED")


class ForbiddenError(AppError):
    def __init__(self, message: str = "Insufficient permissions") -> None:
        super().__init__(message, code="FORBIDDEN")
