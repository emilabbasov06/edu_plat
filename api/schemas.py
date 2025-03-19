from pydantic import BaseModel
from typing import Optional

from models import UserType, PostCategoryType

# USERS TABLE

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    acc_type: UserType

    class Config:
        from_attributes = True


class CreateUserSchema(BaseModel):
    name: str
    email: str
    password: str
    acc_type: UserType

    class Config:
        from_attributes = True


# POSTS TABLE

class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    category: PostCategoryType
    date_posted: str
    user_id: int

    class Config:
        from_attributes = True

class CreatePostSchema(BaseModel):
    title: str
    content: str
    category: PostCategoryType
    user_id: int

    class Config:
        from_attributes = True
