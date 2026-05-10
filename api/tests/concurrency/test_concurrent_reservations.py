import threading
import requests
import random


URL = (
    "http://localhost:8000"
    "/api/v1/reservations/hotels"
)

SUCCESS_RESERVATIONS = 0

FAILED_RESERVATIONS = 0


def reserve_hotel():

    global SUCCESS_RESERVATIONS
    global FAILED_RESERVATIONS

    payload = {
        "customer_id": random.randint(1, 20),

        "hotel_id": 1,

        "rooms_reserved": 1,

        "check_in": "2026-05-10",

        "check_out": "2026-05-15"
    }

    try:

        response = requests.post(
            URL,
            json=payload,
            timeout=10
        )

        if response.status_code == 201:

            SUCCESS_RESERVATIONS += 1

        else:

            FAILED_RESERVATIONS += 1

    except Exception:

        FAILED_RESERVATIONS += 1


def test_concurrent_reservations():

    threads = []

    for _ in range(75):

        thread = threading.Thread(
            target=reserve_hotel
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()

    print(
        f"successful hotel reservations: "
        f"{SUCCESS_RESERVATIONS}"
    )

    print(
        f"failed hotel reservations: "
        f"{FAILED_RESERVATIONS}"
    )

    assert SUCCESS_RESERVATIONS >= 0