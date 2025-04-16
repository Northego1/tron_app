import base58

from core.config import Config
from core.http_client import HttpClient
from core.logger import get_logger
from tron_app.domain.entities.wallet import Wallet
from tron_app.infrastructure.exception import InfrastructureError

log = get_logger(__name__)


class GatewayEmptyResponseError(InfrastructureError): ...


class TronApiGateway:
    def __init__(
            self,
            http_client: HttpClient,
            config: Config,
    ) -> None:
        self.client = http_client.client
        self.api_domain = config.tron.API_DOMAIN


    async def get_wallet(self, address: str) -> Wallet:
        # ________Баланс________
        log.debug("Sending account request to TRON_API by address: %s", address)
        acc_resp = await self.client.get(f"{self.api_domain}/v1/accounts/{address}")
        acc_data = acc_resp.json()
        log.debug("%s", acc_data)
        if "data" not in acc_data or not acc_data["data"]:
            log.debug("Account with address %s not found", address)
            raise GatewayEmptyResponseError(
                status_code=400,
                detail=f"Account with address {address!r} not found",
            )
        trx_balance = acc_data["data"][0].get("balance", 0)

        # ________Ресурсы________
        log.debug("Sending resource request to TRON_API by address: %s", address)
        res_resp = await self.client.post(f"{self.api_domain}/wallet/getaccountresource", json={
            "address": base58.b58decode_check(address).hex(),
        })
        res_data = res_resp.json()
        bandwidth = res_data.get("freeNetLimit", 0)
        energy = res_data.get("EnergyLimit", 0)

        return Wallet(
            address=address,
            balance_trx=trx_balance,
            bandwidth=bandwidth,
            energy=energy,
        )
