from modules.flights.concurrency import (
    FlightConcurrencyControl
)

from modules.hotels.availability import (
    HotelAvailabilityControl
)


class ReservationConcurrencyControl:

    @staticmethod
    def lock_flight(
        connection,
        flight_id
    ):

        return FlightConcurrencyControl \
            .lock_flight_and_validate_seats(
                connection,
                flight_id
            )

    @staticmethod
    def lock_room(
        connection,
        room_id
    ):

        return HotelAvailabilityControl \
            .lock_room(
                connection,
                room_id
            )

    @staticmethod
    def validate_room(
        connection,
        hotel_id,
        room_id,
        check_in,
        check_out
    ):

        return HotelAvailabilityControl \
            .validate_room_availability(
                connection,
                hotel_id,
                room_id,
                check_in,
                check_out
            )