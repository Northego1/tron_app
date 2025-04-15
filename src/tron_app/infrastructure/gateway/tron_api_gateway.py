import base58

from core.config import config
from core.exceptions import AppError
from core.http_client import HttpClient
from core.logger import get_logger
from tron_app.domain.entities.wallet import Wallet

log = get_logger(__name__)


class TronApiGateway:
    def __init__(
            self,
            http_client: HttpClient,
    ) -> None:
        self.client = http_client.client


    async def get_wallet(self, address: str) -> Wallet:
        # ________Баланс________
        log.debug("Sending account request to TRON_API by address: %s", address)
        acc_resp = await self.client.get(f"{config.tron.API_DOMAIN}/v1/accounts/{address}")
        acc_data = acc_resp.json()
        if "data" not in acc_data or not acc_data["data"]:
            raise AppError
        trx_balance = acc_data["data"][0].get("balance", 0)

        # ________Ресурсы________
        log.debug("Sending resource request to TRON_API by address: %s", address)
        res_resp = await self.client.post(f"{config.tron.API_DOMAIN}/wallet/getaccountresource", json={
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
