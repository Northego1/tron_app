from typing import AsyncGenerator
from unittest.mock import AsyncMock, Mock

import pytest
import pytest_mock
from sqlalchemy.ext.asyncio import AsyncSession

from core.uow import Repository, UnitOfWork
from tests.unit.mocks.shared_data import make_wallet_query


async def async_gen(value) -> AsyncGenerator[AsyncSession, None]:  # type: ignore # noqa: ANN001
    yield value


@pytest.mark.asyncio
async def test_uow_commits_on_success() -> None:
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.commit = AsyncMock(return_value=None)
    mock_session.begin = AsyncMock(return_value=None)
    mock_session.rollback = AsyncMock(return_value=None)

    db = Mock()
    db.session_maker = Mock(return_value=async_gen(mock_session))

    uow = UnitOfWork(db, Repository)

    async with uow.transaction() as repo:
        await repo.wallet_queries_repository.add(wallet_query=make_wallet_query())

    mock_session.begin.assert_awaited_once()
    mock_session.commit.assert_awaited_once()
    mock_session.rollback.assert_not_awaited()


@pytest.mark.asyncio
async def test_uow_rollbacks_on_failure(mocker: pytest_mock.MockerFixture) -> None:
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.commit = AsyncMock(return_value=None)
    mock_session.begin = AsyncMock(return_value=None)
    mock_session.rollback = AsyncMock(return_value=None)

    db = Mock()
    db.session_maker = Mock(return_value=async_gen(mock_session))

    uow = UnitOfWork(db, Repository)

    mocker.patch(
        "tron_app.infrastructure.repository.wallet_query_repository.WalletQueryRepository.add",
        side_effect=Exception,
    )
    with pytest.raises(Exception):  # noqa: B017, PT011
        async with uow.transaction() as repo:
            await repo.wallet_queries_repository.add(wallet_query=make_wallet_query())

    mock_session.begin.assert_awaited_once()
    mock_session.commit.assert_not_awaited()
    mock_session.rollback.assert_awaited_once()
