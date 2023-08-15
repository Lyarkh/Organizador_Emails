from organizador_emails.google_api.connection import ConnectGoogleAPI


class Main:
    @staticmethod
    def main(configs):
        google_api = ConnectGoogleAPI(configs)
        google_api.get_credentials()
        all_messages = google_api.get_messages_list([], '')
        print(f'Quantidade de mensagens encontradas: {len(all_messages)}')

        import json

        with open('results.json') as file:
            json.dump(all_messages, file, indent=4)


if __name__ == '__main__':
    Main.main()
