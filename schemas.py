from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Literal
from datetime import datetime

class AlertPromptCreateRequest(BaseModel):
    prompt: str = Field(..., max_length=511)
    llm_model: str
    http_method: Literal["POST", "PUT", "PATCH", "DELETE"] = "POST"
    http_url: str
    is_recurring: bool = False
    max_datetime: Optional[datetime] = None
    payload_format: Optional[Dict] = None

class NewsAlertCreateRequest(BaseModel):
    title: str = Field(..., max_length=63)
    content: str = Field(..., max_length=2047)
    keywords: List[str]