from dependency_injector import containers, providers

from core.config import config
from core.database import DataBase
from core.uow import UnitOfWork
from tron_app.application.container import ApplicationContainer
from tron_app.infrastructure.container import InfrastructureContainer


class Container(containers.DeclarativeContainer):
    """Main application container."""

    wiring_config = containers.WiringConfiguration(packages=[
        "tron_app.presentation.api.v1",
    ])


    db: providers.Singleton[DataBase] = providers.Singleton(
        DataBase,
        dsn=config.db.dsn,
    )
    uow: providers.Singleton[UnitOfWork] = providers.Singleton(
        UnitOfWork,
        db=db,
    )

    # application_container = providers.Container(
    #     ApplicationContainer,
    #     uow=uow,
    # )

    # infrastructure_container = providers.Container(
    #     InfrastructureContainer,
    # )
