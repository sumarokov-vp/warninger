from sqlalchemy.orm import Session
from sqlalchemy import select
from db_engine import engine

from models import Setting

def get_setting(setting_name: str) -> str:
    with Session(engine) as session:
        value: str = str(session.scalars(
            select(Setting)
            .where(Setting.name == setting_name)
        ).one().value)
        return value
