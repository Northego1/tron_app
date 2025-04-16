from dataclasses import asdict
from datetime import UTC, datetime

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Query

from core.container import Container
from core.logger import get_logger
from tron_app.application.dto import Paginator, QueryDto
from tron_app.application.exceptions import ApplicationError
from tron_app.domain.entities.wallet_query import QueryStatus
from tron_app.infrastructure.exception import InfrastructureError
from tron_app.presentation.api.v1 import protocols as proto
from tron_app.presentation.api.v1.schemas import requests, responses

log = get_logger(__name__)

router = APIRouter(prefix="/wallet/queries")


@router.get("/", status_code=200)
@inject
async def get_queries(
        paginator: Paginator = Query(),
        get_queries_uc: proto.GetQueriesUsecase = Depends(
            Provide[Container.application_container.get_queries_uc], # type: ignore
        ),
) -> responses.WalletQueriesResponse:
    try:
        queries = await get_queries_uc.execute(paginator=paginator)
        return responses.WalletQueriesResponse(
            items=[
                responses.WalletQueryResponse(**asdict(query)) for query in queries
            ],
            total=len(queries),
        )
    except (ApplicationError, InfrastructureError) as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail,
        ) from e



@router.post("/", status_code=201)
@inject
async def post_query(
        address: requests.PostTronRequest,
        post_query_uc: proto.GetWalletUsecaseProtocol = Depends(
            Provide[Container.application_container.post_query_uc], # type: ignore
        ),
        create_query_uc: proto.CreateQueryUsecaseProtocol = Depends(
            Provide[Container.application_container.create_query_uc], # type: ignore
        ),
) -> responses.WalletResponse:
    try:
        status = QueryStatus.FAILURE
        log.debug("Calling usecase to get wallet by address: %s", address)
        wallet = await post_query_uc.execute(address=address.address)
        log.debug("Successful got wallet by address: %s", address)
        status = QueryStatus.SUCCESS

        return responses.WalletResponse(
            balance_trx=wallet.balance_trx,
            bandwidth=wallet.bandwidth,
            energy=wallet.energy,
        )
    except (ApplicationError, InfrastructureError)as e:
        log.debug("Failure got wallet by address: %s", address)
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail,
        ) from e
    finally:
        log.debug("Calling usecase to record query by address: %s", address)
        await create_query_uc.execute(
            QueryDto(
                status=status, # type: ignore
                tron_address=address.address,
                query_time=datetime.now(UTC),
            ),
        )
