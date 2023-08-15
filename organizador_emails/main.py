from organizador_emails.google_api.connection import ConnectGoogleAPI


class Main:
    @staticmethod
    def main(configs):
        google_api = ConnectGoogleAPI(configs)
        google_api.get_credentials()
        google_api.get_messages_list('')


if __name__ == '__main__':
    Main.main()
