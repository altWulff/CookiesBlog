from fastapi import APIRouter, Depends
from app.schemas import User
from app.models import User as UserModel
from fastapi import Depends
from .auth import get_current_user


router = APIRouter()


@router.post("/test-token", response_model=User)
def test_token(current_user: UserModel = Depends(get_current_user)):
    return current_user

