from decimal import Decimal

from modules.payments.models import (
    Payment,
    PaymentMethod,
    PaymentStatus
)


def test_should_create_payment():

    payment = Payment(
        id=1,

        reservation_type="flight",
        reservation_id=10,

        customer_id=1,

        amount=Decimal("1500.00"),

        payment_method=PaymentMethod.PIX,

        status=PaymentStatus.APPROVED,

        transaction_id="abc-123",

        created_at=None
    )

    assert payment.amount == Decimal("1500.00")

    assert payment.status == PaymentStatus.APPROVED


def test_should_validate_payment_method():

    payment = Payment(
        id=1,

        reservation_type="hotel",
        reservation_id=5,

        customer_id=1,

        amount=Decimal("850.00"),

        payment_method=PaymentMethod.CREDIT_CARD,

        status=PaymentStatus.APPROVED,

        transaction_id="tx-999",

        created_at=None
    )

    assert (
        payment.payment_method
        == PaymentMethod.CREDIT_CARD
    )