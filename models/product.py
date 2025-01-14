from sqlalchemy import Integer, String, TEXT, DECIMAL
from sqlalchemy.orm import mapped_column, Mapped

from database.base import Base
from models.mixin import CreatedUpdatedMixin


class Product(Base, CreatedUpdatedMixin):
    """
    Product Table
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=0)

# You can add more models here following the same pattern
