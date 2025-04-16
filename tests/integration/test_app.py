import pytest
from dependency_injector import providers
from httpx import AsyncClient
from integration.mock import http_mock

from core.container import Container
from tron_app.infrastructure.gateway.tron_api_gateway import TronApiGateway
from tron_app.presentation.api.v1.schemas import responses


@pytest.mark.asyncio
async def test_get_wallet_queries(
    client: AsyncClient,
) -> None:
    response = await client.get("/api/v1/wallet/queries/?limit=10&offset=0")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_wallet_queries(
    container: Container,
    client: AsyncClient,
) -> None:
    container.infrastructure_container.tron_gateway.override(  # type: ignore
        providers.Factory(
            TronApiGateway,
            http_client=http_mock,
            config=container.config,
        ),
    )

    post_resp = await client.post(
        "/api/v1/wallet/queries/",
        json={"address": "TCRctCvEse9Y6E6i5DaTjkaSwyKRe6QQP8"},
    )
    get_resp = await client.get("/api/v1/wallet/queries/?limit=10&offset=0")
    resp_data = get_resp.json()

    assert len(resp_data["items"]) == 1
    assert (
        post_resp.json()
        == responses.WalletResponse(
            balance_trx=666,
            energy=666,
            bandwidth=666,
        ).model_dump()
    )
