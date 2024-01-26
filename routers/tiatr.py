from sqlmodel import select, Session
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from db import engine
from models.tiatr import Tiatr, Show, StatusOption
from pydantic import BaseModel
from datetime import date as d, time as t
from typing import Optional

class TiatrCreate(BaseModel):
    name: str
    description: str
    image: str

class ShowCreate(BaseModel):
    tiatr_id: int
    hall_id: int
    date: d
    time: t
    status: StatusOption = StatusOption.on_time
    amount: float

class ShowUpdate(BaseModel):
    tiatr_id: Optional[int]
    hall_id: Optional[int]
    date: Optional[d]
    time: Optional[t]
    status: Optional[StatusOption]
    amount: Optional[float]

tiatr_router = APIRouter()

@tiatr_router.get("/")
async def get_all_tiatr():
    with Session(engine) as session:
        data = session.exec(select(Tiatr)).all()
        session.close()
    return JSONResponse(content=data, status_code=200)

@tiatr_router.get("/{tiatr_id}")
async def get_tiatr_by_id(tiatr_id: int):
    with Session(engine) as session:
        tiatr = session.exec(select(Tiatr).where(Tiatr.id == tiatr_id)).first()
        if tiatr is None:
            raise HTTPException(status_code=404, detail="Tiatr not found")
        session.close()
        return JSONResponse(content=tiatr.dict(), status_code=200)

@tiatr_router.post("/")
async def create_tiatr(data: TiatrCreate):
    with Session(engine) as session:
        tiatr = Tiatr(**data.__dict__)
        session.add(tiatr)
        session.commit()
        session.close()
    return JSONResponse(content=data.__dict__, status_code=201)

@tiatr_router.get("/shows/", response_model=list[Show])
async def get_all_shows():
    with Session(engine) as session:
        return session.exec(select(Show)).all()

@tiatr_router.get("/shows/{show_id}", response_model=Show)
async def get_show_by_id(show_id: int):
    with Session(engine) as session:
        show = session.exec(select(Show).where(Show.id == show_id)).first()
        if show is None:
            raise HTTPException(status_code=404, detail="Show not found")
        return show

@tiatr_router.post("/shows/", response_model=Show)
async def create_show(data: ShowCreate):
    with Session(engine) as session:
        show = Show(**data.__dict__)
        session.add(show)
        session.commit()
        session.refresh(show)
        return show

@tiatr_router.put("/shows/{show_id}", response_model=Show)
async def update_show(show_id: int, data: ShowUpdate):
    with Session(engine) as session:
        show = session.exec(select(Show).where(Show.id == show_id)).first()
        if show is None:
            raise HTTPException(status_code=404, detail="Show not found")
        
        for field, value in data.__dict__.items():
            setattr(show, field, value)
        
        session.commit()
        session.refresh(show)
        return show