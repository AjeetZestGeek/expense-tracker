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


def test_get_expense_by_id(client):
    expenses = client.get("/expenses").json()

    expense_id = expenses[0]["id"]

    response = client.get(f"/expenses/{expense_id}")

    assert response.status_code == 200

    assert response.json()["id"] == expense_id


def test_update_expense(client):
    expenses = client.get("/expenses").json()

    expense_id = expenses[0]["id"]

    payload = {
        "amount": 999,
        "category": "Shopping",
        "description": "Keyboard",
        "expense_date": "2026-08-07",
    }

    response = client.put(
        f"/expenses/{expense_id}",
        json=payload,
    )

    assert response.status_code == 200
    assert response.json()["amount"] == 999

def test_delete_expense(client):
    expenses = client.get("/expenses").json()

    expense_id = expenses[0]["id"]

    response = client.delete(f"/expenses/{expense_id}")

    assert response.status_code == 204

    response = client.get(f"/expenses/{expense_id}")

    assert response.status_code == 404