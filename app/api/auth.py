from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
import crud


def get_current_user(
    db: Session = Depends(get_db), token: int = 0
):
    user = crud.get_user(db, user_id=token)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
