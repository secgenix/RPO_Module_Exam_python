from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception:
    logger.error("Ошибка подключеня к бд", exc_info=True)