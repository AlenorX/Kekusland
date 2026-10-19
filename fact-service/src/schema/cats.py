from pydantic import BaseModel


class Cats(BaseModel):
    fact: str
    length: int