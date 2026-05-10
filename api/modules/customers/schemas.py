from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class CustomerCreateRequest(BaseModel):

    first_name: str = Field(
        min_length=2,
        max_length=100
    )

    last_name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    phone: str = Field(
        min_length=8,
        max_length=20
    )

    document_number: str = Field(
        min_length=5,
        max_length=30
    )

    nationality: str = Field(
        min_length=2,
        max_length=100
    )


class CustomerUpdateRequest(BaseModel):

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    phone: Optional[str] = None

    nationality: Optional[str] = None


class CustomerResponse(BaseModel):

    id: int

    first_name: str
    last_name: str

    email: EmailStr
    phone: str

    document_number: str

    nationality: str

    created_at: datetime