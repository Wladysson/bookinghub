from config.database import get_cursor

from modules.hotels import queries

from shared.exceptions.concurrency_exceptions import (
    RoomUnavailableError
)

from shared.exceptions.business_exceptions import (
    ResourceNotFoundError
)


class HotelAvailabilityControl:

    @staticmethod
    def lock_room(
        connection,
        room_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.LOCK_ROOM_FOR_UPDATE,
                (room_id,)
            )

            room = cursor.fetchone()

            if not room:
                raise ResourceNotFoundError(
                    "Quarto não encontrado"
                )

            return room

    @staticmethod
    def validate_room_availability(
        connection,
        hotel_id,
        room_id,
        check_in,
        check_out
    ):

        available_rooms = []

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_AVAILABLE_ROOMS,
                (
                    hotel_id,
                    check_out,
                    check_in
                )
            )

            available_rooms = cursor.fetchall()

        available_room_ids = [
            room["id"]
            for room in available_rooms
        ]

        if room_id not in available_room_ids:

            raise RoomUnavailableError(
                "Quarto indisponível "
                "para o período informado"
            )