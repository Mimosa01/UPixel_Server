from fastapi import APIRouter, Depends

from src.auth.base_config import fastapi_users
from src.auth.models import User

router = APIRouter(
    prefix="/colorings",
    tags=["Colorings"]
)

current_user = fastapi_users.current_user()


@router.get("")
async def get_all_colorings(user: User = Depends(current_user)):
    return {"answer": "Получитьвсе раскраски"}


@router.get("/{user_id}")
async def get_user_colorings(
        user_id: int,
        user: User = Depends(current_user)
):
    return {"answer": "Получить все раскраски пользователя"}


@router.get("/{coloring_id}")
async def get_coloring(
        coloring_id: int,
        user: User = Depends(current_user)
):
    return {"answer": "Получить общую раскраску и загрузить ее пользователю"}


@router.post("/coloring_id")
async def edit_user_coloring(
        coloring_id: int,
        user: User = Depends(current_user)
):
    return {"answer": "Изменить раскраску, которая есть у пользователя"}


@router.delete("/coloring_id")
async def delete_user_coloring(
        coloring_id: int,
        user: User = Depends(current_user)
):
    return {"answer": "Удалить раскраску из базы пользователя"}