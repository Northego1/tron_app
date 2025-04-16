import httpx


class HttpClient:
    def __init__(self) -> None:
        self.client: httpx.AsyncClient

    def create(self) -> httpx.AsyncClient:
        self.client = httpx.AsyncClient()
        return self.client

    async def aclose(self) -> None:
        if hasattr(self, "_client"):
            await self.client.aclose()
