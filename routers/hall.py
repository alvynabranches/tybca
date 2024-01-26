from sqlmodel import select, Session
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from db import engine
from models.hall import Hall, Seat
from pydantic import BaseModel
from typing import Optional

class HallCreate(BaseModel):
    hall_name: str
    location: str
    lat: float
    long: float

class HallUpdate(BaseModel):
    hall_name: Optional[str]
    location: Optional[str]
    lat: Optional[float]
    long: Optional[float]

class SeatCreate(BaseModel):
    seat_number: str
    hall_id: int

class SeatUpdate(BaseModel):
    seat_number: str
    hall_id: int

hall_router = APIRouter()

@hall_router.get("/", response_model=list[Hall])
async def get_all_halls():
    with Session(engine) as session:
        return session.exec(select(Hall)).all()

@hall_router.get("/{hall_id}", response_model=Hall)
async def get_hall_by_id(hall_id: int):
    with Session(engine) as session:
        hall = session.exec(select(Hall).where(Hall.id == hall_id)).first()
        if hall is None:
            raise HTTPException(status_code=404, detail="Hall not found")
        return hall

@hall_router.post("/", response_model=Hall)
async def create_hall(hall_create: HallCreate):
    with Session(engine) as session:
        db_hall = Hall(**hall_create.dict())
        session.add(db_hall)
        session.commit()
        session.refresh(db_hall)
        return db_hall

@hall_router.put("/{hall_id}", response_model=Hall)
async def update_hall(hall_id: int, hall_update: HallUpdate):
    with Session(engine) as session:
        db_hall = session.exec(select(Hall).where(Hall.id == hall_id)).first()
        if db_hall is None:
            raise HTTPException(status_code=404, detail="Hall not found")
        
        for field, value in hall_update.dict().items():
            setattr(db_hall, field, value)
        
        session.commit()
        session.refresh(db_hall)
        return db_hall

@hall_router.get("/seat/", response_model=list[Seat])
async def get_all_seats():
    with Session(engine) as session:
        return session.exec(select(Seat)).all()

@hall_router.put("/seat/{seat_id}", response_model=Seat)
async def update_seat(seat_id: int, seat_update: SeatUpdate):
    with Session(engine) as session:
        db_seat = session.exec(select(Seat).where(Seat.id == seat_id)).first()
        if db_seat is None:
            raise HTTPException(status_code=404, detail="Seat not found")

        # Update the seat with the new data
        for field, value in seat_update.dict().items():
            setattr(db_seat, field, value)

        session.commit()
        session.refresh(db_seat)
        return db_seat