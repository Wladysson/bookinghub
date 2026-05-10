from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class HotelResponse(BaseModel):

    id: int

    name: str
    city: str
    country: str

    stars: int
    address: str


class HotelCreateRequest(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=255
    )

    city: str = Field(
        min_length=2,
        max_length=255
    )

    country: str = Field(
        min_length=2,
        max_length=255
    )

    stars: int = Field(
        ge=1,
        le=5
    )

    address: str = Field(
        min_length=5,
        max_length=500
    )


class RoomResponse(BaseModel):

    id: int

    hotel_id: int

    room_number: str
    type: str

    capacity: int

    price_per_night: Decimal


class RoomCreateRequest(BaseModel):

    hotel_id: int

    room_number: str

    type: str = Field(
        examples=["single", "double", "suite"]
    )

    capacity: int = Field(
        gt=0
    )

    price_per_night: Decimal = Field(
        gt=0
    )