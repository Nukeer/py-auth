from pydantic import BaseModel, EmailStr


class AuthBase(BaseModel):
    email: EmailStr


class AuthLogin(AuthBase):
    password: str


class AuthRegister(AuthLogin):
    pass
