
import psycopg2


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
    SELECT COUNT(*)
    FROM flights
    """
)

before = cursor.fetchone()

print(before)

cursor.execute(
    """
    SELECT COUNT(*)
    FROM flights
    """
)

after = cursor.fetchone()

print(after)

connection.commit()

connection.close()