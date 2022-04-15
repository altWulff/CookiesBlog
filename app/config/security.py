from datetime import datetime, timedelta
from typing import Any
from jose import jwt
from passlib.context import CryptContext
from ..config import settings


class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can`t instance directly")


class Crypt(metaclass=NoInstance):
    crypt_ctx = CryptContext(schemes=[settings.PASSWORD_ALGORITHM])

    @classmethod
    def verify(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.crypt_ctx.verify(plain_password, hashed_password)

    @classmethod
    def hash(cls, password: str) -> str:
        return cls.crypt_ctx.hash(password)


def create_access_token(
    subject: str | Any, expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
