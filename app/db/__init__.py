from .base import Base
from .session import SessionLocal, engine


class DBCTXManager:
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


def get_db():
    with DBCTXManager() as db:
        yield db
