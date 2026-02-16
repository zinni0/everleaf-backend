from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

engine = create_engine(settings.db_url)

SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
