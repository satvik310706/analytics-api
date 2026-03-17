from pydantic import BaseModel, Field
from typing import List, Optional

class EventSchema(BaseModel):
    id: int
    page: Optional[str] = Field(default='')
    description:Optional[str] = Field(default='')

class EventCreateSchema(BaseModel):
    id:int
    page: List[str]
    description:Optional[str] = Field(default='')

class EventUpdateSchema(BaseModel):
    id: int
    page: Optional[str] = Field(default='')
    description: str
    