from organizador_emails.google_api.service_interface import ServiceInterface
from organizador_emails.google_api.gmail.functions.get_messages import Getmessages

class Main:
    @staticmethod
    def main(configs):
        google_api = ServiceInterface(configs).get_email_service()

        all_id_messages = []
        all_messages = []
        page_token = ''

        MAX = 1000

        while True:
            find_messages, next_token = Getmessages().get_messages_list(google_api, page_token)
            all_id_messages.extend(find_messages)
            page_token = next_token
            print(
                f'Quantidade de mensagens encontradas: {len(all_id_messages)}'
            )

            if len(all_id_messages) >= MAX:
                break

            if not page_token:
                break

        for message in all_id_messages:
            print(f"Buscando info da message com id: {message['id']}")
            message_info = Getmessages().get_info_message(google_api, message['id'])
            all_messages.append(message_info)

        return all_messages


if __name__ == '__main__':
    all_messages = Main.main()

    import json

    with open('results.json', mode='w') as file:
        json.dump(all_messages, file, indent=4)
