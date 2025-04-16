import pytest
from httpx import AsyncClient



@pytest.mark.asyncio
async def test_get_wallet_queries(
    client: AsyncClient,
) -> None:
    response = await client.get("/api/v1/wallet/queries/?limit=10&offset=0")
    assert response.status_code == 200



@pytest.mark.asyncio
async def test_post_wallet_queries(
    client: AsyncClient,
) -> None:
    response = await client.post(
        "/api/v1/wallet/queries/?limit=10&offset=0",
        json={"address": "TCRctCvEse9Y6E6i5DaTjkaSwyKRe6QQP8"},
    )
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_post_get_wallet(
    client: AsyncClient,
) -> None:
    await client.post(
        "/api/v1/wallet/queries/?limit=10&offset=0",
        json={"address": "TCRctCvEse9Y6E6i5DaTjkaSwyKRe6QQP8"},
    )

    response = await client.get("/api/v1/wallet/queries/?limit=10&offset=0")
    resp_data = response.json()
    assert len(resp_data["items"]) == 1
