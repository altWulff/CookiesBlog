from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas import User, UserCreate
import app.crud


router = APIRouter()


@router.get('/', response_model=list[User])
def read_users(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100
):
    users = crud.get_users(db, skip, limit)
    return users


@router.post("/", response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
):
    user = crud.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.create_user(db, user_in)
    return user
