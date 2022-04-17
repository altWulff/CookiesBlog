from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from sqlalchemy.orm import Session
from jose import jwt
from app.db import get_db
from app.config import settings
from app.schemas import TokenPayload
from app.models import User as UserModel
import app.crud as crud


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/login/access-token"
)


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, user_id=token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


def get_current_active_user(
    current_user: UserModel = Depends(get_current_user)
) -> UserModel:
    if not crud.user.is_active(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user


def get_current_active_superuser(
    current_user: UserModel = Depends(get_current_user)
) -> UserModel:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user doesn't have enough privileges"
        )
    return current_user
