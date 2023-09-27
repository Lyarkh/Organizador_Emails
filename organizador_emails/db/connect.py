from sqlalchemy import create_engine

engine = create_engine('sqlite:///db_emails.db', echo=True)