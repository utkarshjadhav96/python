from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum as SQLEnum
from app.db import Base
from enum import Enum

class UserLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    expert = "expert"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=True)

    # ✅ FIX IS HERE
    level = Column(
        SQLEnum(UserLevel, name="user_level_enum"),
        default=UserLevel.beginner,
        nullable=False
    )

    hashed_password = Column(String, nullable=False)
