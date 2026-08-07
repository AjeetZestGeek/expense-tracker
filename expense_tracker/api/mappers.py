"""Utility functions for converting domain models to API schemas."""

from uuid import UUID
from datetime import date

from expense_tracker.models import Expense
from expense_tracker.schemas import ExpenseResponse


def to_expense_response(expense: Expense) -> ExpenseResponse:
    """Convert an Expense to an API response."""

    return ExpenseResponse(
        id=expense.id,
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        expense_date=expense.expense_date,
    )


def update_expense(
    self,
    expense_id: UUID,
    amount: float | None = None,
    category: str | None = None,
    description: str | None = None,
    expense_date: date | None = None,
) -> Expense | None:
    """
    Update an expense by UUID.
    """

    expense = self.get_expense_by_id(expense_id)

    if expense is None:
        return None

    if amount is not None:
        expense.amount = amount

    if category is not None:
        expense.category = category

    if description is not None:
        expense.description = description

    if expense_date is not None:
        expense.expense_date = expense_date

    self.storage.save(self.expenses)

    return expense
