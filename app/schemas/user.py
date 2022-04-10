from pydantic import BaseModel


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
