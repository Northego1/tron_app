import contextlib
import dataclasses
from typing import AsyncGenerator, Self

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import DataBase
from core.exceptions import AppError
from core.logger import get_logger

log = get_logger(__name__)


@dataclasses.dataclass(slots=True)
class Repository:
    _conn: AsyncSession



class UnitOfWork:
    def __init__(self, db: DataBase) -> None:
        self.db = db

    @contextlib.asynccontextmanager
    async def transaction(self: Self) -> AsyncGenerator[Repository, None]:
        async for session in self.db.session_maker():
            await session.begin()
            try:
                yield Repository(session)
                log.debug("Commiting transaction")
                await session.commit()
            except AppError as e:
                log.exception(
                    "AppError during transaction: %s, rollback",
                    e.detail,
                )
                await session.rollback()
                raise e from e
            except Exception as e:
                log.critical(
                    "Unexpected error during transaction: %s, rollback",
                    e,
                    exc_info=True,
                )
                await session.rollback()
                raise AppError from e
