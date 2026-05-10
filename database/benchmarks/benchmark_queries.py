import time
import json

import psycopg2


connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bookinghub",
    user="postgres",
    password="postgres"
)

cursor = connection.cursor()


QUERIES = {
    "available_flights": """
        SELECT
            f.id,
            f.flight_number,
            f.available_seats
        FROM flights f
        WHERE f.available_seats > 0
        ORDER BY f.departure_time
    """,

    "customer_history": """
        SELECT
            c.first_name,
            c.last_name,
            p.amount
        FROM customers c
        INNER JOIN payments p
            ON p.customer_id = c.id
        WHERE c.id = 1
    """,

    "hotel_occupancy": """
        SELECT
            h.name,
            COUNT(hr.id)
        FROM hotels h
        INNER JOIN hotel_reservations hr
            ON hr.hotel_id = h.id
        GROUP BY h.name
    """
}


def execute_benchmark(query_name, query):

    start = time.perf_counter()

    cursor.execute(query)

    cursor.fetchall()

    end = time.perf_counter()

    execution_time = round(
        end - start,
        6
    )

    print(
        f"{query_name}: {execution_time}s"
    )

    return {
        "query": query_name,
        "execution_time": execution_time
    }


def run():

    results = []

    for query_name, query in QUERIES.items():

        result = execute_benchmark(
            query_name,
            query
        )

        results.append(result)

    with open(
        "resultados/benchmark_results.json",
        "w"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )

    print("benchmark completed")


if __name__ == "__main__":

    run()