from fastapi.testclient import TestClient

from expense_tracker.app import app

client = TestClient(app)


def test_get_expenses_returns_success() -> None:
    response = client.get("/expenses")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_expense() -> None:
    payload = {
        "amount": 250,
        "category": "Food",
        "description": "Burger",
        "expense_date": "2026-08-03",
    }

    response = client.post("/expenses", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["amount"] == 250
    assert data["category"] == "Food"
    assert data["description"] == "Burger"
