from datetime import datetime

class DateParser:
    def __init__(self, date_string):
        self.date_string = date_string
        self.parse()

    def parse(self):
        # Example of the format -> 'Thu, 3 Aug 2023 19:18:55 +0000 (UTC)'
        print(self.date_string)
        temp_date = self.date_string.split(', ')[1]

        flag_offset = '+'
        if '-' in temp_date:
            flag_offset = '-'

        print(temp_date)
        temp_date_without_offset = temp_date.split(flag_offset)[0].strip()
        print(temp_date_without_offset)

        str_format_date = '%d %b %Y %H:%M:%S'

        date = datetime.strptime(temp_date_without_offset, str_format_date)
        setattr(self, 'date', date)
