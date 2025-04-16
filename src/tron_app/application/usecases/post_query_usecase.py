from typing import Protocol

from core.logger import get_logger
from tron_app.application.exceptions import ApplicationError
from tron_app.domain.entities.wallet import Wallet

log = get_logger(__name__)


class WalletNotFoundError(ApplicationError): ...


class TronApiGatewayProtocol(Protocol):
    async def get_wallet(self, address: str) -> Wallet | None: ...


class GetWalletUsecase:
    def __init__(
            self,
            tron_api_gateway: TronApiGatewayProtocol,
    ) -> None:
        self.tron_api_gateway = tron_api_gateway


    async def execute(self, address: str) -> Wallet:
        log.info("Executing get wallet usecase by address: %s", address)
        if not (
            wallet := await self.tron_api_gateway.get_wallet(address=address)
        ):
            log.info("Not found wallet by address: %s", address)
            raise WalletNotFoundError(status_code=404, detail="Wallet not found")
        log.info("Successfully executed get wallet usecase by address: %s", address)
        return wallet



