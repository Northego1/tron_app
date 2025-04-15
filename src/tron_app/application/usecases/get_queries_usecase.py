from typing import Protocol

from tron_app.application.dto import Paginator
from tron_app.application.usecases.uow_protocol import UowProtocol
from tron_app.domain.entities.wallet_query import WalletQuery


class WalletQueryRepositoryProtocol(Protocol):
    async def get_all(self, limit: int, offset: int) -> list[WalletQuery]: ...


class RepositoryProtocol(Protocol):
    wallet_queries_repository: WalletQueryRepositoryProtocol


class GetQueriesUsecase:
    def __init__(
            self,
            uow: UowProtocol[RepositoryProtocol],
    ) -> None:
        self.uow = uow


    async def execute(self, paginator: Paginator) -> list[WalletQuery]:
        async with self.uow.transaction() as repo:
            return await repo.wallet_queries_repository.get_all(
                limit=paginator.limit,
                offset=paginator.offset,
            )

