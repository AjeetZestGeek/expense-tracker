"""Utility functions for converting domain models to API schemas."""

from expense_tracker.models import Expense
from expense_tracker.schemas import ExpenseResponse

def to_expense_response(
    expense: Expense,
    expense_id: int,
) -> ExpenseResponse:
    """Convert an Expense to an API response."""

    return ExpenseResponse(
        id = expense_id,
        amount = expense.amount,
        category = expense.category,
        description = expense.description,
        expense_date = expense.expense_date,
    )