from sqlalchemy import Integer, String, TEXT, DECIMAL
from sqlalchemy.orm import mapped_column, Mapped

from database.base import Base


class Category(Base):

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
