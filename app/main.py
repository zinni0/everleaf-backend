from sqlalchemy import create_engine, text

from app.core.config import settings

engine = create_engine(settings.db_url)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.scalar())
