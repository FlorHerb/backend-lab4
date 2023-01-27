from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:utn2022@localhost:5432/inmobiliaria_2023"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

BaseBd = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_all():
    BaseBd.metadata.create_all(bind=engine)


def drop_all():
    BaseBd.metadata.drop_all(bind=engine)
