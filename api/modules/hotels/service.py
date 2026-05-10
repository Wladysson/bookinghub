from shared.utils.transaction import transaction

from shared.exceptions.business_exceptions import (
    ValidationError
)

from shared.utils.validators import (
    validate_positive_number
)

from modules.hotels.repository import (
    HotelRepository
)


class HotelService:

    @staticmethod
    def get_all_hotels():

        with transaction() as connection:

            return HotelRepository.find_all(
                connection
            )

    @staticmethod
    def get_hotel_by_id(
        hotel_id: int
    ):

        with transaction() as connection:

            return HotelRepository.find_by_id(
                connection,
                hotel_id
            )

    @staticmethod
    def create_hotel(
        hotel_data: dict
    ):

        HotelService._validate_hotel(
            hotel_data
        )

        with transaction() as connection:

            return HotelRepository.create(
                connection,
                hotel_data
            )

    @staticmethod
    def delete_hotel(
        hotel_id: int
    ):

        with transaction() as connection:

            HotelRepository.delete(
                connection,
                hotel_id
            )

            return {
                "message": "Hotel removido com sucesso"
            }

    @staticmethod
    def create_room(
        room_data: dict
    ):

        HotelService._validate_room(
            room_data
        )

        with transaction() as connection:

            return HotelRepository.create_room(
                connection,
                room_data
            )

    @staticmethod
    def get_rooms_by_hotel(
        hotel_id: int
    ):

        with transaction() as connection:

            return HotelRepository.get_rooms_by_hotel(
                connection,
                hotel_id
            )

    @staticmethod
    def get_available_rooms(
        hotel_id,
        check_in,
        check_out
    ):

        with transaction() as connection:

            return HotelRepository \
                .get_available_rooms(
                    connection,
                    hotel_id,
                    check_in,
                    check_out
                )

    @staticmethod
    def _validate_hotel(
        hotel_data: dict
    ):

        if hotel_data["stars"] < 1:

            raise ValidationError(
                "Hotel deve possuir "
                "ao menos 1 estrela"
            )

    @staticmethod
    def _validate_room(
        room_data: dict
    ):

        room_types = [
            "single",
            "double",
            "suite"
        ]

        if room_data["type"] not in room_types:

            raise ValidationError(
                "Tipo de quarto inválido"
            )

        validate_positive_number(
            room_data["capacity"]
        )

        validate_positive_number(
            room_data["price_per_night"]
        )