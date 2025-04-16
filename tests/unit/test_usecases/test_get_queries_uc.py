import pytest
from dependency_injector import providers
from unit.mocks.mocks_infrasturcture.mock_uow import uow_mock

from core.container import Container
from tests.unit.mocks.shared_data import make_wallet_query
from tron_app.application.dto import Paginator
from tron_app.application.usecases.get_queries_usecase import GetQueriesUsecase
from tron_app.domain.entities.wallet_query import WalletQuery


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("paginator", "expected", "exception"),
    [
        (
            Paginator(limit=10, offset=0),
            [make_wallet_query() for _ in range(10)],
            None,
        ),
    ],
)
async def test_get_queries_usecase(
    paginator: Paginator,
    expected: list[WalletQuery],
    exception: type[Exception] | None,
    container: Container,
) -> None:
    container.application_container.get_queries_uc.override(  # type: ignore
        providers.Factory(
            GetQueriesUsecase,
            uow=uow_mock,
        ),
    )

    get_queries_uc: GetQueriesUsecase = (  # type: ignore
        container.application_container.get_queries_uc()  # type: ignore
    )

    if exception:
        with pytest.raises(exception):
            await get_queries_uc.execute(paginator=paginator)  # type: ignore
    else:
        result = await get_queries_uc.execute(paginator=paginator)  # type: ignore
        assert result == expected
