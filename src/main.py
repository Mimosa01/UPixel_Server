from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_config import fastapi_users, auth_backend
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreate
from src.database import get_async_session
from src.schemas import SPictures


app = FastAPI(
    title="UPixel"
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"
  

@app.get("/")
async def index():
    return {"result": True}


@app.get("/user")
async def get_user():
    return {"answer": "Инофрмация о юзере"}


@app.get("/pictures/{user_id}")
async def get_all_user_pictures(user_id: int, session: AsyncSession = Depends(get_async_session)):
    return {"answer": "Получить все картинки пользователя"}


@app.get("/pictures/{pictures_id}")
async def get_picture(picture_id: int):
    return {"answer": "Получить картинку пользователя"}


@app.post("/pictures/{picture_id}")
async def add_picture(data: SPictures, picture_id: int):
    return {"answer": "Добавить картинку"}


@app.delete("pictures/{picture_id}")
async def delete_picture(picture_id: int):
    return {"answer": "Удалить картинку"}


@app.get("/colorings")
async def get_all_colorings():
    return {"answer": "Получитьвсе раскраски"}


@app.get("/colorings/{user_id}")
async def get_user_colorings(user_id: int):
    return {"answer": "Получить все раскраски пользователя"}


@app.get("/colorings/{coloring_id}")
async def get_coloring(coloring_id: int):
    # По идеи этот поинт должен получить раскраску, которой еще нет у пользователя и он должен сохранить ему ее
    # Конечно если у него такой раскраски нет
    return {"answer": "Получить раскраску пользователя"}


@app.post("/colorings/coloring_id")
async def edit_user_coloring(coloring_id: int):
    return {"answer": "Изменить раскраску, которая есть у пользователя"}


@app.delete("/colorings/coloring_id")
async def delete_user_coloring(coloring_id: int):
    return {"answer": "Удалить раскраску из базы пользователя"}
