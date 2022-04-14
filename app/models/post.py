from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy import func
from app.db import Base


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
