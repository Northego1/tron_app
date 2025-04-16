from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parents[2]

env_file = ".env"


class PostgresSettings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str

    @property
    def dsn(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


class TronApiSettings(BaseSettings):
    API_DOMAIN: str


class AppSettings(BaseSettings):
    PROD: str


class Config:
    def __init__(self, prod_type: Literal["DEV", "TEST"] = "DEV") -> None:
        match prod_type:
            case "DEV":
                env_file = BASE_DIR / ".env"
            case "TEST":
                env_file = BASE_DIR / ".env.test"

        load_dotenv(env_file, override=True)

        self.db = PostgresSettings()  # type: ignore
        self.tron = TronApiSettings()  # type: ignore
        self.app = AppSettings()  # type: ignore


config = Config()
