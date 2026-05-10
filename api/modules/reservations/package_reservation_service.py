from shared.utils.transaction import transaction

from modules.flights.concurrency import (
    FlightConcurrencyControl
)

from modules.hotels.availability import (
    HotelAvailabilityControl
)

from modules.reservations.repository import (
    ReservationRepository
)

from modules.reservations.savepoints import (
    ReservationSavepoints
)


class PackageReservationService:

    @staticmethod
    def reserve_package(
        customer_id,
        flight_id,
        hotel_id,
        room_id,
        check_in,
        check_out
    ):

        with transaction() as connection:

            ReservationSavepoints \
                .create_savepoint(
                    connection
                )

            try:

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

                flight_reservation = (
                    ReservationRepository
                    .create_flight_reservation(
                        connection,
                        customer_id,
                        flight_id
                    )
                )

                HotelAvailabilityControl \
                    .lock_room(
                        connection,
                        room_id
                    )

                HotelAvailabilityControl \
                    .validate_room_availability(
                        connection,
                        hotel_id,
                        room_id,
                        check_in,
                        check_out
                    )

                hotel_reservation = (
                    ReservationRepository
                    .create_hotel_reservation(
                        connection,
                        customer_id,
                        hotel_id,
                        room_id,
                        check_in,
                        check_out
                    )
                )

                package_reservation = (
                    ReservationRepository
                    .create_package_reservation(
                        connection,
                        customer_id,
                        flight_reservation["id"],
                        hotel_reservation["id"]
                    )
                )

                return package_reservation

            except Exception:

                ReservationSavepoints \
                    .rollback_to_savepoint(
                        connection
                    )

                raise