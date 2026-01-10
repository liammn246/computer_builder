from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

engine = create_engine("sqlite:///./database/test.db")
session_local = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db: Session = session_local()
    try:
        yield db
    finally:
        db.close()