from Code.structured_logging.processors.I_processor import IProcessor
from abc import abstractmethod
class AbstractProcessor(IProcessor):
    def set_next(self, processor: IProcessor) -> IProcessor:
        self._next_processor = processor
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return processor
    @abstractmethod
    def handle(self, request) -> str:
        if self._next_processor:
            return self._next_processor.handle(request)
        return None