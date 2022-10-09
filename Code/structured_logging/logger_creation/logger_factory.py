from Code.structured_logging.configuration.logger_config import LoggerConfig
from Code.structured_logging.infrastructure.container import Container
from Code.structured_logging.logger.logger import Logger


def create_logger(logger_config: LoggerConfig) -> Logger:
    container = Container()
    # smá jank en að nota from_value virkar ekki, síðan þarf að passa alvöru config dict áfram svo það er sent með.
    # frekar jank aftur en það virkar og er ekki allt of heimskt. 
    config_dict = logger_config.dict()
    config_dict["config_object"] = logger_config
    
    container.config.from_dict(config_dict)
    return container.logger()
