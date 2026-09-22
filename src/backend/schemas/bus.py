from pydantic import BaseModel


class BusCreate(BaseModel):
    name: str
    plate_number: str
    capacity: int