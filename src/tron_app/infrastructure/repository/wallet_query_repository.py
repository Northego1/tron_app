from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tron_app.domain.entities.wallet_query import WalletQuery
from tron_app.infrastructure.models import WalletQueryModel


class WalletQueryRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session


    async def add(self, wallet_query: WalletQuery) -> None:
        wallet_model = WalletQueryModel(
            id=wallet_query.id,
            tron_address=wallet_query.tron_address,
            query_time=wallet_query.query_time,
            status=wallet_query.status,
        )
        self.session.add(wallet_model)


    async def get_all(self, limit: int, offset: int) -> list[WalletQuery]:
        query = (
            select(WalletQueryModel)
            .offset(offset)
            .limit(limit)
        )

        result = await self.session.execute(query)
        rows = result.scalars().all()

        return [
            WalletQuery(
                id=row.id,
                tron_address=row.tron_address,
                query_time=row.query_time,
                status=row.status,
            ) for row in rows
        ]


