from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Hotel:

    id: Optional[int]

    name: str
    city: str
    country: str

    stars: int
    address: str


@dataclass
class Room:

    id: Optional[int]

    hotel_id: int

    room_number: str
    type: str

    capacity: int

    price_per_night: Decimal