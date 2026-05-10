from decimal import Decimal

from modules.flights.models import Flight


def test_should_create_flight_model():

    flight = Flight(
        id=1,

        flight_number="LA1234",

        origin_airport_id=1,
        destination_airport_id=2,

        departure_time=None,
        arrival_time=None,

        total_seats=180,
        available_seats=180,

        price=Decimal("899.90"),

        created_at=None
    )

    assert flight.flight_number == "LA1234"

    assert flight.available_seats == 180

    assert flight.price == Decimal("899.90")