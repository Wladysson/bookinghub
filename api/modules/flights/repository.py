from config.database import get_cursor

from modules.flights import queries

from shared.exceptions.business_exceptions import (
    ResourceNotFoundError
)


class FlightRepository:

    @staticmethod
    def find_all(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_ALL_FLIGHTS
            )

            return cursor.fetchall()

    @staticmethod
    def find_by_id(
        connection,
        flight_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_FLIGHT_BY_ID,
                (flight_id,)
            )

            flight = cursor.fetchone()

            if not flight:
                raise ResourceNotFoundError(
                    "Voo não encontrado"
                )

            return flight

    @staticmethod
    def create(
        connection,
        flight_data: dict
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.CREATE_FLIGHT,
                (
                    flight_data["flight_number"],
                    flight_data["origin_airport_id"],
                    flight_data["destination_airport_id"],
                    flight_data["departure_time"],
                    flight_data["arrival_time"],
                    flight_data["total_seats"],
                    flight_data["available_seats"],
                    flight_data["price"]
                )
            )

            return cursor.fetchone()

    @staticmethod
    def delete(
        connection,
        flight_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.DELETE_FLIGHT,
                (flight_id,)
            )

            if cursor.rowcount == 0:
                raise ResourceNotFoundError(
                    "Voo não encontrado"
                )

    @staticmethod
    def find_available_flights(
        connection,
        origin=None,
        destination=None,
        departure_date=None
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_AVAILABLE_FLIGHTS,
                (
                    origin,
                    origin,
                    destination,
                    destination,
                    departure_date,
                    departure_date
                )
            )

            return cursor.fetchall()