from typing import TYPE_CHECKING, cast
from unittest.mock import Mock

from unit.mocks.mocks_infrasturcture.mock_repository import MockWalletQueryRepository

if TYPE_CHECKING:
    from core.uow import UnitOfWork


uow_mock = cast("UnitOfWork", Mock())


class RepositoryMock:
    wallet_queries_repository = MockWalletQueryRepository


class Uow:
    async def __aenter__(self) -> RepositoryMock:
        return RepositoryMock()

    async def __aexit__(self, *_: object) -> None:
        pass



uow_mock.transaction = Mock(side_effect=Uow)
