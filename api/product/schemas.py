import datetime
from typing import List
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(min_length=2, max_length=50,
                      title="Product name", example="Apple")
    description: str = Field(min_length=8, max_length=200,title="Product description", example="Red Apple")
    price: float = Field(gt=0, title="Product price", example=100)
    quantity: int = Field(gt=0, title="Product quantity", example=10)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductGet(ProductBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


class ProductOutList(BaseModel):
    products: List[ProductGet]
