from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_should_create_payment():

    response = client.post(
        "/api/v1/payments",
        json={
            "reservation_type": "flight",
            "reservation_id": 1,
            "customer_id": 1,
            "amount": 1200.00,
            "payment_method": "pix"
        }
    )

    assert response.status_code == 201

    body = response.json()

    assert body["status"] == "approved"


def test_should_list_payments():

    response = client.get(
        "/api/v1/payments"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )