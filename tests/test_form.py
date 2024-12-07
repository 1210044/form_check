import pytest
from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_get_user_form_valid():
    response = client.post(
        "/get_form",
        params={
            "email": "alex@mail.ru",
            "phone": "+7 999 999 99 99",
            "name": "Alex",
            "description": "sdfdsf"
        }
    )

    assert response.status_code == 200
    json_response = response.json()
    assert json_response['name'] == 'UserForm'


def test_get_order_form_valid():
    response = client.post(
        "/get_form",
        params={
            "client_email": "alex@mail.ru",
            # "order_date": "01.01.2025",
            "order_date": "2025-01-01",
            "order_title": "Order 1",
        }
    )

    assert response.status_code == 200
    json_response = response.json()
    assert json_response['name'] == 'OrderForm'


if __name__ == "__main__":
    pytest.main()
