from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    chat_id = Column(Integer)

    warnings = relationship("Warning", back_populates="user")
    __table_args__ = (
        UniqueConstraint('chat_id', name='chat_id_unique'),
    )

class Warning(Base):
    __tablename__ = 'warnings'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="warnings")
    # last date time of successful notification
    last_success = Column(DateTime, nullable=True)
    wait_days = Column(Integer, server_default='0')
    wait_hours = Column(Integer, server_default='0')
    wait_minutes = Column(Integer, server_default='0')
    wait_seconds = Column(Integer, server_default='0')
    last_notification = Column(DateTime, nullable=True)
    repeat_days = Column(Integer, server_default='0')
    repeat_hours = Column(Integer, server_default='0')
    repeat_minutes = Column(Integer, server_default='0')
    repeat_seconds = Column(Integer, server_default='0')
    recipients = relationship("Recipient", back_populates="warning")

class Recipient(Base):
    __tablename__ = 'recipients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    chat_id = Column(Integer)
    warning_id = Column(Integer, ForeignKey('warnings.id'))
    warning = relationship("Warning", back_populates="recipients")

class Setting(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
