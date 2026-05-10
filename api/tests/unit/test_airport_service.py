from modules.airports.models import Airport


def test_should_create_airport_model():

    airport = Airport(
        id=1,
        code="FOR",
        name="Pinto Martins International Airport",
        city="Fortaleza",
        country="Brazil",
        created_at=None
    )

    assert airport.code == "FOR"

    assert airport.city == "Fortaleza"

    assert airport.country == "Brazil"