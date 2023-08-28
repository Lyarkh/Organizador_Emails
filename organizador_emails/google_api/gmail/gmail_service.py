from organizador_emails.google_api.api_connection import APIConnection
from googleapiclient.discovery import build


class GmailService:
    def __init__(self, configs):
        self.configs = configs
        self.creds = APIConnection(configs).get_credentials()

    def build(self):
        return build(
            self.configs.google.services.gmail.name,
            self.configs.google.services.gmail.version,
            credentials=self.creds,
        )
