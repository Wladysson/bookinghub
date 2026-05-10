from fastapi import APIRouter
from fastapi import status

from modules.reservations.schemas import (
    FlightReservationRequest,
    HotelReservationRequest,
    PackageReservationRequest
)

from modules.reservations.flight_reservation_service import (
    FlightReservationService
)

from modules.reservations.hotel_reservation_service import (
    HotelReservationService
)

from modules.reservations.package_reservation_service import (
    PackageReservationService
)

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)


@router.post(
    "/flight",
    status_code=status.HTTP_201_CREATED
)
def reserve_flight(
    request: FlightReservationRequest
):

    return FlightReservationService \
        .reserve_flight(
            customer_id=request.customer_id,
            flight_id=request.flight_id
        )


@router.post(
    "/hotel",
    status_code=status.HTTP_201_CREATED
)
def reserve_hotel(
    request: HotelReservationRequest
):

    return HotelReservationService \
        .reserve_room(
            customer_id=request.customer_id,
            hotel_id=request.hotel_id,
            room_id=request.room_id,
            check_in=request.check_in,
            check_out=request.check_out
        )


@router.post(
    "/package",
    status_code=status.HTTP_201_CREATED
)
def reserve_package(
    request: PackageReservationRequest
):

    return PackageReservationService \
        .reserve_package(
            customer_id=request.customer_id,
            flight_id=request.flight_id,
            hotel_id=request.hotel_id,
            room_id=request.room_id,
            check_in=request.check_in,
            check_out=request.check_out
        )