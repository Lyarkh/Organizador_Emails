from datetime import datetime


class DateParser:
    def __init__(self, date_string):
        self.date_string = date_string
        self.parse()

    def parse(self):
        # Example of the format -> 'Thu, 3 Aug 2023 19:18:55 +0000 (UTC)'
        temp_date = self.date_string

        clean_date = self.clean_the_date_string(temp_date)
        self.create_date_object(clean_date)

    def clean_the_date_string(self):
        if ',' in temp_date:
            temp_date = self.date_string.split(', ')[1]

        flag_offset = '+'
        if '-' in temp_date:
            flag_offset = '-'

        temp_date_without_offset = temp_date.split(flag_offset)[0].strip()
        return temp_date_without_offset

    def create_date_obj(self, str_date_to_convert):
        str_format_date = '%d %b %Y %H:%M:%S'
        date = datetime.strptime(str_date_to_convert, str_format_date)
        setattr(self, 'date', date)
