from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas import Post, PostCreate
import app.crud as crud

router = APIRouter()


@router.get("/", response_model=list[Post])
def read_post(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> list[Post]:
    post = crud.post.get_multi_by_user(
        db, user_id=1, skip=skip, limit=limit
    )
    return post


@router.post("/", response_model=Post)
def create_post(
    *,
    db: Session = Depends(get_db),
    post_in: PostCreate,
) -> Post:
    # TODO fix rewrite datetime type to string in <post_in> object
    post = crud.post.create_with_user(db, post_in, user_id=1)
    return post
