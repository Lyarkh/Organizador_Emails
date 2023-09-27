from datetime import datetime
from typing import List, Optional

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Emails(Base):
    __tablename__ = 'emails'

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(200))
    user_from: Mapped[str] = mapped_column(String(200))
    date: Mapped[datetime] = mapped_column(datetime)
