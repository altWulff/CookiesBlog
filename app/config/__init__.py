import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(env_path)


class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", default='secret_key')
    CSRF_KEY: str = os.getenv("CSRF_KEY", default='csrf_key')
    SQLALCHEMY_DATABASE_URL = str = os.getenv("SQLALCHEMY_DATABASE_URL", default='sqlite:///./cookies_app.db')


settings = Settings()

__all__ = [
    'settings'
]
