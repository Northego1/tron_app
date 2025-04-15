from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class BaseConfig(BaseSettings):
    """Base configuration settings."""

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="allow",
    )


class PostgresSettings(BaseConfig):
    """Database configuration settings."""

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



class Config:
    """Application configuration settings."""

    db = PostgresSettings()  # type: ignore



config = Config()
