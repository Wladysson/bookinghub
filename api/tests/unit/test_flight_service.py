from decimal import Decimal

from modules.flights.models import Flight


def test_should_validate_available_seats():

    flight = Flight(
        id=1,
        flight_number="LA1234",

        origin_airport_id=1,
        destination_airport_id=2,

        departure_time=None,
        arrival_time=None,

        total_seats=100,
        available_seats=20,

        price=Decimal("799.90"),

        created_at=None
    )

    assert flight.available_seats > 0


def test_should_validate_flight_price():

    flight = Flight(
        id=1,
        flight_number="G31234",

        origin_airport_id=1,
        destination_airport_id=2,

        departure_time=None,
        arrival_time=None,

        total_seats=100,
        available_seats=50,

        price=Decimal("1200.50"),

        created_at=None
    )

    assert flight.price > 0