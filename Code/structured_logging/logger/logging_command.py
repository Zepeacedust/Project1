from Code.structured_logging.command_queue.command import Command
from Code.structured_logging.sinks.I_sink import ISink

class LoggingCommand(Command):
    def __init__(self, data, sink:ISink):
        self.data = data
        self.sink = sink
    def execute(self):
        self.sink.sink_data(self.data)