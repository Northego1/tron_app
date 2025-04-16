import pytest
from dependency_injector import providers
from unit.mocks.mocks_infrasturcture.mock_uow import uow_mock

from core.container import Container
from tests.unit.mocks.shared_data import make_query_dto
from tron_app.application.dto import QueryDto
from tron_app.application.usecases.create_query_usecase import CreateQueryUsecase
from tron_app.domain.entities.wallet_query import WalletQuery


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("query_dto", "expected", "exception"),
    [
        (
            make_query_dto(),
            None,
            None,
        ),
    ],
)
async def test_create_query_uc(
        query_dto: QueryDto,
        expected: list[WalletQuery],
        exception: type[Exception] | None,
        container: Container,
) -> None:
    container.application_container.create_query_uc.override(                    # type: ignore
        providers.Factory(
            CreateQueryUsecase,
            uow=uow_mock,
        ),
    )

    create_query_uc: CreateQueryUsecase = (                                       # type: ignore
        container.application_container.create_query_uc()                        # type: ignore
    )

    if exception:
        with pytest.raises(exception):
            await create_query_uc.execute(query_dto=query_dto)                   # type: ignore
    else:
        result = await create_query_uc.execute(query_dto=query_dto)              # type: ignore
        assert result == expected
