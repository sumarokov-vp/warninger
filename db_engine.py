from sqlalchemy import create_engine
import configparser

config = configparser.ConfigParser()
config.read('alembic.ini')
url = config['alembic']['sqlalchemy.url']
engine = create_engine(url)
