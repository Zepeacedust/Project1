from dependency_injector import containers, providers
from Code.client.infrastructure.logging.logger_config_factory import create_logger_config
from Code.client.infrastructure.settings.settings import Settings
from Code.structured_logging.logger.logger import Logger
from Code.structured_logging.logger_creation.logger_factory import create_logger


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()

    # NOTE: we are recreating the settings object here because dependency injection in python is bit dense in passing the configuration
    external_logger: Logger = providers.Object(
        create_logger(create_logger_config(Settings())))

    raise NotImplementedError()
