import json
from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import Mapped, DeclarativeBase, Session, mapped_column

class Base(DeclarativeBase):
    pass

class Facts(Base):
    __tablename__ = "facts"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]

connect = create_engine('sqlite:///facts.db')

async def initialization_data():
    pass