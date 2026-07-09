from expense_tracker.manager import ExpenseManager
from expense_tracker.storage import JsonStorage

import pytest


@pytest.fixture
def manager(tmp_path):
    storage = JsonStorage(tmp_path / "expenses.json")
    return ExpenseManager(storage)