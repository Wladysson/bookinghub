import psycopg2
from pprint import pprint


connection = psycopg2.connect(
    host="localhost",
    database="bookinghub",
    user="booking",
    password="secret"
)

cursor = connection.cursor()


QUERIES = {

    "available_flights": """
        EXPLAIN ANALYZE
        SELECT *
        FROM flights
        WHERE available_seats > 0
        ORDER BY departure_time
    """,

    "customer_history": """
        EXPLAIN ANALYZE
        SELECT *
        FROM flight_reservations
        WHERE customer_id = 1
    """,

    "hotel_search": """
        EXPLAIN ANALYZE
        SELECT *
        FROM hotels
        WHERE available_rooms > 0
    """
}


for name, query in QUERIES.items():

    print("\n")
    print("=" * 60)

    print(f"QUERY: {name}")

    print("=" * 60)

    cursor.execute(query)

    result = cursor.fetchall()

    pprint(result)

    print("\n")


connection.close()