from shared.utils.transaction import transaction

from modules.flights.concurrency import (
    FlightConcurrencyControl
)

from modules.flights.repository import (
    FlightRepository
)


class FlightTransactionService:

    @staticmethod
    def reserve_seat(
        flight_id: int
    ):

        with transaction() as connection:

            FlightConcurrencyControl \
                .lock_flight_and_validate_seats(
                    connection,
                    flight_id
                )

            FlightConcurrencyControl \
                .decrement_available_seats(
                    connection,
                    flight_id
                )

            return FlightRepository.find_by_id(
                connection,
                flight_id
            )