from typing import Protocol

from core.logger import get_logger
from tron_app.application.dto import QueryDto
from tron_app.application.usecases.uow_protocol import UowProtocol
from tron_app.domain.entities.wallet_query import WalletQuery

log = get_logger(__name__)


class WalletQueryRepositoryProtocol(Protocol):
    async def add(self, wallet_query: WalletQuery) -> None: ...


class RepositoryProtocol(Protocol):
    wallet_queries_repository: WalletQueryRepositoryProtocol


class CreateQueryUsecase:
    def __init__(
            self,
            uow: UowProtocol[RepositoryProtocol],
    ) -> None:
        self.uow = uow


    async def execute(
            self,
            query_dto: QueryDto,
    ) -> None:
        log.info("Executing CreateQueryUsecase by address: %s", query_dto.tron_address)
        wallet_query = WalletQuery(
            tron_address=query_dto.tron_address,
            query_time=query_dto.query_time,
            status=query_dto.status,
        )
        async with self.uow.transaction() as repo:
            await repo.wallet_queries_repository.add(wallet_query=wallet_query)
        log.info(
            "Succesfully executed CreateQueryUsecase by address: %s",
            query_dto.tron_address,
        )


