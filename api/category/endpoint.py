from fastapi import APIRouter
from models.category import Category
from api.category.services import category_service

router = APIRouter(tags=["Categories"])


@router.get("/categories", response_model=Category)
async def get_all():
    return await category_service.get_all()
