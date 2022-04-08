from datetime import date, datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str | None = None
    timestamp: date | None = datetime.utcnow()
    last_edit: date | None = datetime.utcnow()
    body: str | None = None


class PostCreate(PostBase):
    title: str
    body: str


class PostUpdate(PostBase):
    ...


class Post(PostBase):
    id: int
    title: str
    timestamp: date
    last_edit: date

    class Config:
        orm_mode = True
