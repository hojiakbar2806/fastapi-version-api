from fastapi import FastAPI
from api.product import router
from database.async_session import create_tables
from api.category.endpoint import router as category_router


app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    await create_tables()
    print("Tables created successfully.")


app.include_router(router)
app.include_router(category_router)
