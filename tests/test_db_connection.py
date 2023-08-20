import pytest

from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

import configparser

config = configparser.ConfigParser()
config.read('alembic.ini')

url = config['alembic']['sqlalchemy.url']
engine = create_engine(url)

def test_db_connection():
    with Session(engine) as session:
        test_1 = session.execute(select(1)).scalar()
        assert test_1 == 1
