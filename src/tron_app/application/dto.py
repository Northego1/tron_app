from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel, Field

from tron_app.domain.entities.wallet_query import QueryStatus


@dataclass(slots=True)
class QueryDto:
    status: QueryStatus
    tron_address: str
    query_time: datetime



class Paginator(BaseModel):
    limit: int = Field(ge=0)
    offset: int = Field(ge=0)
