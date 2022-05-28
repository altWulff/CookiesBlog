import os

import motor.motor_asyncio
from bson import ObjectId

from app.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
db = client.blog


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId()

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
