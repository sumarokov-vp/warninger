from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    chat_id = Column(Integer)

    warnings = relationship("Warning", back_populates="user")

class Warning(Base):
    __tablename__ = 'warnings'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="warnings")

class Recipients(Base):
    __tablename__ = 'recipients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    chat_id = Column(Integer)
