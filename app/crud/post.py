from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.models import Post
from app.schemas import PostCreate, PostUpdate
from .base import CRUDBase


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    def create_with_user(
        self, db: Session, obj_in: PostCreate, user_id: int
    ) -> Post:
        db_obj = self.model(**obj_in.dict(), user_id=user_id)
        db_obj.timestamp = obj_in.timestamp
        db_obj.last_edit = obj_in.last_edit
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_user(
        self, db: Session, user_id: int, skip: int = 0, limit: int = 100
    ) -> list[Post]:
        return (
            db.query(self.model)
            .filter(Post.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


post = CRUDPost(Post)

__all__ = (
    'post',
)
