import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




# Load environment variables from .env
# Look for .env in the workspace root (2 levels up from backend/modules)
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".env")
load_dotenv(dotenv_path=env_path)

# Get DB URL
DATABASE_URL = os.getenv("DB_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in .env file")

# Create engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
