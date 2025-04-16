import pytest
from dependency_injector import providers
from unit.mocks.mocks_infrasturcture.mock_gateway import MockTronApiGateway

from core.container import Container
from tests.unit.mocks.shared_data import make_wallet
from tron_app.application.usecases.post_query_usecase import GetWalletUsecase
from tron_app.domain.entities.wallet import Wallet


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("address", "expected", "exception"),
    [
        (
            "TCRctCvEse9Y6E6i5DaTjkaSwyKRe6QQP8",
            make_wallet(),
            None,
        ),
    ],
)
async def test_post_query_usecase(
        address: str,
        expected: Wallet,
        exception: type[Exception] | None,
        container: Container,
) -> None:
    container.application_container.post_query_uc.override(                    # type: ignore
        providers.Factory(
            GetWalletUsecase,
            tron_api_gateway=MockTronApiGateway,
        ),
    )

    post_query_uc: GetWalletUsecase = (                                       # type: ignore
        container.application_container.post_query_uc()                        # type: ignore
    )

    if exception:
        with pytest.raises(exception):
            await post_query_uc.execute(address=address)                   # type: ignore
    else:
        result = await post_query_uc.execute(address=address)              # type: ignore
        assert result == expected
