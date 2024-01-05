import os
from sqlalchemy.engine import URL
from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine

USERNAME = os.environ.get("USERNAME", "root")
PASSWORD = os.environ.get("PASSWORD", "")
DATABASE = os.environ.get("DATABASE", "tiatr")
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "26258"))

SQLALCHEMY_DATABASE_URL = URL.create(
    "cockroachdb",
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DATABASE,
    # query={"disable_cockroachdb_telemetry": "False"},
)

SQLALCHEMY_DATABASE_ASYNC_URL = URL.create(
    "cockroachdb+asyncpg",
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DATABASE,
    # query={"disable_cockroachdb_telemetry": "False"},
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_ASYNC_URL, echo=True, future=True
)

def create_tables():
    from models.user import User, Admin
    from models.hall import Hall, Seat
    from models.tiatr import Tiatr, Show
    from models.booking import Booking, Payment
    
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    create_tables()