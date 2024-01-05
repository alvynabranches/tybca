from sqlmodel import SQLModel, Field

class Booking(SQLModel, table=True):
    id: int = Field(primary_key=True)
    show_id: int = Field(foreign_key="show.id")
    seat_id: int = Field(foreign_key="seat.id")

class Payment(SQLModel, table=True):
    id: int = Field(primary_key=True)
    booking_id: int = Field(foreign_key="booking.id")
    payment_method: str
    payment_status: str
    transaction_id: str
