import os, sys
import yaml


class LoadConfig:
    def __init__(self):
        self.add_project_path()

    def add_project_path(self):
        sys.path.insert(0, os.getcwd())

    def run(self):
        yaml_config = self.open_yaml_file()

        return yaml_config

    def open_yaml_file(self):
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)


if __name__ == '__main__':
    LoadConfig().run()
