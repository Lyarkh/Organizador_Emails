from googleapiclient.discovery import build

from organizador_emails.google_api.api_connection import APIConnection
from organizador_emails.models.base_service import BaseService


class GmailService(BaseService):
    def __init__(self, configs):
        self.configs = configs
        self.creds = APIConnection(self.configs).get_credentials()

    @property
    def build(self):
        return build(
            self.configs.google.services.gmail.name,
            self.configs.google.services.gmail.version,
            credentials=self.creds,
        )
