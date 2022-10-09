from Code.client.infrastructure.settings.settings import Settings
from Code.structured_logging.configuration.logger_config import LoggerConfig


def create_logger_config(settings: Settings) -> LoggerConfig:
    raise NotImplementedError()
