from Code.structured_logging.configuration.environment import Environment
from Code.structured_logging.configuration.logger_config import LoggerConfig
from Code.structured_logging.processors.I_processor import IProcessor
from Code.structured_logging.sinks.I_sink import ISink

from Code.structured_logging.processors.null_processor import NullProcessor
from Code.structured_logging.processors.timestamp_processor import TimestampProcessor
from Code.structured_logging.processors.environment_processor import EnvironmentProcessor

from Code.structured_logging.sinks.console_sink import ConsoleSink
from Code.structured_logging.sinks.file_sink import FileSink


class LoggerConfigBuilder:
    def __init__(self):
        self.sink = ConsoleSink()
        self.processor = NullProcessor()
        self.is_async = False
        self.async_wait_delay_in_seconds = 0

    def with_custom_sink(self, sink: ISink) -> 'LoggerConfigBuilder':
        self.sink = sink
        return self

    def with_file_sink(self, file_path: str) -> 'LoggerConfigBuilder':
        return self.with_custom_sink(FileSink(file_path))

    def with_console_sink(self) -> 'LoggerConfigBuilder':
        return self.with_custom_sink(ConsoleSink())
        
    def as_async(self, wait_delay_in_seconds: int) -> 'LoggerConfigBuilder':
        self.is_async = True
        self.async_wait_delay_in_seconds = wait_delay_in_seconds
        return self
    
    def add_environment(self, environment: Environment) -> 'LoggerConfigBuilder':
        return self.add_processor(EnvironmentProcessor(environment))
    
    def add_timestamp(self):
        return self.add_processor(TimestampProcessor)

    def add_processor(self, processor: IProcessor) -> 'LoggerConfigBuilder':
        new_processeor = processor
        new_processeor.set_next(self.processor)
        self.processor=new_processeor
        return self

    def _clear(self):
        self.sink = ConsoleSink()
        self.processor = NullProcessor()
        self.is_async = False
        self.async_wait_delay_in_seconds = 0
        return self

    def build(self) -> LoggerConfig:
        return LoggerConfig(sink = self.sink, 
                            processor=self.processor,
                            is_async=self.is_async,
                            async_wait_delay_in_seconds=self.async_wait_delay_in_seconds)
