from fastapi import Depends
from models.product import Product
from models.product import Product
from api.product.service import ProductCRUD
from sqlalchemy.ext.asyncio import AsyncSession
from database.async_session import get_async_session
from api.product.schemas import ProductCreate, ProductUpdate


product_crud = ProductCRUD(Product)


async def get_all(db: AsyncSession = Depends(get_async_session)):
    prodcut_db = await product_crud.get_all(db)
    return {"products": prodcut_db}


async def get(id: int, db: AsyncSession = Depends(get_async_session)):
    return await product_crud.get(db, id)


async def create(obj_in: ProductCreate, db: AsyncSession = Depends(get_async_session)):
    return await product_crud.create(db, obj_in)


async def update(id: int, obj_in: ProductUpdate, db: AsyncSession = Depends(get_async_session)):
    return await product_crud.update(db, id, obj_in)


async def delete(id: int, db: AsyncSession = Depends(get_async_session)):
    return await product_crud.delete(db, id)
