from shared.utils.transaction import transaction

from modules.hotels.availability import (
    HotelAvailabilityControl
)

from modules.reservations.repository import (
    ReservationRepository
)


class HotelReservationService:

    @staticmethod
    def reserve_room(
        customer_id,
        hotel_id,
        room_id,
        check_in,
        check_out
    ):

        with transaction() as connection:

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

            reservation = (
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

            return reservation