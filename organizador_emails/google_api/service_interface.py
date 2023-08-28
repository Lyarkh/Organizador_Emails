from organizador_emails.google_api.gmail.gmail_service import GmailService


class ServiceInterface:
    def __init__(self, configs):
        self.configs = configs


    def get_email_service(self):
        return GmailService().build()
