from googleapiclient.discovery import build

from organizador_emails.google_api.api_connection import APIConnection


class ServiceInterface:
    def __init__(self, name, configs):
        self.configs = configs
        self.name_service = name
        self.creds = APIConnection(configs).get_credentials()

    def get_email_service(self):
        return build(
                self.configs.google.services.gmail.name,
                self.configs.google.services.gmail.version,
                credentials=self.creds,
            )