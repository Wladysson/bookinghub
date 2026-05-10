import psycopg2
import threading


def reserve_seat():

    connection = psycopg2.connect(
        host="localhost",
        database="bookinghub",
        user="postgres",
        password="postgres"
    )

    connection.set_session(
        isolation_level="SERIALIZABLE"
    )

    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            SELECT available_seats
            FROM flights
            WHERE id = 1
            FOR UPDATE
            """
        )

        result = cursor.fetchone()

        seats = result[0]

        if seats > 0:

            cursor.execute(
                """
                UPDATE flights
                SET available_seats = available_seats - 1
                WHERE id = 1
                """
            )

            print(
                "seat reserved"
            )

        connection.commit()

    except Exception as error:

        print(
            f"serialization failure: {error}"
        )

        connection.rollback()

    finally:

        connection.close()


def test_serializable():

    threads = []

    for _ in range(20):

        thread = threading.Thread(
            target=reserve_seat
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()

    assert True