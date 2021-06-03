from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, future=True)
SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False, future=True)
