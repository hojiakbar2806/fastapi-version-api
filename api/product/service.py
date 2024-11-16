from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy.future import select

from api.product.schemas import ProductCreate, ProductUpdate


class ProductCRUD:
    def __init__(self, model):
        self.model = model

    async def get(self, db: AsyncSession, id: int):
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalars().first()

    async def get_all(self, db: AsyncSession):
        result = await db.execute(select(self.model))
        return result.scalars().all()

    async def create(self, db: AsyncSession, obj_in: ProductCreate):
        obj_data = obj_in.dict()
        db_obj = self.model(**obj_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, id: int, obj_in: ProductUpdate):
        db_obj = await self.get(db, id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Product not found")
        update_data = obj_in.dict(exclude_unset=True)
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, id: int):
        db_obj = await self.get(db, id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Product not found")
        await db.delete(db_obj)
        await db.commit()
        return db_obj
