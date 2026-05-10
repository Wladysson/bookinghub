from config.database import get_cursor

from modules.payments import queries

from shared.exceptions.business_exceptions import (
    ResourceNotFoundError
)


class PaymentRepository:

    @staticmethod
    def create(
        connection,
        payment_data: dict
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.CREATE_PAYMENT,
                (
                    payment_data["reservation_type"],
                    payment_data["reservation_id"],
                    payment_data["customer_id"],
                    payment_data["amount"],
                    payment_data["payment_method"],
                    payment_data["status"],
                    payment_data["transaction_id"]
                )
            )

            return cursor.fetchone()

    @staticmethod
    def find_by_id(
        connection,
        payment_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_PAYMENT_BY_ID,
                (payment_id,)
            )

            payment = cursor.fetchone()

            if not payment:

                raise ResourceNotFoundError(
                    "Pagamento não encontrado"
                )

            return payment

    @staticmethod
    def find_all(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.GET_ALL_PAYMENTS
            )

            return cursor.fetchall()

    @staticmethod
    def update_status(
        connection,
        payment_id: int,
        status: str
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.UPDATE_PAYMENT_STATUS,
                (
                    status,
                    payment_id
                )
            )

    @staticmethod
    def lock_payment(
        connection,
        payment_id: int
    ):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.LOCK_PAYMENT,
                (payment_id,)
            )

            payment = cursor.fetchone()

            if not payment:

                raise ResourceNotFoundError(
                    "Pagamento não encontrado"
                )

            return payment