import uuid
from datetime import UTC, datetime

from tron_app.application.dto import QueryDto
from tron_app.domain.entities.wallet import Wallet
from tron_app.domain.entities.wallet_query import QueryStatus, WalletQuery


def make_wallet_query() -> WalletQuery:
    return WalletQuery(
        id=uuid.UUID("27a28779-2042-4b46-b8aa-f4a99cf0fcc6"),
        query_time=datetime(tzinfo=UTC, year=2025, month=1, day=1),
        status=QueryStatus.SUCCESS,
        tron_address="TCRctCvEse9Y6E6i5DaTjkaSwyKRe6QQP8",
    )

def make_query_dto() -> QueryDto:
    return QueryDto(
        status=QueryStatus.SUCCESS,
        tron_address="TCRctCvEse9Y6E6i5DaTjkaSwyKRe6QQP8",
        query_time=datetime(tzinfo=UTC, year=2025, month=1, day=1),
    )


def make_wallet() -> Wallet:
    return Wallet(
        address="TCRctCvEse9Y6E6i5DaTjkaSwyKRe6QQP8",
        balance_trx=100,
        bandwidth=250,
        energy=250,
    )
