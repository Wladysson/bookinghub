import threading
import psycopg2


def update_seats():

    connection = psycopg2.connect(
        host="localhost",
        database="bookinghub",
        user="booking",
        password="secret"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE flights
        SET available_seats =
        available_seats - 1
        WHERE id = 1
        """
    )

    connection.commit()

    connection.close()

    print("seat updated")


threads = []

for _ in range(20):

    thread = threading.Thread(
        target=update_seats
    )

    threads.append(thread)

    thread.start()

for thread in threads:

    thread.join()