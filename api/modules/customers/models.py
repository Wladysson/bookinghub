from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Customer:

    id: Optional[int]

    first_name: str
    last_name: str

    email: str
    phone: str

    document_number: str

    nationality: str

    created_at: Optional[datetime]