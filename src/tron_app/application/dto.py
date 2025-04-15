from datetime import datetime
from uuid import UUID


class QueryDto:
    id: UUID
    tron_address: str
    query_time: datetime
