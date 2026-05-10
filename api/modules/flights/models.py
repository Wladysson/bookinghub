from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class Flight:

    id: Optional[int]

    flight_number: str

    origin_airport_id: int
    destination_airport_id: int

    departure_time: datetime
    arrival_time: datetime

    total_seats: int
    available_seats: int

    price: Decimal