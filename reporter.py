from time import sleep
from sqlalchemy import select
from datetime import datetime, timedelta

from db_engine import engine
from sqlalchemy.orm import Session
from models import Warning
from models import Recipient
from bot import bot

def process_warning(warning: Warning, session: Session) -> int:

    # Get datetime of start notify based on last_success
    if not warning.last_success: # type: ignore
        print("No last_success")
        return -1
    notification_timeout: datetime = warning.last_success + timedelta( # type: ignore
        days=warning.wait_days, # type: ignore
        hours=warning.wait_hours, # type: ignore
        minutes=warning.wait_minutes, # type: ignore
        seconds=warning.wait_seconds, # type: ignore
    )

    # Get datetime of next notification based on last_notification
    next_notification: datetime
    if not warning.last_notification: # type: ignore
        print("First notification")
        next_notification = warning.last_success # type: ignore
    else:
        next_notification = warning.last_notification + timedelta( # type: ignore
            days= warning.repeat_days, # type: ignore
            hours= warning.repeat_hours, # type: ignore
            minutes= warning.repeat_minutes, # type: ignore
            seconds= warning.repeat_seconds, # type: ignore
        )

    # Notify if next notification is in the past
    # and update last_success
    if next_notification < datetime.now() and notification_timeout < datetime.now():
        notify(warning= warning, session= session)
        warning.last_notification = datetime.now() # type: ignore
        session.commit()
        return 0
    else:
        print(f"Now datetime: {datetime.now()}")
        print(f"notification_timeout: {notification_timeout}")
        print(f"next_notification: {next_notification}")
        print("Not time yet")
        return 1

def notify(warning: Warning, session: Session):
    recipients = session.scalars(
        select(Recipient)
        .where(Recipient.warning_id == warning.id)
    )
    for recipient in recipients:
        bot.send_message(recipient.chat_id, warning.message) # type: ignore

if __name__ == "__main__":
    while True:
        print(f"Start loop -- {datetime.now()}")
        with Session(engine, expire_on_commit= False) as session:
            warnings = session.scalars(
                select(Warning)
            )
            for warning in warnings:
                process_warning(warning= warning, session= session)
        sleep(100)
