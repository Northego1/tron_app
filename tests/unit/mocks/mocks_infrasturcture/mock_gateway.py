from typing import TYPE_CHECKING, cast
from unittest.mock import AsyncMock, Mock

from tests.unit.mocks.shared_data import make_wallet
from tron_app.domain.entities.wallet import Wallet

if TYPE_CHECKING:
    from tron_app.infrastructure.gateway.tron_api_gateway import TronApiGateway


def get_wallet_effect(address: str) -> Wallet:
    wallet = make_wallet()
    wallet.address = address
    return wallet


MockTronApiGateway = cast("TronApiGateway", Mock())

MockTronApiGateway.get_wallet = AsyncMock(side_effect=get_wallet_effect)
