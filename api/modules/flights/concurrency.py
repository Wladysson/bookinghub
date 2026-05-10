from config.database import get_cursor

from modules.flights import queries

from shared.exceptions.concurrency_exceptions import (
    OverbookingError
)

from shared.exceptions.business_exceptions import (
    ResourceNotFoundError
)


class FlightConcurrencyControl:

    @staticmethod
    def lock_flight_and_validate_seats(
        connection,
        flight_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.LOCK_FLIGHT_FOR_UPDATE,
                (flight_id,)
            )

            flight = cursor.fetchone()

            if not flight:
                raise ResourceNotFoundError(
                    "Voo não encontrado"
                )

            if flight["available_seats"] <= 0:
                raise OverbookingError(
                    "Não há assentos disponíveis"
                )

            return flight

    @staticmethod
    def decrement_available_seats(
        connection,
        flight_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.DECREMENT_AVAILABLE_SEATS,
                (flight_id,)
            )