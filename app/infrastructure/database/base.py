import uuid
from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn, declared_attr, mapped_column


class Base(DeclarativeBase):
    """
    Declarative base shared by all ORM models.

    Subclasses automatically get:
    - __tablename__  derived from the class name (snake_case'd)
    - id             UUID primary key
    - created_at / updated_at  server-side timestamps
    """

    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:
        # Convert CamelCase → snake_case  (e.g. UserProfile → user_profile)
        name = cls.__name__
        return "".join(
            f"_{c.lower()}" if c.isupper() and i else c.lower()
            for i, c in enumerate(name)
        )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"
