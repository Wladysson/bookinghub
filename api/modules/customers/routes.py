from fastapi import APIRouter
from fastapi import status

from modules.customers.schemas import (
    CustomerCreateRequest,
    CustomerUpdateRequest,
    CustomerResponse
)

from modules.customers.service import (
    CustomerService
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get(
    "",
    response_model=list[CustomerResponse]
)
def get_all_customers():

    return CustomerService.get_all_customers()


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def get_customer_by_id(
    customer_id: int
):

    return CustomerService.get_customer_by_id(
        customer_id
    )


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_customer(
    request: CustomerCreateRequest
):

    return CustomerService.create_customer(
        request.model_dump()
    )


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse
)
def update_customer(
    customer_id: int,
    request: CustomerUpdateRequest
):

    return CustomerService.update_customer(
        customer_id,
        request.model_dump()
    )


@router.delete(
    "/{customer_id}"
)
def delete_customer(
    customer_id: int
):

    return CustomerService.delete_customer(
        customer_id
    )