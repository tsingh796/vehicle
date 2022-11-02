from fastapi import FastAPI
from .routes import vehicle

app = FastAPI()

app.include_router(vehicle.router)

