def calculate_occupancy_rate(
    total_seats: int,
    available_seats: int
) -> float:

    occupied = total_seats - available_seats

    if total_seats == 0:
        return 0

    return round(occupied / total_seats, 2)


def classify_demand(occupancy_rate: float) -> str:

    if occupancy_rate >= 0.80:
        return "HIGH"

    if occupancy_rate >= 0.50:
        return "MEDIUM"

    return "LOW"