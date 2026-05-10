from config.database import get_cursor

from modules.reports import queries


class ReportsRepository:

    @staticmethod
    def get_total_revenue(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.TOTAL_REVENUE
            )

            return cursor.fetchone()

    @staticmethod
    def get_total_reservations(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.TOTAL_RESERVATIONS
            )

            return cursor.fetchone()

    @staticmethod
    def get_top_destinations(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.TOP_DESTINATIONS
            )

            return cursor.fetchall()

    @staticmethod
    def get_hotel_occupancy(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.HOTEL_OCCUPANCY
            )

            return cursor.fetchall()

    @staticmethod
    def get_payments_by_method(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.PAYMENTS_BY_METHOD
            )

            return cursor.fetchall()

    @staticmethod
    def get_monthly_revenue(connection):

        with get_cursor(connection) as cursor:

            cursor.execute(
                queries.MONTHLY_REVENUE
            )

            return cursor.fetchall()