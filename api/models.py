from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


#class UserModel(Base):
#    __tablename__ = 'users'
#
#    id = Column(Integer, primary_key=True, autoincrement=True)
#    full_name = Column(String(255))
#    email = Column(String(255), unique=True)
