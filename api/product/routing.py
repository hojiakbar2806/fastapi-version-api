from fastapi import APIRouter, status

from api.product.schemas import ProductGet, ProductOutList
from api.product.v1.endpoint import *


router = APIRouter()


router.add_api_route(
    "/products",
    get_all,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    response_model=ProductOutList,
    description="Get "
)

router.add_api_route(
    "/products/{id}",
    get,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
    response_model=ProductGet,
    description="Get product by id"
)

router.add_api_route(
    "/products",
    create,
    methods=["POST"],
    status_code=status.HTTP_201_CREATED,
    response_model=ProductGet,
    description="Create product"
)

router.add_api_route(
    "/products/{id}",
    update,
    methods=["PUT"],
    status_code=status.HTTP_200_OK,
    response_model=ProductGet,
    description="Update product"
)

router.add_api_route(
    "/products/{id}",
    delete,
    methods=["DELETE"],
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete product",
)
