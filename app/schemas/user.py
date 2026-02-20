import uuid

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str


class UserRead(UserBase):
    id: uuid.UUID
    is_admin: bool

    class Config:
        from_attributes = True
