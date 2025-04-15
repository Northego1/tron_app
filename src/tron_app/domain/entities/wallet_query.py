import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class QueryStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


@dataclass(slots=True)
class WalletQuery:
    tron_address: str
    query_time: datetime
    status: QueryStatus
    id: uuid.UUID = field(default_factory=uuid.uuid4)



