from psycopg2.errors import UniqueViolation

from config.database import get_cursor

from modules.airports import queries

from shared.exceptions.business_exceptions import (
    ResourceNotFoundError,
    ValidationError
)


class AirportRepository:

    @staticmethod
    def find_all(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_ALL_AIRPORTS
            )

            return cursor.fetchall()

    @staticmethod
    def find_by_id(
        connection,
        airport_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_AIRPORT_BY_ID,
                (airport_id,)
            )

            airport = cursor.fetchone()

            if not airport:
                raise ResourceNotFoundError(
                    "Aeroporto não encontrado"
                )

            return airport

    @staticmethod
    def find_by_code(
        connection,
        code: str
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_AIRPORT_BY_CODE,
                (code,)
            )

            return cursor.fetchone()

    @staticmethod
    def create(
        connection,
        airport_data: dict
    ):

        try:

            with get_cursor(connection) as cursor:

                cursor.execute(
                    queries.CREATE_AIRPORT,
                    (
                        airport_data["code"],
                        airport_data["name"],
                        airport_data["city"],
                        airport_data["country"]
                    )
                )

                return cursor.fetchone()

        except UniqueViolation:

            raise ValidationError(
                "Código de aeroporto já existe"
            )

    @staticmethod
    def delete(
        connection,
        airport_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.DELETE_AIRPORT,
                (airport_id,)
            )

            if cursor.rowcount == 0:
                raise ResourceNotFoundError(
                    "Aeroporto não encontrado"
                )