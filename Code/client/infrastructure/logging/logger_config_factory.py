from Code.client.infrastructure.settings.settings import Settings
from Code.structured_logging.configuration.logger_config import LoggerConfig
from Code.structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder

def create_logger_config(settings: Settings) -> LoggerConfig:
    builder = LoggerConfigBuilder()
    if settings.logging_type == "file":
        builder = builder.with_file_sink(settings.logging_file_path)
    
    if settings.logging_is_async:
        builder = builder.as_async(settings.logging_async_delay)

    builder= builder.add_environment(settings.environment)
    builder= builder.add_timestamp()
    
    return builder.build()