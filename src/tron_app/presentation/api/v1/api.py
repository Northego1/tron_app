from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Query

from tron_app.presentation.api.v1.schemas import requests, responses

router = APIRouter(prefix="/wallet/queries")


@router.get("/", status_code=200)
@inject
async def get_queries(
    paginator: requests.Paginator = Query(),
) -> responses.WalletQueriesResponse:
    ...


@router.post("/", status_code=201)
@inject
async def post_query(
    address: requests.PostTronRequest,
) -> responses.WalletResponse:
    ...
