from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy import func, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    posts = relationship("Post")


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    timestamp = Column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
    last_edit = Column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
    body = Column(Text, nullable=False)



