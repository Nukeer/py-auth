from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from . import service

from src.users import schema
from src.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=schema.User)
async def register(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service.create_user(db, user=user)


@router.get("/", response_model=List[schema.User])
async def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = service.get_users(db, skip, limit)
    return users
