from organizador_emails.utils.date_parser import DateParser


class Getmessages:
    def get_messages_list(self, service, page_token):
        service = service
        messages = (
            service.users()
            .messages()
            .list(userId='me', pageToken=page_token)
            .execute()
        )

        result = messages['messages']
        new_page_token = messages.get('nextPageToken', '')

        return result, new_page_token

    def get_info_message(self, service, message_id):
        service = service
        message = (
            service.users()
            .messages()
            .get(userId='me', id=message_id)
            .execute()
        )
        self.get_headers_info(message)

        return message

    def get_headers_info(self, message):
        header_info = message['payload']['headers']

        labels = message['labelIds']
        message_snippet = message['snippet']

        user_from = 'User Send - Not Found'
        date = 'Date - Not Found'
        subject = 'Subject - Not Found'

        for info in header_info:
            if info['name'] == 'From':
                user_from = info['value']
            if info['name'] == 'Date':
                date_parser = DateParser(info['value'])
                date_parser.parse()
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
