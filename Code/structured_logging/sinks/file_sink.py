from Code.structured_logging.sinks.I_sink import ISink
import json

class FileSink(ISink):
    def __init__(self, file_path:str) -> None:
        super().__init__()
        self.file = open(file_path, "a")
    
    def sink_data(self, data: dict):
        json.dump(data, self.file)
    
    def __del__(self):
        self.file.close()