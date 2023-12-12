from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: Field(primary_key=True)
    username: str
    email: str
    phone: int
    hash: str
    
class Admin(SQLModel, table=True):
    id: Field(primary_key=True)
    username: str
    hash: str
    phone: int
