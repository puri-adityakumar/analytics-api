from fastapi import APIRouter

router = APIRouter()



@router.get("/")
def read_events():
    return {
        "result": [1, 2, 3]
    }


@router.get("/event_id")
def get_event(event_int: int):
    return {"abcid": event_id}