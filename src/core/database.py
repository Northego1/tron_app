from typing import AsyncGenerator, Self

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from core.config import Config


class DataBase:
    def __init__(self: Self, config: Config) -> None:
        self.config = config
        self.engine = create_async_engine(url=config.db.dsn)
        self.async_session_maker = async_sessionmaker(self.engine, expire_on_commit=False)

    async def session_maker(self: Self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session_maker() as session:
            yield session


class Base(DeclarativeBase):
    pass
