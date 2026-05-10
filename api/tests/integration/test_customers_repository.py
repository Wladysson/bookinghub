from modules.customers.models import Customer


def test_should_create_customer_model():

    customer = Customer(
        id=1,

        first_name="Wladyson",
        last_name="Araujo",

        email="wladyson@email.com",

        phone="85999999999",

        document_number="12345678900",

        nationality="Brazil",

        created_at=None
    )

    assert customer.first_name == "Wladyson"

    assert customer.email == "wladyson@email.com"

    assert customer.nationality == "Brazil"