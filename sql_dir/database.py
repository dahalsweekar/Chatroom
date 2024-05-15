from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_URL = "sqlite:///./my_sql.db"
engine = create_engine(
    SQL_URL,
    echo=True
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()