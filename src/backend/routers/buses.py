from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.schemas.bus import BusCreate
from backend.db.database import get_db
from backend.models.bus import Bus
from backend.models.trip import Trip


router = APIRouter(
    prefix="/buses",
    tags=["Buses"]
)


@router.get("/")
def get_buses(db: Session = Depends(get_db)):
    buses = db.query(Bus).all()

    return buses


@router.post("/")
def create_bus(
    bus: BusCreate,
    db: Session = Depends(get_db)
):
    new_bus = Bus(
        name=bus.name,
        plate_number=bus.plate_number,
        capacity=bus.capacity
    )

    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)

    return new_bus


