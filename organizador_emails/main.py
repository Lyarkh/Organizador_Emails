from organizador_emails.google_api.connection import ConnectGoogleAPI


class Main:
    @staticmethod
    def main(configs):
        google_api = ConnectGoogleAPI(configs)
        google_api.get_credentials()

        all_messages = []
        page_token = ''

        while True:
            find_messages, next_token = google_api.get_messages_list(page_token)
            all_messages.extend(find_messages)
            page_token = next_token
            print(f'Quantidade de mensagens encontradas: {len(all_messages)}')
            print(f'Próximo token:  {page_token}')
            if not page_token:
                break

        import json

        with open('results.json', mode='w') as file:
            json.dump(all_messages, file, indent=4)


if __name__ == '__main__':
    Main.main()
