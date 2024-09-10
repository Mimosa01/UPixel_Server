from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="UPixel"
)

class Test(BaseModel):
  data: str
  

@app.get("/")
def index():
    return {"result": True}


@app.get("/user")
def get_user():
    return {"answer": "Инофрмация о юзере"}


@app.get("/pictures/{user_id}")
def get_user_pictures(user_id: int):
    return {"answer": "Получить все каринки пользователя"}


@app.get("/pictures/{pictures_id}")
def get_picture(picture_id: int):
    return {"answer": "Получить картинку пользователя"}


@app.post("/pictures/{picture_id}")
def add_picture(data: Test, picture_id: int):
    return {"answer": "Добавить картинку"}


@app.delete("pictures/{picture_id}")
def delete_picture(picture_id: int):
    return {"answer": "Удалить картинку"}


@app.get("/colorings")
def get_all_colorings():
    return {"answer": "Получитьвсе раскраски"}


@app.get("/colorings/{user_id}")
def get_user_colorings(user_id: int):
    return {"answer": "Получить все раскраски пользователя"}


@app.get("/colorings/{coloring_id}")
def get_coloring(coloring_id: int):
    # По идеи этот поинт должен получить раскраску, которой еще нет у пользователя и он должен сохранить ему ее
    # Конечно если у него такой раскраски нет
    return {"answer": "Получить раскраску пользователя"}


@app.post("/colorings/coloring_id")
def edit_user_coloring(coloring_id: int):
    return {"answer": "Изменить раскраску, которая есть у пользователя"}


@app.delete("/colorings/coloring_id")
def delete_user_coloring(coloring_id: int):
    return {"answer": "Удалить раскраску из базы пользователя"}
