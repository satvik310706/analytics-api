from fastapi import APIRouter
from .schemas import EventSchema, EventCreateSchema, EventUpdateSchema
import os
from api.db.config import DATABASE_URL
app = APIRouter()

@app.get("/")
def get_love() -> EventSchema:
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    return {"id":69}

@app.post("/")
def give_love(payload:EventCreateSchema) -> EventSchema:
    return {"id":payload.id}

@app.put("/{id}")
def update_love(payload:EventUpdateSchema) -> EventSchema:
    return {"id":payload.id}