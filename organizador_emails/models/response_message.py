from pydantic import BaseModel
from datetime import datetime


class ResponseMessage(BaseModel):
    user_from: str
    labels: list[str]
    date: datetime
    subject: str
    snippet: str
