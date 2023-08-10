import yaml

from organizador_emails.models.config import Config


class LoadConfig:
    def __init__(self):
        self.configs = self.get_all_configs()

    @property
    def get_variables(self):
        return self.configs

    def get_all_configs(self):
        yaml_config = self.open_yaml_file()
        config_obj = Config(yaml_config)

        return config_obj

    def open_yaml_file(self):
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)


if __name__ == '__main__':
    LoadConfig()
