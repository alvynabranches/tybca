from sqlmodel import SQLModel, Field

class Feedback(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    title: str
    description: str