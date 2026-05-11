import time
import psycopg2


connection = psycopg2.connect(
    host="localhost",
    database="bookinghub",
    user="booking",
    password="secret"
)

cursor = connection.cursor()


QUERIES = [

    (
        "available_flights",

        """
        SELECT *
        FROM flights
        WHERE available_seats > 0
        """
    ),

    (
        "available_hotels",

        """
        SELECT *
        FROM hotels
        WHERE available_rooms > 0
        """
    ),

    (
        "payments",

        """
        SELECT *
        FROM payments
        WHERE status = 'approved'
        """
    )
]


for name, query in QUERIES:

    start = time.perf_counter()

    for _ in range(100):

        cursor.execute(query)

        cursor.fetchall()

    end = time.perf_counter()

    total = end - start

    print("\n")

    print(f"query: {name}")

    print(f"time: {total:.4f}s")


connection.close()