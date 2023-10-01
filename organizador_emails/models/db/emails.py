from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Emails(Base):
    __tablename__ = 'emails'

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(200))
    user_from: Mapped[str] = mapped_column(String(200))
    date: Mapped[datetime]


if __name__ == '__main__':
    from organizador_emails.db.connect import engine

    Base.metadata.create_all(bind=engine)
