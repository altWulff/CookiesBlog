from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas import User, UserCreate
from app.models import User as UserModel
import app.crud as crud


router = APIRouter()


@router.get('/', response_model=list[User])
def read_users(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100
):
    users = crud.user.get_multi(db, skip, limit)
    return users


@router.post("/", response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
) -> Any:
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user
