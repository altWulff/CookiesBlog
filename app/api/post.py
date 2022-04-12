from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from schemas import Post, PostCreate
from models import User
import crud

router = APIRouter()


@router.post("/", response_model=Post)
def create_post(
    *,
    db: Session = Depends(get_db),
    post_in: PostCreate,
):
    post = crud.create_post(db, post_in)
    return post
