from typing import TYPE_CHECKING

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .base import Base
from .user import User

if TYPE_CHECKING:
    from .comment import Comment  # noqa: F401
    from .tag import Tag  # noqa: F401


article_tag_association = Table(
    "article_tag",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)

    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author = relationship(User, uselist=False)

    comments = relationship("Comment", uselist=True)
    tags = relationship("Tag", uselist=True, secondary=article_tag_association)
