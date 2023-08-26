import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


from organizador_emails.utils.date_parser import DateParser

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class APIConnection:
    def __init__(self, configs):
        self.creds = None
        self.configs = configs

    def get_credentials(self):
        path_keys = self.configs.paths.keys
        token_path = self.configs.google.token_file
        credentials_path = self.configs.google.credentials_file

        if os.path.exists(f'{path_keys}/{token_path}'):
            self.creds = Credentials.from_authorized_user_file(
                f'{path_keys}/{token_path}', SCOPES
            )

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    f'{path_keys}/{credentials_path}', SCOPES
                )
                self.creds = flow.run_local_server(port=0)

            with open(f'{path_keys}/{token_path}', 'w') as token:
                token.write(self.creds.to_json())

        return self.creds
