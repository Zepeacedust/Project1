from dependency_injector import containers, providers
from Code.client.infrastructure.logging.logger_config_factory import create_logger_config
from Code.client.infrastructure.settings.settings import Settings
from Code.structured_logging.logger.logger import Logger
from Code.structured_logging.logger_creation.logger_factory import create_logger
from Code.client.infrastructure.logging.structured_logger import StucturedLogger
from Code.client.services.order_service import OrderService
from Code.client.services.payment_service_stub import PaymentServiceStub
from Code.client.repositories.order_repository import OrderRepository


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()

    # NOTE: we are recreating the settings object here because dependency injection in python is bit dense in passing the configuration
    external_logger: Logger = providers.Object(
        create_logger(create_logger_config(Settings())))

    internal_logger = providers.Singleton(StucturedLogger, external_logger)
    
    payment_service_stub = providers.Singleton(PaymentServiceStub,True, internal_logger)
    
    order_repo = providers.Singleton(OrderRepository, config.order_file_path)

    order_service = providers.Factory(OrderService, payment_service_stub, order_repo, internal_logger)