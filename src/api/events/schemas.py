from typing import List
from pydantic import BaseModel

class Event(BaseModel):
    id: int 


class EventListSchema(BaseModel):
    results: List[EventSchema]
    count: int