from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_config import fastapi_users
from src.auth.models import User
from src.database import get_async_session
from src.schemas.schemas import SPictures


router = APIRouter(
    prefix="/pictures",
    tags=["Pictures"]
)

current_user = fastapi_users.current_user()


@router.get("/{user_id}/all")
async def get_all_user_pictures(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    return {"answer": "Получить все картинки пользователя"}


@router.get("/{pictures_id}")
async def get_picture(
        pictures_id: int,
        user: User = Depends(current_user)
):
    return {"answer": "Получитьодну картинку"}


@router.post("/{picture_id}")
async def add_picture(
        data: SPictures,
        picture_id: int,
        user: User = Depends(current_user)
):
    return {"answer": "Добавить картинку"}


@router.delete("/{picture_id}")
async def delete_picture(
        picture_id: int,
        user: User = Depends(current_user)
):
    return {"answer": "Удалить картинку"}
