from pydantic import BaseModel
from typing import Tuple

class AmbulanceCreate(BaseModel):
    name: str
    location: Tuple[float, float]  # (latitude, longitude)

class AmbulanceResponse(AmbulanceCreate):
    id: int

    class Config:
        from_attributes = True
