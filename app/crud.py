from sqlalchemy.orm import Session
import models
import schemas
from security import Crypt


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter_by(id=user_id).first()


def get_user_by_name(db: Session, user_name: int):
    return db.query(models.User).filter_by(username=user_name).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter_by(email=email).first()


def get_superuser(db: Session):
    return db.query(models.User).filter(models.User.is_superuser).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> dict:
    hash_password = Crypt.hash(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.__dict__
