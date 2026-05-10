import psycopg2
import threading
import time


def transaction_one():

    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="bookinghub",
        user="postgres",
        password="postgres"
    )

    connection.set_session(
        isolation_level="READ COMMITTED"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE flights
        SET available_seats = available_seats - 1
        WHERE id = 1
        """
    )

    print(
        "transaction one updated seats"
    )

    time.sleep(5)

    connection.commit()

    connection.close()


def transaction_two():

    time.sleep(1)

    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="bookinghub",
        user="postgres",
        password="postgres"
    )

    connection.set_session(
        isolation_level="READ COMMITTED"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT available_seats
        FROM flights
        WHERE id = 1
        """
    )

    result = cursor.fetchone()

    print(
        f"visible seats: {result}"
    )

    connection.close()


def test_read_committed():

    t1 = threading.Thread(
        target=transaction_one
    )

    t2 = threading.Thread(
        target=transaction_two
    )

    t1.start()

    t2.start()

    t1.join()

    t2.join()

    assert True