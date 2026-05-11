import threading
import requests


URL = (
    "http://127.0.0.1:8000"
    "/api/v1/reservations/flights"
)

SUCCESS = 0

FAILED = 0


def reserve():

    global SUCCESS
    global FAILED

    payload = {
        "customer_id": 1,
        "flight_id": 1,
        "seats_reserved": 1
    }

    try:

        response = requests.post(
            URL,
            json=payload,
            timeout=5
        )

        if response.status_code == 201:

            SUCCESS += 1

        else:

            FAILED += 1

    except Exception:

        FAILED += 1


threads = []

for _ in range(500):

    thread = threading.Thread(
        target=reserve
    )

    threads.append(thread)

    thread.start()

for thread in threads:

    thread.join()

print(f"success: {SUCCESS}")

print(f"failed: {FAILED}")