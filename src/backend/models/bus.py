from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
from backend.db.database import Base


class Bus(Base):
    __tablename__ = "buses"

    id = Column(
    String,
    primary_key=True,
    default=lambda: str(uuid.uuid4()),
    index=True,
)
    name = Column(String(50), index=True)
    plate_number = Column(String(20), unique=True, index=True)
    capacity = Column(Integer, index=True)
    seats = relationship(
        "Seat",
        back_populates="bus")
    trips = relationship(
        "Trip",
        back_populates="bus"
    )