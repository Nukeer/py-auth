from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from .schema import AuthLogin, AuthRegister

from . import service
from ..users import schema

router = APIRouter(
    prefix="/oauth",
    tags=["Authentication"],
)


@router.post("/login")
async def login(user: AuthLogin, db: Session = Depends(get_db)):
    auth = service.authenticate(db, user)
    return {"message": auth}


@router.post("/register", response_model=schema.User)
async def register(user: AuthRegister, db: Session = Depends(get_db)):
    auth = service.register(db, user)
    return auth
