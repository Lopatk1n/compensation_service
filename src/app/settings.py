from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_DB: Optional[str] = None
    POSTGRES_PORT: int = 5432

    def __init__(self, **kwargs):  # for mypy compatibility
        super().__init__(**kwargs)


@lru_cache
def get_settings() -> Settings:
    return Settings(
        _env_file=".env",
        _env_file_encoding="utf-8",
    )
