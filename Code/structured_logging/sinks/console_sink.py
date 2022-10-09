import json
from Code.structured_logging.sinks.I_sink import ISink

class ConsoleSink(ISink):
    def sink_data(self, dictionary):
        dict_to_json = json.dumps(dictionary)
        print(dict_to_json)