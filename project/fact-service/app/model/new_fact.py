from pydantic import BaseModel

class NewFact(BaseModel):
    text: str