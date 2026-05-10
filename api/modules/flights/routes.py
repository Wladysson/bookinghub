from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from fastapi import Query
from fastapi import status

from modules.flights.schemas import (
    FlightResponse,
    FlightCreateRequest
)

from modules.flights.service import (
    FlightService
)

from modules.flights.transaction_service import (
    FlightTransactionService
)

router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)


@router.get(
    "",
    response_model=list[FlightResponse]
)
def get_all_flights():

    return FlightService.get_all_flights()


@router.get(
    "/{flight_id}",
    response_model=FlightResponse
)
def get_flight_by_id(
    flight_id: int
):

    return FlightService.get_flight_by_id(
        flight_id
    )


@router.post(
    "",
    response_model=FlightResponse,
    status_code=status.HTTP_201_CREATED
)
def create_flight(
    request: FlightCreateRequest
):

    return FlightService.create_flight(
        request.model_dump()
    )


@router.delete(
    "/{flight_id}"
)
def delete_flight(
    flight_id: int
):

    return FlightService.delete_flight(
        flight_id
    )


@router.get(
    "/available/search"
)
def get_available_flights(
    origin: Optional[str] = Query(None),
    destination: Optional[str] = Query(None),
    departure_date: Optional[datetime] = Query(None)
):

    return FlightService.get_available_flights(
        origin,
        destination,
        departure_date
    )


@router.post(
    "/{flight_id}/reserve-seat"
)
def reserve_seat(
    flight_id: int
):

    return FlightTransactionService.reserve_seat(
        flight_id
    )