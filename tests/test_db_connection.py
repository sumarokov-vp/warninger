import pytest

from sqlalchemy import select
from sqlalchemy.orm import Session
from db_engine import engine

def test_db_connection():
    with Session(engine) as session:
        test_1 = session.execute(select(1)).scalar()
        assert test_1 == 1
