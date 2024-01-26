from sqlmodel import SQLModel, Field, UniqueConstraint

class User(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("username"),)
    id: int = Field(primary_key=True)
    username: str
    email: str
    phone: int
    hash: str
    usertype: str
