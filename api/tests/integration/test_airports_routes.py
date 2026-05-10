from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_should_create_airport():

    response = client.post(
        "/api/v1/airports",
        json={
            "code": "FOR",
            "name": "Pinto Martins International Airport",
            "city": "Fortaleza",
            "country": "Brazil"
        }
    )

    assert response.status_code == 201

    body = response.json()

    assert body["code"] == "FOR"

    assert body["city"] == "Fortaleza"


def test_should_list_airports():

    response = client.get(
        "/api/v1/airports"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )