from pydantic_settings import BaseSettings
from core.logging_config import logger 
class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

try:
    settings = Settings()
except Exception:
    logger.error("Нет данных в .env", exc_info=True)