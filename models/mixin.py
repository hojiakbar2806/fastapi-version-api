from datetime import datetime
from sqlalchemy import  DateTime
from sqlalchemy.orm import Mapped, mapped_column


class CreatedUpdatedMixin:
    """Ummumiy created_at va updated_at ustunlarini o'z ichiga oluvchi mixin klass."""

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


