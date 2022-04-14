from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas import Post, PostCreate
import app.crud

router = APIRouter()


@router.post("/", response_model=Post)
def create_post(
    *,
    db: Session = Depends(get_db),
    post_in: PostCreate,
):
    post = crud.create_post(db, post_in)
    return post
