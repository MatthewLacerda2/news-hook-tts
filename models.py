from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow) 