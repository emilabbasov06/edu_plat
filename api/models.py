import enum
from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Creating DEFAULT Enum objects

class UserType(enum.Enum):
    student = 'Student'
    teacher = 'Teacher'
    researcher = 'Researcher'

class PostCategoryType(enum.Enum):
    general = 'General Education'
    stem = 'STEM (Science, Technology, Engineering, Mathematics)'
    lang_lit = 'Language & Literature'
    other = 'Other'



# Creating Models for Future Use

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    acc_type = Column(Enum(UserType), default=UserType.student)

class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(Text)
    category = Column(Enum(PostCategoryType), default=PostCategoryType.other)
    date_posted = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('UserModel')
