from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///./app_sql.db')

# check_same_thread must be false only for sqlite databases
engine = create_engine(DATABASE_URL,
    connect_args={"check_same_thread": not DATABASE_URL.startswith('sqlite://')})

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create base class for models
Base = declarative_base()