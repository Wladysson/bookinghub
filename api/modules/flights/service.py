from shared.utils.transaction import transaction

from shared.exceptions.business_exceptions import (
    ValidationError
)

from modules.flights.repository import (
    FlightRepository
)


class FlightService:

    @staticmethod
    def get_all_flights():

        with transaction() as connection:

            return FlightRepository.find_all(
                connection
            )

    @staticmethod
    def get_flight_by_id(
        flight_id: int
    ):

        with transaction() as connection:

            return FlightRepository.find_by_id(
                connection,
                flight_id
            )

    @staticmethod
    def create_flight(
        flight_data: dict
    ):

        FlightService._validate_flight_data(
            flight_data
        )

        with transaction() as connection:

            return FlightRepository.create(
                connection,
                flight_data
            )

    @staticmethod
    def delete_flight(
        flight_id: int
    ):

        with transaction() as connection:

            FlightRepository.delete(
                connection,
                flight_id
            )

            return {
                "message": "Voo removido com sucesso"
            }

    @staticmethod
    def get_available_flights(
        origin=None,
        destination=None,
        departure_date=None
    ):

        with transaction() as connection:

            return FlightRepository \
                .find_available_flights(
                    connection,
                    origin,
                    destination,
                    departure_date
                )

    @staticmethod
    def _validate_flight_data(
        flight_data: dict
    ):

        if (
            flight_data["origin_airport_id"]
            ==
            flight_data["destination_airport_id"]
        ):

            raise ValidationError(
                "Origem e destino não podem ser iguais"
            )

        if (
            flight_data["available_seats"]
            >
            flight_data["total_seats"]
        ):

            raise ValidationError(
                "Assentos disponíveis não podem "
                "ser maiores que o total"
            )

        if (
            flight_data["departure_time"]
            >=
            flight_data["arrival_time"]
        ):

            raise ValidationError(
                "Horário de chegada deve ser "
                "maior que saída"
            )