from dependency_injector import containers, providers

from core.config import Config
from core.database import DataBase
from core.http_client import HttpClient
from core.uow import Repository, UnitOfWork
from tron_app.application.container import ApplicationContainer
from tron_app.infrastructure.container import InfrastructureContainer


class Container(containers.DeclarativeContainer):
    """Main application container."""

    wiring_config = containers.WiringConfiguration(
        packages=[
            "tron_app.presentation.api.v1",
        ],
    )

    config: providers.Singleton[Config] = providers.Singleton(Config, prod_type="DEV")

    http_client: providers.Singleton[HttpClient] = providers.Singleton(
        HttpClient,
    )
    db: providers.Singleton[DataBase] = providers.Singleton(
        DataBase,
        config=config,
    )
    uow: providers.Singleton[UnitOfWork] = providers.Singleton(
        UnitOfWork,
        db=db,
        repository=providers.Factory(
            lambda: Repository,
        ),
    )

    infrastructure_container = providers.Container(
        InfrastructureContainer,
        http_client=http_client,
        config=config,
    )

    application_container = providers.Container(
        ApplicationContainer,
        infra_container=infrastructure_container,
        uow=uow,
    )
