import threading
import psycopg2


def reserve():

    connection = psycopg2.connect(
        host="localhost",
        database="bookinghub",
        user="booking",
        password="secret"
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

        cursor.execute(
            """
            UPDATE flights
            SET available_seats =
            available_seats - 1
            WHERE id = 1
            """
        )

        connection.commit()

        print("reservation success")

    except Exception as error:

        print(error)

        connection.rollback()

    finally:

        connection.close()


threads = []

for _ in range(50):

    thread = threading.Thread(
        target=reserve
    )

    threads.append(thread)

    thread.start()

for thread in threads:

    thread.join()