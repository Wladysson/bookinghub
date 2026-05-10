from shared.utils.transaction import transaction

from modules.reports.repository import (
    ReportsRepository
)

from modules.reports.analytics import (
    ReportsAnalytics
)


class ReportsService:

    @staticmethod
    def get_dashboard_metrics():

        with transaction() as connection:

            revenue = (
                ReportsRepository
                .get_total_revenue(
                    connection
                )
            )

            reservations = (
                ReportsRepository
                .get_total_reservations(
                    connection
                )
            )

            average_ticket = (
                ReportsAnalytics
                .calculate_average_ticket(
                    revenue["total_revenue"],
                    reservations[
                        "total_reservations"
                    ]
                )
            )

            return {
                "total_revenue":
                    revenue["total_revenue"],

                "total_reservations":
                    reservations[
                        "total_reservations"
                    ],

                "average_ticket":
                    average_ticket
            }

    @staticmethod
    def get_top_destinations():

        with transaction() as connection:

            return ReportsRepository \
                .get_top_destinations(
                    connection
                )

    @staticmethod
    def get_hotel_occupancy():

        with transaction() as connection:

            return ReportsRepository \
                .get_hotel_occupancy(
                    connection
                )

    @staticmethod
    def get_payments_by_method():

        with transaction() as connection:

            return ReportsRepository \
                .get_payments_by_method(
                    connection
                )

    @staticmethod
    def get_monthly_revenue():

        with transaction() as connection:

            return ReportsRepository \
                .get_monthly_revenue(
                    connection
                )