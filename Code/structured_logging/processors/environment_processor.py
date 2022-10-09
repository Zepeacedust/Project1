from Code.structured_logging.processors.abstract_processor import AbstractProcessor

class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, environment):
        self.environment = environment
    def handle(self, data: dict):
        data["environment"] = str(self.environment)
        return super().handle(data)