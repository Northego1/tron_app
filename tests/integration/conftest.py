from typing import AsyncGenerator

import pytest
import pytest_asyncio
from dependency_injector import providers
from httpx import ASGITransport, AsyncClient

from core.config import Config
from core.container import Container
from core.database import Base
from main import app


@pytest.fixture(scope="function")
def container() -> Container:
    container = Container()
    container.config.override(  # type: ignore
        providers.Singleton(
            Config,
            prod_type="TEST",
        ),
    )
    container.init_resources() # type: ignore
    container.wire(packages=["tron_app.presentation.api.v1"])

    return container


@pytest_asyncio.fixture(scope="function")
async def lifespan(container: Container) -> AsyncGenerator[None, None]:
    client = container.http_client()
    client.create()
    yield
    await client.aclose()


@pytest_asyncio.fixture(scope="function")
async def setup_db(container: Container) -> AsyncGenerator[None, None]:
    database = container.db()
    if database.config.app.PROD != "TEST":
        raise Exception("Database is not in test mode")
    else:
        async with database.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        yield
        async with database.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def client(setup_db: None, lifespan: None) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac





