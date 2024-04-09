from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
  __tablename__ = 'User'

  id = Column(Integer(), primary_key=True)
  fullname = Column(String(100), nullable=False)
  email = Column(String(100), nullable=False)
  websiteurl = Column(String(100), nullable=False)
  phonenumber = Column(Integer(), nullable=True)
  created_on = Column(DateTime(), default=datetime.now)
