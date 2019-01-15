import json


class JsonFileReader:

    @staticmethod
    def _get_json(json_file_path):
        with open(json_file_path, 'r') as f:
            return json.load(f)
