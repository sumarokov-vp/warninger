from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import DateTime

from models import Warning
from db_engine import engine

from reporter import process_warning

def test_example_warning():
    with Session(engine, expire_on_commit= False) as session:
        test_warning = session.scalars(
            select(Warning)
            .where(Warning.message == 'Test message')
        ).one()

        test_warning.last_success = datetime.now() - timedelta(days= 1,) # type: ignore
        test_warning.wait_days = 0 # type: ignore
        test_warning.wait_hours = 10 # type: ignore
        test_warning.wait_minutes = 0 # type: ignore
        test_warning.wait_seconds = 0 # type: ignore
        test_warning.last_notification = None # type: ignore
        test_warning.repeat_days = 0 # type: ignore
        test_warning.repeat_hours = 12 # type: ignore
        test_warning.repeat_minutes = 0 # type: ignore
        test_warning.repeat_seconds = 0 # type: ignore
        session.commit()

        print(f"test_warning.last_success: {test_warning.last_success}")
        assert process_warning(
            warning= test_warning,
            session= session
        ) == 0
