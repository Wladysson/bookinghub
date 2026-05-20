from psycopg2.extras import RealDictCursor
from config.database import get_connection


class RecommendationRepository:

    @staticmethod
    def get_top_flights():

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute("""
            SELECT
                id,
                flight_number,
                origin_airport_code,
                destination_airport_code,
                price,
                available_seats
            FROM flights
            WHERE available_seats > 0
            ORDER BY available_seats DESC
            LIMIT 10
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    @staticmethod
    def get_top_hotels():

        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute("""
            SELECT
                id,
                name,
                city,
                stars
            FROM hotels
            ORDER BY stars DESC
            LIMIT 10
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data