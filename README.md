# Test Server with FastAPI and MySQL

A simple test server using FastAPI with MySQL database integration.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up MySQL:
- Make sure MySQL is installed and running
- Create a new database named 'test_db' (or your preferred name)
- Copy `env.example` to `.env` and update the credentials as needed

## Running the Server

Start the server with:
```bash
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Available Endpoints

- `POST /items/` - Create a new item
- `GET /items/` - List all items
- `GET /items/{item_id}` - Get a specific item
- `DELETE /items/{item_id}` - Delete an item 