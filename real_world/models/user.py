from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .base import Base

user_follower_association = Table(
    "user_follower",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("follower_id", Integer, ForeignKey("users.id")),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    bio = Column(String)
    image = Column(String)
    followers = relationship(
        "User",
        secondary=user_follower_association,
        primaryjoin=(id == user_follower_association.c.user_id),
        secondaryjoin=(id == user_follower_association.c.follower_id),
        uselist=True,
    )
