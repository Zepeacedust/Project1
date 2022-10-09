from dependency_injector import containers, providers
from Code.structured_logging.command_queue.queue import Queue

from Code.structured_logging.logger.logger import Logger

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    queue = providers.Selector(config.is_async,
                               true=providers.Factory(Queue, config.async_wait_delay_in_seconds),
                               false=providers.Object(None)
                               )
    logger = providers.Singleton(Logger,config.config_object, queue)

