from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite for demo; swap to Postgres via DATABASE_URL env
DATABASE_URL = "sqlite:///./attendance.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, pool_pre_ping=True, pool_size=5, max_overflow=10
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
