from organizador_emails.google_api.gmail.gmail_service import GmailService


class ServiceInterface:
    @staticmethod
    def get_email_service(configs):
        return GmailService(configs).build()
