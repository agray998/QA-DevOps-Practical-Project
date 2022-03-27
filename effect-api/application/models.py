from pydantic import BaseModel

class Event(BaseModel):
    event: str
    unit: str