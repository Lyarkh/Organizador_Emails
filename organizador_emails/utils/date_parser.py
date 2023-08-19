from datetime import datetime


class DateParser:
    def __init__(self, date_string):
        self.date_string = date_string
        self.parse()

    def parse(self):
        # Example of the format -> 'Thu, 3 Aug 2023 19:18:55 +0000 (UTC)'
        temp_date = self.date_string.split(',')
        date = datetime.strptime(temp_date[1], '%d %b %Y %H:%M:%S %z (UTC)')
        setattr(self, 'date', date)
