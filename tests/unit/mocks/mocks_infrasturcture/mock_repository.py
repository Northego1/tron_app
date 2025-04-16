from typing import TYPE_CHECKING, cast
from unittest.mock import AsyncMock, Mock

from tests.unit.mocks.shared_data import make_wallet_query
from tron_app.domain.entities.wallet_query import WalletQuery

if TYPE_CHECKING:
    from tron_app.infrastructure.repository.wallet_query_repository import WalletQueryRepository


def get_all_side_effect(limit: int, offset: int) -> list[WalletQuery]:  # noqa: ARG001
    return [make_wallet_query() for _ in range(limit)]


MockWalletQueryRepository = cast("WalletQueryRepository", Mock())

MockWalletQueryRepository.add = AsyncMock(return_value=None)
MockWalletQueryRepository.get_all = AsyncMock(side_effect=get_all_side_effect)
