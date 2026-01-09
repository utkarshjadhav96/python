from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class UserBase(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    expert = "expert"


class UserBase(BaseModel):
    username: str
    email: str
    age : Optional[int] = None
    level : UserBase = UserBase.beginner


class UserIn(UserBase):
    password : str


class UserInBase(UserBase):
    id : int

    class Config:
        orm_mode = True

class userInDB(UserInBase):
    hashed_password : str


class TokenData(BaseModel):
    username: Optional[str] = None

class token(BaseModel):
    access_token: str
    token_type: str