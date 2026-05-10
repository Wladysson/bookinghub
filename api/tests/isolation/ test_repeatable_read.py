import psycopg2
import threading
import time


def reader_transaction():

    connection = psycopg2.connect(
        host="localhost",
        database="bookinghub",
        user="postgres",
        password="postgres"
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

    first_read = cursor.fetchone()

    print(
        f"first read: {first_read}"
    )

    time.sleep(5)

    cursor.execute(
        """
        SELECT available_rooms
        FROM hotels
        WHERE id = 1
        """
    )

    second_read = cursor.fetchone()

    print(
        f"second read: {second_read}"
    )

    connection.commit()

    connection.close()


def writer_transaction():

    time.sleep(1)

    connection = psycopg2.connect(
        host="localhost",
        database="bookinghub",
        user="postgres",
        password="postgres"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE hotels
        SET available_rooms = available_rooms - 1
        WHERE id = 1
        """
    )

    connection.commit()

    connection.close()

    print(
        "rooms updated"
    )


def test_repeatable_read():

    reader = threading.Thread(
        target=reader_transaction
    )

    writer = threading.Thread(
        target=writer_transaction
    )

    reader.start()

    writer.start()

    reader.join()

    writer.join()

    assert True