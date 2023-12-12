import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"url": os.environ["DB_URL"]}
