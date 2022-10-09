from Code.client.infrastructure.logging.I_logger import ILogger
from Code.structured_logging.logger.logger import Logger
class StucturedLogger(ILogger):
    def __init__(self, logger:Logger) -> None:
        self.logger = logger
    
    def error(self, message: str, exception: Exception = None):
        self.logger.log(type="ERROR",message=message, exception = exception)

    def warning(self, message: str, exception: Exception = None):
        self.logger.log(type="WARNING",message=message, exception = exception)
        
    def info(self, message: str):
        self.logger.log(type="INFO",message=message)
