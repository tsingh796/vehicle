import uvicorn
from fastapi import FastAPI
from vehicle_app.routers import vehicles

app = FastAPI()

app.include_router(vehicles.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)