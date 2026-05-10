import threading
import requests


URL = (
    "http://localhost:8000"
    "/api/v1/reservations/flights"
)

SUCCESS = 0

FAILURES = 0


def reserve_seat():

    global SUCCESS
    global FAILURES

    payload = {
        "customer_id": 1,
        "flight_id": 1,
        "seats_reserved": 1
    }

    try:

        response = requests.post(
            URL,
            json=payload,
            timeout=10
        )

        if response.status_code == 201:

            SUCCESS += 1

        else:

            FAILURES += 1

    except Exception:

        FAILURES += 1


def test_overbooking():

    threads = []

    for _ in range(100):

        thread = threading.Thread(
            target=reserve_seat
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()

    print(f"successful reservations: {SUCCESS}")

    print(f"failed reservations: {FAILURES}")

    assert SUCCESS <= 100