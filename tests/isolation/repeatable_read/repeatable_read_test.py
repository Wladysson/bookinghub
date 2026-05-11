import psycopg2
import threading
import time


def reader():

    connection = psycopg2.connect(
        host="localhost",
        database="bookinghub",
        user="booking",
        password="secret"
    )

    connection.set_session(
        isolation_level="REPEATABLE READ"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT available_rooms
        FROM hotels
        WHERE id = 1
        """
    )

    first = cursor.fetchone()

    print(first)

    time.sleep(5)

    cursor.execute(
        """
        SELECT available_rooms
        FROM hotels
        WHERE id = 1
        """
    )

    second = cursor.fetchone()

    print(second)

    connection.commit()

    connection.close()


def writer():

    time.sleep(1)

    connection = psycopg2.connect(
        host="localhost",
        database="bookinghub",
        user="booking",
        password="secret"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE hotels
        SET available_rooms =
        available_rooms - 5
        WHERE id = 1
        """
    )

    connection.commit()

    connection.close()


t1 = threading.Thread(target=reader)

t2 = threading.Thread(target=writer)

t1.start()

t2.start()

t1.join()

t2.join()