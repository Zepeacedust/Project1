from Code.structured_logging.processors.I_processor import IProcessor
from abc import abstractmethod
class AbstractProcessor(IProcessor):
    _next_processor = None
    def set_next(self, processor: IProcessor) -> IProcessor:
        self._next_processor = processor
        return processor
    @abstractmethod
    def handle(self, data: dict):
        if self._next_processor:
            return self._next_processor.handle(data)
        return None