# from datetime import timedelta
# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
#
# from app.config import settings, security
# from app.schemas import User, Token
# from app.models import User as UserModel
# from app.db import get_db
# from .auth import get_current_user
# import app.crud as crud
#
# router = APIRouter()
#
#
# @router.post("/login/access-token", response_model=Token)
# def login_access_token(
#     db: Session = Depends(get_db),
#     form_data: OAuth2PasswordRequestForm = Depends()
# ) -> dict:
#     """
#     OAuth2 compatible token login, get an access token for future requests
#     """
#     user = crud.user.authenticate(
#         db, email=form_data.username, password=form_data.password
#     )
#     if not user:
#         raise HTTPException(
#             status_code=400, detail="Incorrect email or password")
#     elif not crud.user.is_active(user):
#         raise HTTPException(
#             status_code=400, detail="Inactive user")
#     access_token_expires = timedelta(
#         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     return {
#         "access_token": security.create_access_token(
#             user.id, expires_delta=access_token_expires
#         ),
#         "token_type": "bearer",
#     }
#
#
# @router.post("/test-token", response_model=User)
# def test_token(current_user: UserModel = Depends(get_current_user)):
#     return current_user
