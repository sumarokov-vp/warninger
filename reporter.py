from logging import warn
from time import sleep
from sqlalchemy import select
from datetime import datetime, timedelta

from db_engine import engine
from sqlalchemy.orm import Session
from models import Warning
from models import Recipient
from bot import bot
from telebot import apihelper
from settings import get_setting

def process_warning(warning: Warning, session: Session) -> int:

    # Get datetime of start notify based on last_success
    print(f"\nWarning name: {warning.name}")
    print(f"Last success: {warning.last_success}")

    if not warning.last_success: # type: ignore
        return -1
    notification_timeout: datetime = warning.last_success + timedelta( # type: ignore
        days=warning.wait_days, # type: ignore
        hours=warning.wait_hours, # type: ignore
        minutes=warning.wait_minutes, # type: ignore
        seconds=warning.wait_seconds, # type: ignore
    )
    print(f"Notification start time: {notification_timeout}")


    # Get datetime of next notification based on last_notification
    next_notification: datetime
    if not warning.last_notification: # type: ignore
        next_notification = warning.last_success # type: ignore
    else:
        print(f"Last notification: {warning.last_notification}")
        print(f"{warning.repeat_days=} {warning.repeat_hours=} {warning.repeat_minutes=} {warning.repeat_seconds=}")
        next_notification = warning.last_notification + timedelta( # type: ignore
            days= warning.repeat_days or 0, # type: ignore
            hours= warning.repeat_hours or 0, # type: ignore
            minutes= warning.repeat_minutes or 0, # type: ignore
            seconds= warning.repeat_seconds or 0, # type: ignore
        )

    # Notify if next notification is in the past
    # and update last_success
    if notification_timeout < datetime.now():
        if next_notification < datetime.now():
            message = f"""
    {warning.message}
    _____________________
    <code>
    Warning name: {warning.name}
    Last success signal: {warning.last_success}
    </code>
    """
            warning.all_recipients_mailing(
                session= session,
                message= message,
            )
            warning.last_notification = datetime.now() # type: ignore
            session.commit()
            return 0
        else:
            print(f"Last notification: {warning.last_notification}")
            print(f"Now datetime: {datetime.now()}")
            print(f"Next_notification: {next_notification}")
            return 1
    else:
        print(f"Not time for notification yet")
        return 2

if __name__ == "__main__":
    while True:
        print(f"Start loop -- {datetime.now()}")
        with Session(engine, expire_on_commit= False) as session:
            warnings = session.scalars(
                select(Warning)
                .where(Warning.enabled == True) # type: ignore
                .where(Warning.last_success != None) # type: ignore
            )
            for warning in warnings:
                # try:
                process_warning(warning= warning, session= session)
                # except apihelper.ApiTelegramException as e:
                #     print(f"Telegram API error: {e}")
                #     session.rollback()
                #     continue
        sleep_time = int(get_setting('reporter_sleep_time_sec'))
        sleep(sleep_time)
