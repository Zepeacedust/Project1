from Code.structured_logging.processors.I_processor import IProcessor
from pydantic import (BaseSettings)
from Code.structured_logging.sinks.I_sink import ISink


class LoggerConfig(BaseSettings):
    sink: ISink
    processor: IProcessor
    is_async: str
    async_wait_delay_in_seconds: int
    def get():
        pass
