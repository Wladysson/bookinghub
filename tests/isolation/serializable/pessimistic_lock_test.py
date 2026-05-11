import psycopg2
import time


connection = psycopg2.connect(
    host="localhost",
    database="bookinghub",
    user="booking",
    password="secret"
)

cursor = connection.cursor()

cursor.execute(
    """
    BEGIN;
    """
)

cursor.execute(
    """
    SELECT *
    FROM flights
    WHERE id = 1
    FOR UPDATE
    """
)

print("row locked")

time.sleep(10)

connection.commit()

connection.close()

print("lock released")