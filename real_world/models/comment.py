from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .article import Article
from .base import Base
from .user import User


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    body = Column(String)

    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author = relationship(User, uselist=False)

    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    article = relationship(Article, uselist=False)
