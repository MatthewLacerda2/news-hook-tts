from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import httpx
import models
import schemas
from database import engine, get_db
from schemas import NewsAlertCreateRequest
import uvicorn
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Hook TTS")

ALERTS_API_URL = "http://127.0.0.1:8000/api/v1/"

@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "News Hook TTS"}

@app.get("/news-alert-schema", response_model=dict)
def get_news_alert_schema():
    logger.info("News alert schema requested")
    return NewsAlertCreateRequest.model_json_schema()

@app.post("/create-alert", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_alert(
    request: schemas.AlertPromptCreateRequest,
    db: Session = Depends(get_db)
):
    logger.info(f"Creating new alert with prompt: {request.prompt}")
    # Create the alert in our database
    db_alert = models.AlertPrompt(
        prompt=request.prompt,
        is_recurring=request.is_recurring,
        max_datetime=request.max_datetime
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)

    # Forward the request to the alerts API
    async with httpx.AsyncClient() as client:
        try:
            logger.debug(f"Forwarding alert to external API: {ALERTS_API_URL}alerts/")
            response = await client.post(
                ALERTS_API_URL + "alerts/",
                json=request.model_dump(mode='json'),
                headers={
                    "X-API-Key": "03148719-f9d0-4dd6-9687-6cf2391d6ac9"
                },
                timeout=30
            )
            response.raise_for_status()
            logger.info(f"Alert successfully created and forwarded. ID: {db_alert.id}")
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Failed to forward alert to alerts service: {str(e)}")
            # If the forwarding fails, delete the alert from our database
            db.delete(db_alert)
            db.commit()
            logger.info(f"Rolled back alert creation due to forwarding failure")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to forward alert to alerts service: {str(e)}"
            )

@app.post("/generic-alert", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_generic_alert(
    request: dict,
    db: Session = Depends(get_db)
):
    logger.info("Creating new generic alert")
    # Create the generic alert in our database
    db_alert = models.GenericAlert(
        content=request
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    
    logger.info(f"Generic alert created successfully. ID: {db_alert.id}")
    return {
        "id": db_alert.id,
        "created_at": db_alert.created_at,
        "content": db_alert.content
    }

@app.post("/news-alert", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_news_alert(
    request: schemas.NewsAlertCreateRequest,
    db: Session = Depends(get_db)
):
    logger.info(f"Creating new news alert with title: {request.model_dump_json()}")
    # Create the news alert in our database
    db_alert = models.NewsAlert(
        title=request.title,
        content=request.content,
        keywords=request.keywords,
        entities=request.keywords,
        due_date=datetime.now(),
        source_url="https://localhost:8000/",
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)

    logger.info(f"News alert created successfully. ID: {db_alert.id}")
    return {
        "id": db_alert.id,
        "created_at": db_alert.created_at,
        "title": db_alert.title,
    }

if __name__ == "__main__":
    logger.info("Starting News Hook TTS server")
    uvicorn.run(app, host="127.0.0.1", port=8001, reload=True)
