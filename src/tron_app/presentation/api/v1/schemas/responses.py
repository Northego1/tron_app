from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from tron_app.domain.entities.wallet_query import QueryStatus


class WalletQueryResponse(BaseModel):
    id: UUID
    tron_address: str = Field(examples=["TWd413qHSXZ9ryAZUkk1A5j3PScT7jfahE"])
    query_time: datetime
    status: QueryStatus


class WalletQueriesResponse(BaseModel):
    items: list[WalletQueryResponse]
    total: int


class WalletResponse(BaseModel):
    balance_trx: float
    bandwidth: int
    energy: int
