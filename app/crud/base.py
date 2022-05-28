"""
Module contains superclass for CRUD
"""

from typing import Generic, TypeVar

from fastapi import Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from app.db import db

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[CreateSchemaType, UpdateSchemaType]):
    """Create Read Update Delete, base operation on database"""

    def __init__(self, model: str):
        """
        :param model: collection name in database
        """
        self.model = model

    async def get(self, db_id: str) -> dict | None:
        """
        Get object from database
        :param db_id: cursor object
        :return: database record or None
        """
        db_obj = await db[self.model].find_one({"_id": db_id})
        return db_obj

    async def get_multi(self, skip: int = 0, limit: int = 100) -> list[dict]:
        """
        Get list of objects in database
        :param skip: offset
        :param limit: max request
        :return: list of records from database, length limit 1000 rec.
        """
        db_objects = await db[self.model].find().to_list(1000)
        return db_objects[skip : skip + limit]

    async def create(self, obj_in: CreateSchemaType = Body(...)) -> dict:
        """
        Create object in database
        :param obj_in: data from body request
        :return: database record, from created data
        """
        db_obj = jsonable_encoder(obj_in)
        new_student = await db[self.model].insert_one(db_obj)
        create_student = await db[self.model].find_one({"_id": new_student.inserted_id})
        return create_student

    async def update(self, db_id: str, obj: UpdateSchemaType = Body(...)) -> dict:
        """
        Update object in database
        :param db_id: cursor update record
        :param obj: request body with data
        :return: updated record
        """
        obj = {k: v for k, v in obj.dict().items() if v is not None}

        if obj:
            update_result = await db[self.model].update_one(
                {"_id": db_id}, {"$set": obj}
            )

            if update_result.modified_count == 1:
                if (
                    update_obj := await db[self.model].find_one({"_id": db_id})
                ) is not None:
                    return update_obj

        if (existing_obj := await db[self.model].find_one({"_id": db_id})) is not None:
            return existing_obj

    async def remove(self, db_id: str) -> dict:
        """
        Remove object in database
        :param db_id: cursor remove obj
        :return: deleted dict object
        """
        obj = await db[self.model].delete_one({"_id": db_id})
        return obj
