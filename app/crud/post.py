from fastapi import Body

from app.schemas import Post, PostUpdate

from .base import CRUDBase


class CRUDPost(CRUDBase[Post, PostUpdate]):
    async def create_with_user(self, user_id: int, obj_in: Post = Body(...)) -> dict:
        record = await super().create(obj_in)
        return record

    async def get_multi_by_user(
        self, user_id: int, skip: int = 0, limit: int = 100
    ) -> list[dict]:
        record = await super().get_multi(skip, limit)
        return record


post = CRUDPost("post")

__all__ = ("post",)
