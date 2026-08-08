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


def test_filter_expenses_by_category(client):
    response = client.get("/expenses/category/Food")

    assert response.status_code == 200

    expenses = response.json()

    assert all(expense["category"].lower() == "food" for expense in expenses)


def test_filter_expenses_by_unknown_category(client):
    response = client.get("/expenses/category/Unknown")

    assert response.status_code == 200
    assert response.json() == []


def test_get_expenses_by_date(client):
    response = client.get("/expenses/date/2026-08-05")

    assert response.status_code == 200

    expenses = response.json()

    assert all(expense["expense_date"] == "2026-08-05" for expense in expenses)


def test_get_expenses_by_date_no_results(client):
    response = client.get("/expenses/date/2030-01-01")

    assert response.status_code == 200
    assert response.json() == []


def test_get_total_expenses(client):
    response = client.get("/expenses/total")

    assert response.status_code == 200

    data = response.json()

    assert "total" in data
    assert isinstance(data["total"], (int, float))


def test_get_total_expenses(client):
    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 10668.0


def test_get_expense_count(client):
    response = client.get("/expenses/count")

    assert response.status_code == 200

    data = response.json()

    assert "count" in data
    assert isinstance(data["count"], int)
    assert data["count"] >= 0


def test_get_latest_expense(client):
    response = client.get("/expenses/latest")

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "amount" in data
    assert "category" in data
    assert "description" in data
    assert "expense_date" in data


def test_get_latest_expense_when_empty(client):
    # This test should use an isolated empty storage fixture.
    response = client.get("/expenses/latest")

    assert response.status_code == 404
    assert response.json()["detail"] == "No expenses found"
