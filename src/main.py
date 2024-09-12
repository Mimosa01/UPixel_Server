from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.schemas import SPictures

from src.models import pictures


app = FastAPI(
    title="UPixel"
)
  

@app.get("/")
async def index():
    return {"result": True}


@app.get("/user")
async def get_user():
    return {"answer": "Инофрмация о юзере"}


@app.get("/pictures/{user_id}")
async def get_all_user_pictures(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(pictures).where(pictures.c.id == user_id)
    result = await session.execute(query)
    return {"answer": result}


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
