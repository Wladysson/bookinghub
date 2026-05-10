from fastapi import APIRouter
from fastapi import status

from modules.airports.schemas import (
    AirportResponse,
    AirportCreateRequest
)

from modules.airports.service import (
    AirportService
)

router = APIRouter(
    prefix="/airports",
    tags=["Airports"]
)


@router.get(
    "",
    response_model=list[AirportResponse]
)
def get_all_airports():

    return AirportService.get_all_airports()


@router.get(
    "/{airport_id}",
    response_model=AirportResponse
)
def get_airport_by_id(
    airport_id: int
):

    return AirportService.get_airport_by_id(
        airport_id
    )


@router.post(
    "",
    response_model=AirportResponse,
    status_code=status.HTTP_201_CREATED
)
def create_airport(
    request: AirportCreateRequest
):

    return AirportService.create_airport(
        request.model_dump()
    )


@router.delete(
    "/{airport_id}",
    status_code=status.HTTP_200_OK
)
def delete_airport(
    airport_id: int
):

    return AirportService.delete_airport(
        airport_id
    )