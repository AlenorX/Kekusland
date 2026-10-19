import yaml

class YAML():
    def __init__(self):
        pass

    def decode(self, path_file: str) -> dict:
        with open(path_file, 'r+') as file:
            return yaml.safe_load(file)