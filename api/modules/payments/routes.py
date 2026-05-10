from fastapi import APIRouter
from fastapi import status

from modules.payments.schemas import (
    PaymentCreateRequest,
    PaymentResponse,
    RefundRequest,
    RefundResponse
)

from modules.payments.service import (
    PaymentService
)

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post(
    "",
    response_model=PaymentResponse,
    status_code=status.HTTP_201_CREATED
)
def process_payment(
    request: PaymentCreateRequest
):

    return PaymentService.process_payment(
        request.model_dump()
    )


@router.post(
    "/refund",
    response_model=RefundResponse
)
def refund_payment(
    request: RefundRequest
):

    return PaymentService.refund_payment(
        request.payment_id
    )


@router.get(
    "",
    response_model=list[PaymentResponse]
)
def get_all_payments():

    return PaymentService.get_all_payments()


@router.get(
    "/{payment_id}",
    response_model=PaymentResponse
)
def get_payment(
    payment_id: int
):

    return PaymentService.get_payment(
        payment_id
    )