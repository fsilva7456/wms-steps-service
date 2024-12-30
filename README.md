# WMS Steps Service

A service for managing workflow management system (WMS) steps and sequences.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export DATABASE_URL="postgresql://user:pass@localhost:5432/mydb"
```

4. Run the application:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Documentation

Once the service is running, visit:
- http://localhost:8000/docs for the Swagger UI
- http://localhost:8000/redoc for ReDoc documentation

## Endpoints

- `GET /`: Root endpoint, health check
- `GET /steps/`: Get all steps
- `POST /steps/`: Create a new step