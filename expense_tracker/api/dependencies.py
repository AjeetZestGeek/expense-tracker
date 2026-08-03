"""Shared API dependencies."""

from pathlib import Path

from expense_tracker.manager import ExpenseManager
from expense_tracker.storage import JsonStorage

DATA_FILE = Path("data") / "expenses.json"

def get_expense_manager() -> ExpenseManager:
    """
    Return a configured ExpenseManager instance.
    """
    storage = JsonStorage(DATA_FILE)
    return ExpenseManager(storage)