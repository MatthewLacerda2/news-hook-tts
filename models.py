from sqlalchemy import Column, String, DateTime, JSON, Boolean
import uuid
from datetime import datetime
from database import Base

class AlertPrompt(Base):
    __tablename__ = "alert_requests"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now())
    prompt = Column(String(511), nullable=False)
    is_recurring = Column(Boolean, default=False)
    max_datetime = Column(DateTime, nullable=True)

class GenericAlert(Base):
    __tablename__ = "generic_alerts"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now())
    content = Column(JSON, nullable=False)

class NewsAlert(Base):
    __tablename__ = "news_alerts"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now())
    title = Column(String(63), nullable=False)
    content = Column(String(2047), nullable=False)
    keywords = Column(JSON, nullable=False)
    entities = Column(JSON, nullable=True)
    due_date = Column(DateTime, nullable=True)
    source_url = Column(String(255), nullable=True)