from datetime import datetime

from sqlalchemy import Date, DateTime, ForeignKey, String,Column, Integer
from sqlalchemy.orm import  relationship
import uuid
from backend.db.database import Base




class Trip(Base):
    __tablename__ = "trips"

    id = Column(
      String,
      primary_key=True,
      default=lambda: str(uuid.uuid4()),
      index=True,
  )

    origin = Column(String(100))
    destination = Column(String(100))
    travel_date = Column(Date)

    bus_id = Column(
        ForeignKey("buses.id")
    )
    trip_seats = relationship(
        "TripSeat",
        back_populates="trip"
    )

    bus = relationship(
        "Bus",
        back_populates="trips"
    )