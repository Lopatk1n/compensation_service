from typing import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import get_settings  # noqa

settings = get_settings()

POSTGRES_USER = settings.POSTGRES_USER
POSTGRES_PASSWORD = settings.POSTGRES_PASSWORD
POSTGRES_DB = settings.POSTGRES_DB
POSTGRES_PORT = settings.POSTGRES_PORT

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine: Engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def yield_session() -> Generator:
    s = session()
    try:
        yield s
    finally:
        s.close()
