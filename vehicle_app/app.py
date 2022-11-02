from fastapi import FastAPI


app = FastAPI()

@app.get("/vehicles")
async def main():
    return {'message': 'Hello World'}