from typing import Any, Iterable
from Code.structured_logging.command_queue.queue import Queue
from Code.structured_logging.configuration.logger_config import LoggerConfig
from Code.structured_logging.logger.logging_command import LoggingCommand

class Logger:
    def __init__(self, logger_config: LoggerConfig, logging_queue: Queue):
        self.__logger_config = logger_config
        self.__logging_queue = logging_queue

    def log(self, **kwargs: Iterable[Any]):
        data = kwargs.copy()
        self.__logger_config.processor.handle(data)
        command = LoggingCommand(data,LoggerConfig.sink)
        if self.__logger_config.is_async:
            self.__logging_queue.add(command)
        else:
            command.execute()
