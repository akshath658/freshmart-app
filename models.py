from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True   