from fastapi import APIRouter
from .schemas import EventSchema

app = APIRouter()

@app.get('/')
def get_information():
    return {
        "items":[1,2,3,4]
    }

@app.get("/{ids}")
def get_ids(ids) -> EventSchema:
    return {"id":ids}