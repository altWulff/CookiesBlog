from sqlalchemy.orm import Session
from app.models import Post
from app.schemas import PostCreate, PostUpdate


def create_post(db: Session, post: PostCreate) -> dict:
    new_post = Post(
        title=post.title,
        body=post.body,
        timestamp=post.timestamp,
        last_edit=post.last_edit,
        user_id=1
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post.__dict__
