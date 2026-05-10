import random
import uuid

from faker import Faker

import psycopg2

fake = Faker()


connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bookinghub",
    user="postgres",
    password="postgres"
)

cursor = connection.cursor()


def seed_customers(total=1000):

    for _ in range(total):

        cursor.execute(
            """
            INSERT INTO customers (
                first_name,
                last_name,
                email,
                phone,
                document_number,
                nationality
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                fake.phone_number(),
                str(uuid.uuid4()),
                fake.country()
            )
        )

    connection.commit()

    print(f"{total} customers created")


def seed_airports():

    airports = [
        ("GRU", "Guarulhos", "São Paulo", "Brazil"),
        ("FOR", "Fortaleza", "Fortaleza", "Brazil"),
        ("GIG", "Galeão", "Rio de Janeiro", "Brazil"),
        ("JFK", "John F Kennedy", "New York", "USA")
    ]

    for airport in airports:

        cursor.execute(
            """
            INSERT INTO airports (
                code,
                name,
                city,
                country
            )
            VALUES (%s, %s, %s, %s)
            """,
            airport
        )

    connection.commit()

    print("airports created")


if __name__ == "__main__":

    seed_customers(1000)

    seed_airports()

    cursor.close()
    connection.close()