from decimal import Decimal


class ReportsAnalytics:

    @staticmethod
    def calculate_average_ticket(
        total_revenue,
        total_reservations
    ):

        reservations = (
            total_reservations or 0
        )

        if reservations == 0:
            return Decimal("0.00")

        return round(
            Decimal(total_revenue)
            / Decimal(reservations),
            2
        )

    @staticmethod
    def calculate_occupancy_rate(
        occupied_rooms,
        total_rooms
    ):

        if total_rooms == 0:
            return 0

        return round(
            (occupied_rooms / total_rooms)
            * 100,
            2
        )

    @staticmethod
    def growth_percentage(
        current,
        previous
    ):

        if previous == 0:
            return 0

        return round(
            ((current - previous) / previous)
            * 100,
            2
        )