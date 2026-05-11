import threading
import requests
import random


URL = (
    "http://127.0.0.1:8000"
    "/api/v1/reservations/hotels"
)


def reserve_room(customer_id):

    payload = {
        "customer_id": customer_id,
        "hotel_id": 1,
        "rooms_reserved": 1,
        "check_in": "2026-06-01",
        "check_out": "2026-06-10"
    }

    response = requests.post(
        URL,
        json=payload
    )

    print(
        customer_id,
        response.status_code
    )


threads = []

for i in range(300):

    thread = threading.Thread(
        target=reserve_room,
        args=(random.randint(1, 1000),)
    )

    threads.append(thread)

    thread.start()

for thread in threads:

    thread.join()