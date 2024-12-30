from fastapi import FastAPI
from .routers import steps

app = FastAPI(title="WMS Steps Service")

app.include_router(steps.router)

@app.get("/")
def root():
    return {"message": "Hello from wms-steps-service!"}