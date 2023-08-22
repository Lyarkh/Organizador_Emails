import pytest
from datetime import datetime

from organizador_emails.utils.date_parser import DateParser

raw_dates_examples = [
    "Thu, 3 Aug 2023 19:18:55 +0000 (UTC)",
    "Fri, 14 Apr 2022 08:30:00 -0700",
    "Mon, 25 Dec 2023 15:45:30 +0200 (CEST)",
    "Wed, 7 Jun 2022 12:00:00",
    "Sat, 1 Jan 2022 00:00:00 -0500",
    "Sun, 9 Nov 2023 21:10:15 +0300 (EAT)",
    "Tue, 18 Jul 2023 10:20:05 +0800",
    "Thu, 29 Sep 2022 17:30:45 -0400",
    "Mon, 6 Mar 2023 06:15:30 +1100",
    "Wed, 12 Oct 2022 14:50:00 -0300"
]
clean_dates_examples = [
    "3 Aug 2023 19:18:55",
    "14 Apr 2022 08:30:00",
    "25 Dec 2023 15:45:30",
    "7 Jun 2022 12:00:00",
    "1 Jan 2022 00:00:00",
    "9 Nov 2023 21:10:15",
    "18 Jul 2023 10:20:05",
    "29 Sep 2022 17:30:45",
    "6 Mar 2023 06:15:30",
    "12 Oct 2022 14:50:00"
]


@pytest.mark.parametrize('raw_date,clean_date', zip(raw_dates_examples, clean_dates_examples))
def test_clean_the_date_string(raw_date, clean_date):
    date_parser = DateParser(raw_date)
    cleaned_date = date_parser.clean_the_date_string(raw_date)
    assert cleaned_date == clean_date

def test_create_date_object():
    example_date = "3 Aug 2023 19:18:55"
    date_parser = DateParser(example_date)
    date_parser.create_date_object(example_date)
    assert hasattr(date_parser, 'date')
    assert isinstance(date_parser.date, datetime)
    assert date_parser.date.year == 2023
    assert date_parser.date.month == 8
    assert date_parser.date.day == 3
    assert date_parser.date.hour == 19
    assert date_parser.date.minute == 18
    assert date_parser.date.second == 55

def test_parse():
    example_date = "Thu, 3 Aug 2023 19:18:55 +0000 (UTC)"
    date_parser = DateParser(example_date)
    date_parser.parse()
    assert hasattr(date_parser, 'date')
    assert isinstance(date_parser.date, datetime)

    expected_date = datetime(2023, 8, 3, 19, 18, 55)
    assert date_parser.date == expected_date