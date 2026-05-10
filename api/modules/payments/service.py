import uuid
import random

from shared.utils.transaction import transaction

from modules.payments.repository import (
    PaymentRepository
)

from shared.exceptions.business_exceptions import (
    ValidationError,
    BusinessRuleError
)


class PaymentService:

    VALID_PAYMENT_METHODS = [
        "credit_card",
        "pix",
        "debit_card"
    ]

    @staticmethod
    def process_payment(
        payment_data: dict
    ):

        PaymentService._validate_payment(
            payment_data
        )

        with transaction() as connection:

            transaction_id = str(
                uuid.uuid4()
            )

            payment_status = (
                PaymentService
                ._simulate_gateway_processing()
            )

            payment = PaymentRepository.create(
                connection,
                {
                    **payment_data,
                    "status": payment_status,
                    "transaction_id": transaction_id
                }
            )

            return payment

    @staticmethod
    def refund_payment(
        payment_id: int
    ):

        with transaction() as connection:

            payment = (
                PaymentRepository
                .lock_payment(
                    connection,
                    payment_id
                )
            )

            if payment["status"] == "refunded":

                raise BusinessRuleError(
                    "Pagamento já foi reembolsado"
                )

            if payment["status"] != "approved":

                raise BusinessRuleError(
                    "Somente pagamentos aprovados "
                    "podem ser reembolsados"
                )

            PaymentRepository.update_status(
                connection,
                payment_id,
                "refunded"
            )

            return {
                "payment_id": payment_id,
                "refund_status": "completed"
            }

    @staticmethod
    def get_payment(
        payment_id: int
    ):

        with transaction() as connection:

            return PaymentRepository.find_by_id(
                connection,
                payment_id
            )

    @staticmethod
    def get_all_payments():

        with transaction() as connection:

            return PaymentRepository.find_all(
                connection
            )

    @staticmethod
    def _validate_payment(
        payment_data: dict
    ):

        if (
            payment_data["payment_method"]
            not in PaymentService
            .VALID_PAYMENT_METHODS
        ):

            raise ValidationError(
                "Método de pagamento inválido"
            )

        valid_reservation_types = [
            "flight",
            "hotel",
            "package"
        ]

        if (
            payment_data["reservation_type"]
            not in valid_reservation_types
        ):

            raise ValidationError(
                "Tipo de reserva inválido"
            )

    @staticmethod
    def _simulate_gateway_processing():

        success_rate = random.randint(1, 100)

        if success_rate <= 90:
            return "approved"

        return "failed"