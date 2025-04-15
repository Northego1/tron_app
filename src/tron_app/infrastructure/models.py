import uuid
from datetime import datetime

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import UUID, DateTime, String

from core.database import Base
from tron_app.domain.entities.wallet_query import QueryStatus


class WalletQueryModel(Base):
    __tablename__ = "wallet_queries"


    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    tron_address: Mapped[str] = mapped_column(String, nullable=False)
    query_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[QueryStatus] = mapped_column(
        Enum(QueryStatus, native_enum=True),
        nullable=False,
    )
