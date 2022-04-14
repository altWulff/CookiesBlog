from datetime import date, datetime
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str | None = None
    timestamp: datetime | None = datetime.utcnow()
    last_edit: datetime | None = datetime.utcnow()
    body: str | None = None


class PostCreate(PostBase):
    title: str
    body: str


class PostUpdate(PostBase):
    ...


class Post(PostBase):
    id: int
    title: str
    timestamp: datetime
    last_edit: datetime

    class Config:
        orm_mode = True
