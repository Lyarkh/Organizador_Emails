from dataclasses import dataclass
from datetime import datetime


@dataclass
class ResponseMessage:
    user_from: str
    labels: list[str]
    date: datetime
    subject: str
    snippet: str
