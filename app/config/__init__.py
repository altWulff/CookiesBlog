import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

env_path = Path(".") / ".env"
load_dotenv(env_path)


class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", default="secret_key")
    CSRF_KEY: str = os.getenv("CSRF_KEY", default="csrf_key")
    SQLALCHEMY_DATABASE_URL: str = os.getenv(
        "SQLALCHEMY_DATABASE_URL", default="sqlite:///./cookies_app.db"
    )
    PASSWORD_ALGORITHM = "sha256_crypt"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    MONGODB_URL = os.environ.get(
        "MONGODB_URL", "mongodb://localhost:27017/cookies_blog"
    )


settings = Settings()

__all__ = ("settings",)
