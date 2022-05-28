from datetime import datetime

from pydantic import BaseModel, Field

from app.db import ObjectId, PyObjectId


class Post(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    timestamp: datetime = datetime.utcnow()
    last_edit: datetime = datetime.utcnow()
    body: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Jane Doe",
                "body": "Experiments, Science, and Fashion in Nanophotonics",
            }
        }


class PostUpdate(BaseModel):
    title: str | None
    body: str | None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Jane Doe",
                "body": "Experiments, Science, and Fashion in Nanophotonics",
            }
        }
