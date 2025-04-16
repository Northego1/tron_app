from typing import Protocol

from tron_app.application.dto import Paginator, QueryDto
from tron_app.domain.entities.wallet import Wallet
from tron_app.domain.entities.wallet_query import WalletQuery


class CreateQueryUsecaseProtocol(Protocol):
    async def execute(self, query_dto: QueryDto) -> None: ...


class GetQueriesUsecase(Protocol):
    async def execute(self, paginator: Paginator) -> list[WalletQuery]: ...


class GetWalletUsecaseProtocol(Protocol):
    async def execute(self, address: str) -> Wallet: ...
