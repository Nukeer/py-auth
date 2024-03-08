from fastapi import FastAPI

from src import models
from src.database import engine

from src.users.router import router as router_user
from src.auth.router import router as router_auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_user)
app.include_router(router_auth)
