from sqlmodel import SQLModel, Field

class Hall(SQLModel, table=True):
    id: Field(primary_key=True)
    hall_name: str
    location: str
    lat: float
    long: float

class Seat(SQLModel, table=True):
    id: Field(primary_key=True)
    seat_number: str
    hall_id: Field(foreign_key="hall.id")
    