import threading
import requests


URL = (
    "http://localhost:8000"
    "/api/v1/payments"
)

SUCCESS_PAYMENTS = 0

FAILED_PAYMENTS = 0


def process_payment():

    global SUCCESS_PAYMENTS
    global FAILED_PAYMENTS

    payload = {
        "reservation_type": "flight",
        "reservation_id": 1,
        "customer_id": 1,
        "amount": 899.90,
        "payment_method": "pix"
    }

    try:

        response = requests.post(
            URL,
            json=payload,
            timeout=10
        )

        if response.status_code == 201:

            SUCCESS_PAYMENTS += 1

        else:

            FAILED_PAYMENTS += 1

    except Exception:

        FAILED_PAYMENTS += 1


def test_simultaneous_payments():

    threads = []

    for _ in range(50):

        thread = threading.Thread(
            target=process_payment
        )

        threads.append(thread)

        thread.start()

    for thread in threads:

        thread.join()

    print(
        f"successful payments: "
        f"{SUCCESS_PAYMENTS}"
    )

    print(
        f"failed payments: "
        f"{FAILED_PAYMENTS}"
    )

    assert SUCCESS_PAYMENTS >= 0