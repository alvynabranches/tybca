from sqlmodel import SQLModel, Field
from datetime import date as d, time as t
from enum import Enum

class StatusOption(Enum):
    on_time: str = "ON TIME"
    delayed: str = "DELAYED"
    cancelled: str = "CANCELLED"

class Tiatr(SQLModel, table=True):
    id: Field(primary_key=True)
    name: str
    amount: int | float
    
class Show(SQLModel, table=True):
    id: Field(primary_key=True)
    tiatr_id: Field(foreign_key="tiatr.id")
    hall_id: Field(foreign_key="hall.id")
    date: d
    time: t
    status: StatusOption = StatusOption.on_time
    