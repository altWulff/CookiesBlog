from typing import Any

from fastapi import Body

from app.config.security import Crypt
from app.db import db
from app.schemas import User, UserUpdate

from .base import CRUDBase


class CRUDUser(CRUDBase[User, UserUpdate]):
    async def get_by_email(self, email: str) -> dict | None:
        """
        Get user from database
        :param email: user emil
        :return: database record or None
        """
        db_obj = await db[self.model].find_one({"email": f"/@{email}/i"})
        return db_obj

    async def create(self, obj_in: User = Body(...)) -> dict:
        """
        Create user in database, with hashed password
        :param obj_in: data from body request
        :return: database record, from created data
        """
        obj_in.password = Crypt.hash(obj_in.password)
        record = await super().create(obj_in)
        return record

    async def update(self, db_id: str, obj: UserUpdate = Body(...)) -> dict:
        record = await super().update(db_id, obj)
        if "password" in record:
            record["password"] = str(Crypt.hash(record["password"]))
        return record

    async def authenticate(self, email: str, password: str) -> dict | None:
        auth_user = await self.get_by_email(email)
        if not auth_user:
            return None
        if not Crypt.verify(password, auth_user["password"]):
            return None
        return auth_user

    @staticmethod
    async def is_active(user: User) -> bool:
        return user.is_active

    @staticmethod
    async def is_superuser(user: User) -> bool:
        return user.is_superuser


user = CRUDUser("user")

__all__ = ("user",)
