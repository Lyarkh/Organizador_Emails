from organizador_emails.google_api.connection import ConnectGoogleAPI


class Main:
    @staticmethod
    def main(configs):
        google_api = ConnectGoogleAPI(configs)
        google_api.get_credentials()

        all_id_messages = []
        all_messages = []
        page_token = ''

        while True:
            find_messages, next_token = google_api.get_messages_list(page_token)
            all_id_messages.extend(find_messages)
            page_token = next_token
            print(f'Quantidade de mensagens encontradas: {len(all_id_messages)}')
            if not page_token:
                break

        for message in all_id_messages:
            print(f"Buscando info da message com id: {message['id']}")
            message_info = google_api.get_info_message(message['id'])
            all_messages.append(message_info)

        return all_messages


if __name__ == '__main__':
    all_messages = Main.main()

    import json

    with open('results.json', mode='w') as file:
        json.dump(all_messages, file, indent=4)
