from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine

db_file = "database.db"
engine = create_engine(f"sqlite:///{db_file}", echo=True, future=True)
# async_engine = create_async_engine(
#     f"aiosqlite+sqlite:///{db_file}", echo=True, future=True
# )

def create_tables():
    from models.user import User
    from models.hall import Hall, Seat
    from models.feedback import Feedback
    from models.tiatr import Tiatr, Show
    from models.booking import Booking, Payment
    
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    create_tables()