### Deployment

- install poetry
```
curl -sSL https://install.python-poetry.org | python3.11 -
poetry config virtualenvs.in-project true
poetry env use python3.11
poetry shell
```

- install dependencies
```
poetry install
```

- create database and connect
```
cp alembic.ini_ alembic.ini
vim alembic.ini
# replace sqlalchemy.url with your server credentials
pytest tests/test_db_connection.py
```

- deploy database
```
alembic upgrade head
# execute test_objects.sql
# select create_test_objects()
```

- run listener and reporter

- setup warnings in the db

- setup telegram bot token
