from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import httpx
import models
import schemas
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Hook TTS")

ALERTS_API_URL = "http://127.0.0.1:8000/api/v1/"

@app.post("/create-alert", response_model=dict)
async def create_alert(
    request: schemas.AlertPromptCreateRequest,
    db: Session = Depends(get_db)
):
    # Create the alert in our database
    db_alert = models.AlertPrompt(
        prompt=request.prompt,
        http_method=request.http_method,
        is_recurring=request.is_recurring,
        llm_model=request.llm_model,
        max_datetime=request.max_datetime
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)

    # Forward the request to the alerts API
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                ALERTS_API_URL + "alerts",
                json=request.model_dump()
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            # If the forwarding fails, delete the alert from our database
            db.delete(db_alert)
            db.commit()
            raise HTTPException(
                status_code=500,
                detail=f"Failed to forward alert to alerts service: {str(e)}"
            )