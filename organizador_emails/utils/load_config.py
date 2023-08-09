import os
import sys
import yaml

from organizador_emails.models.config import Config


class LoadConfig:
    def __init__(self):
        self.add_project_path()
        self.get_all_configs()

    def add_project_path(self):
        sys.path.insert(0, os.getcwd())

    def get_all_configs(self):
        yaml_config = self.open_yaml_file()
        config_obj = Config(yaml_config)

        return config_obj

    def open_yaml_file(self):
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)


if __name__ == '__main__':
    LoadConfig()
