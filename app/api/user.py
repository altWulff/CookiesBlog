from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas import User, UserCreate, UserUpdate
from app.models import User as UserModel
from app.api.auth import get_current_user
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


@router.post("/me", response_model=User)
def get_current_user(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return current_user


@router.put('{user_id}', response_model=User)
def update_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    user_schema: UserUpdate,
    current_user: UserModel = Depends(get_current_user)
) -> UserModel:
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='The user with this username does not exist in the system'
        )
    user_update = crud.user.update(db, db_obj=user, obj_in=user_schema)
    return user_update
