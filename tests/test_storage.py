from datetime import date

import pytest

from expense_tracker.exceptions import StorageError
from expense_tracker.models import Expense
from expense_tracker.storage import JsonStorage

def test_save_expenses(tmp_path):
    file = tmp_path / "expenses.json"

    storage = JsonStorage(file)

    expenses = [
        Expense(
            100,
            "Food",
            "Pizza",
            date.today(),
        )
    ]

    storage.save(expenses)

    assert file.exists()

def test_load_expenses(tmp_path):
    file = tmp_path / "expenses.json"

    storage = JsonStorage(file)

    expenses = [
        Expense(
            200,
            "Travel",
            "Bus",
            date.today(),
        )
    ]

    storage.save(expenses)

    loaded = storage.load()

    assert len(loaded) == 1
    assert loaded[0].amount == 200

def test_missing_file_returns_empty_list(tmp_path):
    file = tmp_path / "missing.json"

    storage = JsonStorage(file)

    assert storage.load() == []

def test_invalid_json(tmp_path):
    file = tmp_path / "expenses.json"

    file.write_text("{invalid json}")

    storage = JsonStorage(file)

    with pytest.raises(StorageError):
        storage.load()

def test_empty_file(tmp_path):
    file = tmp_path / "expenses.json"

    file.write_text("")

    storage = JsonStorage(file)

    with pytest.raises(StorageError):
        storage.load()

def test_multiple_expenses(tmp_path):
    file = tmp_path / "expenses.json"

    storage = JsonStorage(file)

    expenses = [
        Expense(
            100,
            "Food",
            "Pizza",
            date.today(),
        ),
        Expense(
            300,
            "Travel",
            "Taxi",
            date.today(),
        ),
    ]

    storage.save(expenses)

    loaded = storage.load()

    assert len(loaded) == 2

def test_example(tmp_path):
    file = tmp_path / "demo.txt"

    file.write_text("Hello")

    assert file.exists()