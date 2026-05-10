from datetime import datetime

from fastapi import APIRouter
from fastapi import Query
from fastapi import status

from modules.hotels.schemas import (
    HotelResponse,
    HotelCreateRequest,
    RoomResponse,
    RoomCreateRequest
)

from modules.hotels.service import (
    HotelService
)

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)


@router.get(
    "",
    response_model=list[HotelResponse]
)
def get_all_hotels():

    return HotelService.get_all_hotels()


@router.get(
    "/{hotel_id}",
    response_model=HotelResponse
)
def get_hotel_by_id(
    hotel_id: int
):

    return HotelService.get_hotel_by_id(
        hotel_id
    )


@router.post(
    "",
    response_model=HotelResponse,
    status_code=status.HTTP_201_CREATED
)
def create_hotel(
    request: HotelCreateRequest
):

    return HotelService.create_hotel(
        request.model_dump()
    )


@router.delete(
    "/{hotel_id}"
)
def delete_hotel(
    hotel_id: int
):

    return HotelService.delete_hotel(
        hotel_id
    )


@router.post(
    "/rooms",
    response_model=RoomResponse,
    status_code=status.HTTP_201_CREATED
)
def create_room(
    request: RoomCreateRequest
):

    return HotelService.create_room(
        request.model_dump()
    )


@router.get(
    "/{hotel_id}/rooms",
    response_model=list[RoomResponse]
)
def get_rooms_by_hotel(
    hotel_id: int
):

    return HotelService.get_rooms_by_hotel(
        hotel_id
    )


@router.get(
    "/{hotel_id}/available-rooms"
)
def get_available_rooms(
    hotel_id: int,
    check_in: datetime = Query(...),
    check_out: datetime = Query(...)
):

    return HotelService.get_available_rooms(
        hotel_id,
        check_in,
        check_out
    )