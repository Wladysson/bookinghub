from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class FlightReservationRequest(BaseModel):

    customer_id: int

    flight_id: int


class HotelReservationRequest(BaseModel):

    customer_id: int

    hotel_id: int

    room_id: int

    check_in: datetime
    check_out: datetime


class PackageReservationRequest(BaseModel):

    customer_id: int

    flight_id: int

    hotel_id: int
    room_id: int

    check_in: datetime
    check_out: datetime


class ReservationResponse(BaseModel):

    reservation_id: int

    reservation_type: str

    customer_id: int

    total_amount: Decimal

    status: str

    created_at: datetime


class ReservationErrorResponse(BaseModel):

    error: str