from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
from sqlalchemy import BooleanClauseList, Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from bot import bot

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
    status_id = Column(Integer, ForeignKey('warning_status.id'))
    status = relationship("WarningStatus", back_populates="warnings")
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
    enabled = Column(Boolean, server_default='1')
    name = Column(String)
    description = Column(String)
    success_message = Column(String)


    def all_recipients_mailing(self, session: Session, message: str):
        recipients = session.scalars(
            select(Recipient)
            .where(Recipient.warning_id == self.id)
        )
        for recipient in recipients:
            bot.send_message(
                chat_id= int(recipient.chat_id), # type: ignore
                text= message,
                parse_mode= "HTML",
            ) # type: ignore

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
    __table_args__ = (
        UniqueConstraint('name', name='name_unique'),
    )

class WarningStatus(Base):
    __tablename__ = 'warning_status'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    success = Column(Boolean, server_default='0')
    warnings = relationship("Warning", back_populates="status")

    __table_args__ = (
        UniqueConstraint('name', name='name_unique'),
    )
