import pytest
from fastapi.testclient import TestClient

from expense_tracker.api.dependencies import get_expense_manager
from expense_tracker.app import app
from expense_tracker.manager import ExpenseManager
from expense_tracker.storage import JsonStorage


@pytest.fixture
def manager(tmp_path) -> ExpenseManager:
    """Return an ExpenseManager using temporary test storage."""
    storage = JsonStorage(tmp_path / "expenses.json")
    return ExpenseManager(storage)


@pytest.fixture
def client(manager: ExpenseManager):
    """Return a FastAPI test client using isolated test storage."""

    app.dependency_overrides[get_expense_manager] = lambda: manager

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()