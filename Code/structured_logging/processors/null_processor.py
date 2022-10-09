from abstract_processor import AbstractProcessor

class NullProcessor(AbstractProcessor):
    def handle(self,data):
        if self._next_processor != None:
            self._next_processor
        else:
            return None