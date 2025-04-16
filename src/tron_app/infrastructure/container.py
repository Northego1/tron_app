from dependency_injector import containers, providers

from tron_app.infrastructure.gateway.tron_api_gateway import TronApiGateway


class InfrastructureContainer(containers.DeclarativeContainer):
    http_client: providers.Dependency = providers.Dependency()  # type: ignore
    config: providers.Dependency = providers.Dependency()  # type: ignore

    tron_gateway: providers.Factory[TronApiGateway] = providers.Factory(
        TronApiGateway,
        http_client=http_client,
        config=config,
    )
