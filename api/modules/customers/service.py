from shared.utils.transaction import transaction

from modules.customers.repository import (
    CustomerRepository
)

from shared.exceptions.business_exceptions import (
    ValidationError
)


class CustomerService:

    @staticmethod
    def get_all_customers():

        with transaction() as connection:

            return CustomerRepository.find_all(
                connection
            )

    @staticmethod
    def get_customer_by_id(
        customer_id: int
    ):

        with transaction() as connection:

            return CustomerRepository.find_by_id(
                connection,
                customer_id
            )

    @staticmethod
    def create_customer(
        customer_data: dict
    ):

        CustomerService._validate_customer(
            customer_data
        )

        with transaction() as connection:

            existing_email = (
                CustomerRepository.find_by_email(
                    connection,
                    customer_data["email"]
                )
            )

            if existing_email:

                raise ValidationError(
                    "E-mail já cadastrado"
                )

            existing_document = (
                CustomerRepository.find_by_document(
                    connection,
                    customer_data["document_number"]
                )
            )

            if existing_document:

                raise ValidationError(
                    "Documento já cadastrado"
                )

            return CustomerRepository.create(
                connection,
                customer_data
            )

    @staticmethod
    def update_customer(
        customer_id: int,
        customer_data: dict
    ):

        with transaction() as connection:

            return CustomerRepository.update(
                connection,
                customer_id,
                customer_data
            )

    @staticmethod
    def delete_customer(
        customer_id: int
    ):

        with transaction() as connection:

            CustomerRepository.delete(
                connection,
                customer_id
            )

            return {
                "message": "Cliente removido com sucesso"
            }

    @staticmethod
    def _validate_customer(
        customer_data: dict
    ):

        document = (
            customer_data["document_number"]
            .strip()
        )

        if len(document) < 5:

            raise ValidationError(
                "Documento inválido"
            )

        customer_data["email"] = (
            customer_data["email"]
            .lower()
            .strip()
        )