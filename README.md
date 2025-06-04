# Test Server with FastAPI and MySQL

A simple test server using FastAPI with MySQL database integration.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`

## API Documentation

We send Alert-Requests
We receive:
    - GenericAlerts (just the payload the server wants to send)
    - NewsAlert (alert on news, to test that the server sends the desired payload)