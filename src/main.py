from fastapi import FastAPI

from src.auth.base_config import fastapi_users, auth_backend
from src.auth.schemas import UserRead, UserCreate
from src.colorings.router import router as router_colorings
from src.pictures.router import router as router_pictures


app = FastAPI(
    title="UPixel",
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

app.include_router(router_colorings)
app.include_router(router_pictures)
  

@app.get("/")
async def index():
    return {"result": True}


@app.get("/user")
async def get_user():
    return {"answer": "Инофрмация о юзере"}
