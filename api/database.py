from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
