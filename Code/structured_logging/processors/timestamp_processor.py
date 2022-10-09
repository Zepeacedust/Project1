from Code.structured_logging.processors.abstract_processor import AbstractProcessor
from datetime import datetime
class TimestampProcessor(AbstractProcessor):
    def handle(self, data: dict):
        data["timestamp"] = str(datetime.now())
        return super().handle(data)