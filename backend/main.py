from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from core.logging_config import logger  
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Incident(Base):
    __tablename__ = "incidents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    status = Column(String, default="open")

try:
    Base.metadata.create_all(bind=engine)
except Exception:
    logger.error("Ошибка подключеня к бд", exc_info=True)

app = FastAPI(title="NexusMonitor API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/incidents")
def get_incidents(db: Session = Depends(get_db)):
    logger.info("Запрос списка инцидентов")
    return {"status": "success", "data": []}

