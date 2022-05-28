from pydantic import BaseModel, EmailStr, Field

from app.db import ObjectId, PyObjectId


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str
    is_active: bool = True
    is_superuser: bool = False

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "Jane Doe",
                "email": "jane@mail.com",
                "password": "1234",
            }
        }


class UserUpdate(BaseModel):
    username: str | None
    email: EmailStr | None
    password: str | None
    is_active: bool = True
    is_superuser: bool = False

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "Jane Doe",
                "email": "jane@mail.com",
            }
        }
