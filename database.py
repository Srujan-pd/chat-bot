from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# This will pick up your Supabase URI from Cloud Run Environment Variables
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# If using Supabase/Postgres, we don't need check_same_thread
if DATABASE_URL.startswith("postgresql"):
    engine = create_engine(DATABASE_URL)
else:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
