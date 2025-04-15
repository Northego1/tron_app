from datetime import UTC, datetime
from typing import Protocol

from tron_app.application.usecases.uow_protocol import UowProtocol
from tron_app.domain.entities.wallet_query import WalletQuery


class WalletQueriesRepositoryProtocol(Protocol):
    async def add(self, wallet_query: WalletQuery) -> None: ...


class RepositoryProtocol(Protocol):
    wallet_queries_repository: WalletQueriesRepositoryProtocol


class CreateQuery:
    def __init__(
            self,
            uow: UowProtocol[RepositoryProtocol],
            tron_api_gateway: TronApiGatewayProtocol,
    ) -> None:
        self.uow = uow
        self.tron_api_gateway = tron_api_gateway


    async def execute(
            self,
            address: str,
    ) -> Wallet:
        wallet = await self. tron_api_gateway.get_wallet(address=address)

        async with self.uow.transaction() as repo:


