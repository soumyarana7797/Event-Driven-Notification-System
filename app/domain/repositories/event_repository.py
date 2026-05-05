from app.domain.models.event import Event
from app.domain.repositories.base import Repository


class EventRepository(Repository[Event]):
    """
    Port (abstract interface) for event persistence.

    The infrastructure layer provides the concrete adapter.
    Application services depend only on this interface.
    """
