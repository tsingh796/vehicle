from fastapi import FastAPI
from .routers import vehicles

app = FastAPI()

app.include_router(vehicles.router)

