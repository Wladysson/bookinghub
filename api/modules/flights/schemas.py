from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class FlightResponse(BaseModel):

    id: int

    flight_number: str

    origin_airport_id: int
    destination_airport_id: int

    origin_airport_code: Optional[str] = None
    destination_airport_code: Optional[str] = None

    departure_time: datetime
    arrival_time: datetime

    total_seats: int
    available_seats: int

    price: Decimal


class FlightCreateRequest(BaseModel):

    flight_number: str = Field(
        min_length=2,
        max_length=20
    )

    origin_airport_id: int
    destination_airport_id: int

    departure_time: datetime
    arrival_time: datetime

    total_seats: int = Field(
        gt=0
    )

    available_seats: int = Field(
        gt=0
    )

    price: Decimal = Field(
        gt=0
    )


class FlightAvailabilityQuery(BaseModel):

    origin: Optional[str] = None
    destination: Optional[str] = None
    departure_date: Optional[datetime] = None