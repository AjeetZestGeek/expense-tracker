from datetime import date

import pytest

from expense_tracker.models import Expense


def test_create_expense():
    expense = Expense(
        amount=500,
        category="Food",
        description="Lunch",
        expense_date=date(2026, 7, 9),
    )

    assert expense.amount == 500
    assert expense.category == "Food"
    assert expense.description == "Lunch"


def test_invalid_amount():
    with pytest.raises(ValueError):
        Expense(
            amount=0,
            category="Food",
            description="Lunch",
            expense_date=date.today(),
        )


def test_empty_category():
    with pytest.raises(ValueError):
        Expense(
            amount=100,
            category="",
            description="Lunch",
            expense_date=date.today(),
        )


def test_empty_description():
    with pytest.raises(ValueError):
        Expense(
            amount=100,
            category="Food",
            description="",
            expense_date=date.today(),
        )


def test_to_dict():
    expense = Expense(
        amount=300,
        category="Travel",
        description="Metro",
        expense_date=date(2026, 7, 9),
    )

    data = expense.to_dict()

    assert data["amount"] == 300
    assert data["category"] == "Travel"
    assert data["expense_date"] == "2026-07-09"


def test_from_dict():
    data = {
        "amount": 450,
        "category": "Shopping",
        "description": "Shoes",
        "expense_date": "2026-07-09",
    }

    expense = Expense.from_dict(data)

    assert expense.amount == 450
    assert expense.category == "Shopping"