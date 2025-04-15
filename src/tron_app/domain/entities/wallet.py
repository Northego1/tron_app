from dataclasses import dataclass


@dataclass(slots=True)
class Wallet:
    address: str
    balance_trx: float
    bandwidth: int
    energy: int
