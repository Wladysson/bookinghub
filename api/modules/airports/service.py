from shared.utils.transaction import transaction

from modules.airports.repository import (
    AirportRepository
)

from shared.exceptions.business_exceptions import (
    ValidationError
)


class AirportService:

    @staticmethod
    def get_all_airports():

        with transaction() as connection:

            return AirportRepository.find_all(
                connection
            )

    @staticmethod
    def get_airport_by_id(
        airport_id: int
    ):

        with transaction() as connection:

            return AirportRepository.find_by_id(
                connection,
                airport_id
            )

    @staticmethod
    def create_airport(
        airport_data: dict
    ):

        AirportService._validate_airport_data(
            airport_data
        )

        with transaction() as connection:

            existing_airport = (
                AirportRepository.find_by_code(
                    connection,
                    airport_data["code"]
                )
            )

            if existing_airport:
                raise ValidationError(
                    "Código de aeroporto já cadastrado"
                )

            return AirportRepository.create(
                connection,
                airport_data
            )

    @staticmethod
    def delete_airport(
        airport_id: int
    ):

        with transaction() as connection:

            AirportRepository.delete(
                connection,
                airport_id
            )

            return {
                "message": "Aeroporto removido com sucesso"
            }

    @staticmethod
    def _validate_airport_data(
        airport_data: dict
    ):

        required_fields = [
            "code",
            "name",
            "city",
            "country"
        ]

        for field in required_fields:

            if not airport_data.get(field):

                raise ValidationError(
                    f"Campo obrigatório ausente: {field}"
                )

        airport_data["code"] = (
            airport_data["code"]
            .upper()
            .strip()
        )