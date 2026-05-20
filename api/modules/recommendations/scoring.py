def calculate_flight_score(
    popularity: float,
    availability: float,
    price_factor: float
) -> float:

    score = (
        popularity * 0.5 +
        availability * 0.3 +
        price_factor * 0.2
    )

    return round(score, 2)


def calculate_hotel_score(
    stars: float,
    popularity: float,
    price_factor: float
) -> float:

    score = (
        stars * 0.4 +
        popularity * 0.4 +
        price_factor * 0.2
    )

    return round(score, 2)