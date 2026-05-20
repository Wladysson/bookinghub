from psycopg2.extras import RealDictCursor

from config.database import get_connection
from modules.pricing.engine import PricingEngine


class PricingService:

    @staticmethod
    def get_dynamic_price(flight_id: int):

        conn = get_connection()

        cursor = conn.cursor(
            cursor_factory=RealDictCursor
        )

        cursor.execute("""
            SELECT
                id,
                total_seats,
                available_seats,
                price
            FROM flights
            WHERE id = %s
        """, (flight_id,))

        flight = cursor.fetchone()

        cursor.close()
        conn.close()

        if not flight:
            return {
                "error": "Voo não encontrado"
            }

        return PricingEngine.calculate_dynamic_price(
            flight
        )