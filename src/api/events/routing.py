from fastapi import APIRouter
from .schemas import EventSchema, EvenListSchema

router = APIRouter()



@router.get("/")
def read_events() -> EventListSchema:
    return {
        "results": [
            {"id": 1}, {"id": 2}. {"id": 3}
        ],
        "count": 
    }

@router.post("/")
def create_event(payload:EventCreateSchema) -> EventSchema:
    print(payload)
    return {"id": 123}


@router.get("/event_id")
def get_event(event_int: int) -> EventSchema:
    return {"id": event_id}