from abstract_processor import AbstractProcessor

class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, environment):
        self.environment = environment
    def handle(self, data: dict):
        data["environment"] = self.environment
        return super().handle(data)