from Code.structured_logging.processors.I_processor import IProcessor
from abc import abstractmethod
class AbstractProcessor(IProcessor):
    def set_next(self, processor: IProcessor) -> IProcessor:
        self._next_processor = processor
        return processor
    @abstractmethod
    def handle(self, request):
        if self._next_processor:
            return self._next_processor.handle(request)
        return None