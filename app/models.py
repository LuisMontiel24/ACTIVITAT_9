# app/models.py
from pydantic import BaseModel
from typing import Optional, List

class Tag(BaseModel):
    name: str
    value: int

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = 0.0
    tags: List[Tag] = []
