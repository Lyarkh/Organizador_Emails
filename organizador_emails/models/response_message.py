from datetime import datetime

from pydantic import BaseModel


class ResponseMessage(BaseModel):
    user_from: str
    labels: list[str]
    date: datetime
    subject: str
    snippet: str
