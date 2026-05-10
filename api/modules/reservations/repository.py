from config.database import get_cursor

from modules.reservations import queries


class ReservationRepository:

    @staticmethod
    def create_flight_reservation(
        connection,
        customer_id,
        flight_id
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.CREATE_FLIGHT_RESERVATION,
                (
                    customer_id,
                    flight_id
                )
            )

            return cursor.fetchone()

    @staticmethod
    def create_hotel_reservation(
        connection,
        customer_id,
        hotel_id,
        room_id,
        check_in,
        check_out
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.CREATE_HOTEL_RESERVATION,
                (
                    customer_id,
                    hotel_id,
                    room_id,
                    check_in,
                    check_out
                )
            )

            return cursor.fetchone()

    @staticmethod
    def create_package_reservation(
        connection,
        customer_id,
        flight_reservation_id,
        hotel_reservation_id
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.CREATE_PACKAGE_RESERVATION,
                (
                    customer_id,
                    flight_reservation_id,
                    hotel_reservation_id
                )
            )

            return cursor.fetchone()