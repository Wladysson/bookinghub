from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional
from enum import Enum


class PaymentStatus(str, Enum):

    APPROVED = "approved"

    FAILED = "failed"

    REFUNDED = "refunded"


class PaymentMethod(str, Enum):

    CREDIT_CARD = "credit_card"

    PIX = "pix"

    DEBIT_CARD = "debit_card"


@dataclass
class Payment:

    id: Optional[int]

    reservation_type: str
    reservation_id: int

    customer_id: int

    amount: Decimal

    payment_method: str

    status: str

    transaction_id: str

    created_at: Optional[datetime]
    