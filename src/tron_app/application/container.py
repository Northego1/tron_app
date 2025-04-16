from dependency_injector import containers, providers

from tron_app.application.usecases.create_query_usecase import CreateQueryUsecase
from tron_app.application.usecases.get_queries_usecase import GetQueriesUsecase
from tron_app.application.usecases.post_query_usecase import GetWalletUsecase


class ApplicationContainer(containers.DeclarativeContainer):
    infra_container = providers.DependenciesContainer()
    uow: providers.Dependency = providers.Dependency()  # type: ignore

    create_query_uc: providers.Factory[CreateQueryUsecase] = providers.Factory(
        CreateQueryUsecase,
        uow=uow,
    )

    get_queries_uc: providers.Factory[GetQueriesUsecase] = providers.Factory(
        GetQueriesUsecase,
        uow=uow,
    )

    post_query_uc: providers.Factory[GetWalletUsecase] = providers.Factory(
        GetWalletUsecase,
        tron_api_gateway=infra_container.tron_gateway,  # type: ignore
    )
