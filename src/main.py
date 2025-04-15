from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI

from core.container import Container
from core.logger import get_logger
from tron_app.presentation import api

log = get_logger(__name__)

@asynccontextmanager
async def _lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    yield


def create_app() -> FastAPI:
    """Create a FastAPI application instance."""
    log.debug("creating fastapi app")
    app = FastAPI(title="SecretApp", lifespan=_lifespan)
    app.include_router(api.router)

    log.debug("initing dependency container")
    container = Container()
    container.init_resources()  # type: ignore
    app.state.container = container
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)