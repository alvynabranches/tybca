import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.tiatr import tiatr_router

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
app.include_router(tiatr_router, prefix="/tiatr")

@app.get("/")
async def home():
    # return {"url": os.environ["DB_URL"]}
    return {"url": "sample"}
