from Code.structured_logging.configuration.logger_config import LoggerConfig
from Code.structured_logging.infrastructure.container import Container
from Code.structured_logging.logger.logger import Logger


def create_logger(logger_config: LoggerConfig) -> Logger:
    container = Container()
    container.config.from_value(logger_config)
    return container.logger()
