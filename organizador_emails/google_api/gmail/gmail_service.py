from googleapiclient.discovery import build


class GmailService:
    def build(self):
        return build(
            self.configs.google.services.gmail.name,
            self.configs.google.services.gmail.version,
            credentials=self.creds,
        )
