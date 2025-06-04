from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict
from datetime import datetime

class AlertPromptCreateRequest(BaseModel):
    prompt: str = Field(..., max_length=511)
    llm_model: str
    is_recurring: bool = False
    max_datetime: Optional[datetime] = None

class GenericAlertCreateRequest(BaseModel):
    content: Dict

class NewsAlertCreateRequest(BaseModel):
    title: str = Field(..., max_length=63)
    content: str = Field(..., max_length=2047)
    keywords: List[str]
    entities: Optional[List[str]] = None
    due_date: Optional[datetime] = None
    source_url: Optional[str] = Field(None, max_length=255)