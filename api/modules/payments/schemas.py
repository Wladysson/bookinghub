from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class PaymentCreateRequest(BaseModel):

    reservation_type: str = Field(
        examples=["flight", "hotel", "package"]
    )

    reservation_id: int

    customer_id: int

    amount: Decimal = Field(
        gt=0
    )

    payment_method: str = Field(
        examples=[
            "credit_card",
            "pix",
            "debit_card"
        ]
    )


class PaymentResponse(BaseModel):

    id: int

    reservation_type: str
    reservation_id: int

    customer_id: int

    amount: Decimal

    payment_method: str

    status: str

    transaction_id: str

    created_at: datetime


class RefundRequest(BaseModel):

    payment_id: int

    reason: Optional[str] = None


class RefundResponse(BaseModel):

    payment_id: int

    refund_status: str

    refunded_at: datetime