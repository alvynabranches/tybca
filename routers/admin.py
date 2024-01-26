from sqlmodel import select, Session
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from db import engine
from models.hall import Hall, Seat
from pydantic import BaseModel
from typing import Optional

