from shared.utils.transaction import transaction

from modules.flights.concurrency import (
    FlightConcurrencyControl
)

from modules.reservations.repository import (
    ReservationRepository
)


class FlightReservationService:

    @staticmethod
    def reserve_flight(
        customer_id,
        flight_id
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

            reservation = (
                ReservationRepository
                .create_flight_reservation(
                    connection,
                    customer_id,
                    flight_id
                )
            )

            return reservation