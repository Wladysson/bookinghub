from config.database import get_cursor

from modules.customers import queries

from shared.exceptions.business_exceptions import (
    ResourceNotFoundError
)


class CustomerRepository:

    @staticmethod
    def find_all(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_ALL_CUSTOMERS
            )

            return cursor.fetchall()

    @staticmethod
    def find_by_id(
        connection,
        customer_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_CUSTOMER_BY_ID,
                (customer_id,)
            )

            customer = cursor.fetchone()

            if not customer:

                raise ResourceNotFoundError(
                    "Cliente não encontrado"
                )

            return customer

    @staticmethod
    def find_by_email(
        connection,
        email: str
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_CUSTOMER_BY_EMAIL,
                (email,)
            )

            return cursor.fetchone()

    @staticmethod
    def find_by_document(
        connection,
        document_number: str
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_CUSTOMER_BY_DOCUMENT,
                (document_number,)
            )

            return cursor.fetchone()

    @staticmethod
    def create(
        connection,
        customer_data: dict
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.CREATE_CUSTOMER,
                (
                    customer_data["first_name"],
                    customer_data["last_name"],
                    customer_data["email"],
                    customer_data["phone"],
                    customer_data["document_number"],
                    customer_data["nationality"]
                )
            )

            return cursor.fetchone()

    @staticmethod
    def update(
        connection,
        customer_id: int,
        customer_data: dict
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.UPDATE_CUSTOMER,
                (
                    customer_data.get("first_name"),
                    customer_data.get("last_name"),
                    customer_data.get("phone"),
                    customer_data.get("nationality"),
                    customer_id
                )
            )

            customer = cursor.fetchone()

            if not customer:

                raise ResourceNotFoundError(
                    "Cliente não encontrado"
                )

            return customer

    @staticmethod
    def delete(
        connection,
        customer_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.DELETE_CUSTOMER,
                (customer_id,)
            )

            if cursor.rowcount == 0:

                raise ResourceNotFoundError(
                    "Cliente não encontrado"
                )