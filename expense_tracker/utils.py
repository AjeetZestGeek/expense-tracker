from __future__ import annotations

from datetime import date


def validate_amount(amount: float) -> float:
    """Validate the expense amount."""
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number.")

    amount = float(amount)

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    return amount


def validate_category(category: str) -> str:
    """Validate the expense category."""
    if not isinstance(category, str):
        raise TypeError("Category must be a string.")

    category = category.strip()

    if not category:
        raise ValueError("Category cannot be empty.")

    return category


def validate_description(description: str) -> str:
    """Validate the expense description."""
    if not isinstance(description, str):
        raise TypeError("Description must be a string.")

    description = description.strip()

    if not description:
        raise ValueError("Description cannot be empty.")

    return description


def validate_date(expense_date: date) -> date:
    """Validate the expense date."""
    if not isinstance(expense_date, date):
        raise TypeError("expense_date must be a datetime.date instance.")

    return expense_date