"""
Contains SQLAlchemy Session Instance
"""
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from core.config import settings
from database.base import Base


engine = create_async_engine(settings.sqlalchemy_url, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_async_session():
    async with async_session() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
