from googleapiclient.errors import HttpError

from organizador_emails.google_api.service_interface import ServiceInterface


class GetLabels:
    def __init__(self, service):
        self.service = service

    def run(self):
        try:
            results = self.service.users().labels().list(userId='me').execute()
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
