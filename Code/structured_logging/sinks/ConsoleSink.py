from json import dumps, json

class ConsoleSink():
    def print_json(self, dictionary):
        dict_to_json = json.dumps(dictionary)
        print(dict_to_json)