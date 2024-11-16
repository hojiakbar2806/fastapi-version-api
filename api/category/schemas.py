import datetime
from typing import List
from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryGet(CategoryBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


class CategoryOutList(BaseModel):
    products: List[CategoryGet]
