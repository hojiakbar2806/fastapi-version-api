from api.crud_base import CRUDBase
from models.category import Category
from api.category.schemas import CategoryCreate, CategoryUpdate


class CategoryService(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    pass


category_service = CategoryService(Category)
