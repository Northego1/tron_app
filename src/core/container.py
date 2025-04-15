from dependency_injector import containers, providers

from core.config import config
from core.database import DataBase
from core.http_client import HttpClient
from core.uow import UnitOfWork
from tron_app.application.container import ApplicationContainer
from tron_app.infrastructure.container import InfrastructureContainer


class Container(containers.DeclarativeContainer):
    """Main application container."""

    wiring_config = containers.WiringConfiguration(packages=[
        "tron_app.presentation.api.v1",
    ])



    http_client: providers.Singleton[HttpClient] = providers.Singleton(
        HttpClient,
    )
    db: providers.Singleton[DataBase] = providers.Singleton(
        DataBase,
        dsn=config.db.dsn,
    )
    uow: providers.Singleton[UnitOfWork] = providers.Singleton(
        UnitOfWork,
        db=db,
    )

    infrastructure_container = providers.Container(
        InfrastructureContainer,
        http_client=http_client,
    )

    application_container = providers.Container(
        ApplicationContainer,
        infra_container=infrastructure_container,
        uow=uow,
    )
