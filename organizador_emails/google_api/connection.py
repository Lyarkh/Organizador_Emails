import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from organizador_emails.utils.date_parser import DateParser


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class ConnectGoogleAPI:
    def __init__(self, configs):
        self.creds = None
        self.configs = configs

    def get_credentials(self):
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        path_keys = self.configs.paths.keys
        token_path = self.configs.google.token_file
        credentials_path = self.configs.google.credentials_file

        if os.path.exists(f'{path_keys}/{token_path}'):
            self.creds = Credentials.from_authorized_user_file(
                f'{path_keys}/{token_path}', SCOPES
            )

        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    f'{path_keys}/{credentials_path}', SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(f'{path_keys}/{token_path}', 'w') as token:
                token.write(self.creds.to_json())

    def get_service(self):
        return build(self.configs.google.service.name, self.configs.google.service.version, credentials=self.creds)

    def get_labels(self):
        try:
            # Call the Gmail API
            service = self.get_service()
            results = service.users().labels().list(userId='me').execute()
            labels = results.get('labels', [])

            if not labels:
                print('No labels found.')
                return
            print('Labels:')
            for label in labels:
                print(label['name'])

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f'An error occurred: {error}')

    def get_messages_list(self, page_token):
        service = self.get_service()
        messages = service.users().messages().list(userId='me', pageToken=page_token).execute()


        result = messages['messages']
        new_page_token = messages.get('nextPageToken', '')

        return result, new_page_token

    def get_info_message(self, message_id):
        service = self.get_service()
        message = service.users().messages().get(userId='me', id=message_id).execute()
        self.get_headers_info(message)

        return message

    def get_headers_info(self, message):
        header_info = message['payload']['headers']

        labels =  message['labelIds']
        message_snippet = message['snippet']

        user_from = 'User Send - Not Found'
        date = 'Date - Not Found'
        subject = 'Subject - Not Found'

        for info in header_info:
            if info['name'] == 'From':
                user_from = info['value']
            if info['name'] == 'Date':
                date_parser = DateParser(info['value'])
                date = date_parser.date
            if info['name'] == 'Subject':
                subject = info['value']

        print(
            '\n------------------\n'
            f'From: {user_from}\n'
            f'Labels: {labels}\n'
            f'Date: {date}\n'
            f'Subject: {subject}\n'
            f'Snippet: {message_snippet}\n'
            '------------------'
        )
