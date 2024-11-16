from fastapi import HTTPException
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError

from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Any

T = TypeVar('T')


class ApiResponse(BaseModel, Generic[T]):
    data: Optional[T] = None
    error: Optional[str] = None
    status: bool
    status_code: int


async def generate_response(data: Any = None, error: str = None, status: bool = True, status_code: int = 200) -> ApiResponse:
    return ApiResponse(data=data, error=error, status=status, status_code=status_code)


def handle_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException as e:
            return await generate_response(error=str(e.detail), status=False, status_code=e.status_code)
        except SQLAlchemyError as e:
            return await generate_response(error="Database error: " + str(e), status=False, status_code=500)
        except Exception as e:
            return await generate_response(error=str(e), status=False, status_code=500)
    return wrapper
