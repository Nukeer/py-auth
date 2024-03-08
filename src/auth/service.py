from fastapi import HTTPException
from sqlalchemy.orm import Session
from .schema import AuthLogin, AuthRegister
from src.users.service import get_user_by_email
from . import dependencies
from .. import models


def authenticate(db: Session, user: AuthLogin):
    get_user = get_user_by_email(db, user.email)
    if not get_user:
        raise HTTPException(status_code=400, detail="Email don't registered")
    if not dependencies.verify_password(user.password, get_user.hashed_password):
        raise HTTPException(status_code=400, detail="Password don't match")
    return get_user


def register(db: Session, user: AuthRegister):
    get_user = get_user_by_email(db, user.email)
    if get_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)


def create_user(db: Session, user: AuthRegister):
    db_user = models.User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
