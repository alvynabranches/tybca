from sqlmodel import SQLModel, Field

class Booking(SQLModel, table=True):
    id: Field(primary_key=True)
    show_id: Field(foreign_key="show.id")
    seat_id: Field(foreign_key="seat.id")

class Payment(SQLModel, table=True):
    id: Field(primary_key=True)
    booking_id: Field(foreign_key="booking.id")
    payment_method: str
    payment_status: str
    transaction_id: str
