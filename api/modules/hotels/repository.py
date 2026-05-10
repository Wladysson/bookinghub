from config.database import get_cursor

from modules.hotels import queries

from shared.exceptions.business_exceptions import (
    ResourceNotFoundError
)


class HotelRepository:

    @staticmethod
    def find_all(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_ALL_HOTELS
            )

            return cursor.fetchall()

    @staticmethod
    def find_by_id(
        connection,
        hotel_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_HOTEL_BY_ID,
                (hotel_id,)
            )

            hotel = cursor.fetchone()

            if not hotel:
                raise ResourceNotFoundError(
                    "Hotel não encontrado"
                )

            return hotel

    @staticmethod
    def create(
        connection,
        hotel_data: dict
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.CREATE_HOTEL,
                (
                    hotel_data["name"],
                    hotel_data["city"],
                    hotel_data["country"],
                    hotel_data["stars"],
                    hotel_data["address"]
                )
            )

            return cursor.fetchone()

    @staticmethod
    def delete(
        connection,
        hotel_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.DELETE_HOTEL,
                (hotel_id,)
            )

            if cursor.rowcount == 0:
                raise ResourceNotFoundError(
                    "Hotel não encontrado"
                )

    @staticmethod
    def create_room(
        connection,
        room_data: dict
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.CREATE_ROOM,
                (
                    room_data["hotel_id"],
                    room_data["room_number"],
                    room_data["type"],
                    room_data["capacity"],
                    room_data["price_per_night"]
                )
            )

            return cursor.fetchone()

    @staticmethod
    def get_rooms_by_hotel(
        connection,
        hotel_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_ROOMS_BY_HOTEL,
                (hotel_id,)
            )

            return cursor.fetchall()

    @staticmethod
    def get_available_rooms(
        connection,
        hotel_id: int,
        check_in,
        check_out
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_AVAILABLE_ROOMS,
                (
                    hotel_id,
                    check_out,
                    check_in
                )
            )

            return cursor.fetchall()