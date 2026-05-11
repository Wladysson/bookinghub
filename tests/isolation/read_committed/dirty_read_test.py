import psycopg2
import threading
import time


def transaction_one():

    connection = psycopg2.connect(
        host="localhost",
        database="bookinghub",
        user="booking",
        password="secret"
    )

    connection.set_session(
        isolation_level="READ COMMITTED"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE flights
        SET available_seats = 5
        WHERE id = 1
        """
    )

    print("transaction one updated")

    time.sleep(5)

    connection.rollback()

    connection.close()


def transaction_two():

    time.sleep(1)

    connection = psycopg2.connect(
        host="localhost",
        database="bookinghub",
        user="booking",
        password="secret"
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

    print(cursor.fetchone())

    connection.close()


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