from sqlmodel import SQLModel, Field

class Hall(SQLModel, table=True):
    id: int = Field(primary_key=True)
    hall_name: str
    location: str
    lat: float
    long: float

class Seat(SQLModel, table=True):
    id: int = Field(primary_key=True)
    seat_number: str
    hall_id: int = Field(foreign_key="hall.id")
    