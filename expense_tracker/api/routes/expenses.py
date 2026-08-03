"""Expense API endpoints."""

from fastapi import APIRouter, Depends, status

from expense_tracker.api.dependencies import get_expense_manager
from expense_tracker.api.mappers import to_expense_response
from expense_tracker.manager import ExpenseManager
from expense_tracker.schemas import ExpenseCreate, ExpenseResponse

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


@router.get(
    "",
    response_model=list[ExpenseResponse],
    summary="Get all expenses",
)
def get_expenses(
    manager: ExpenseManager = Depends(get_expense_manager),
) -> list[ExpenseResponse]:
    """
    Return all expenses.
    """

    expenses = manager.get_all_expenses()

    return [
        ExpenseResponse(
            id=index,
            amount=expense.amount,
            category=expense.category,
            description=expense.description,
            expense_date=expense.expense_date,
        )
        for index, expense in enumerate(expenses)
    ]


@router.post(
    "",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create expense",
)
def create_expense(
    expense: ExpenseCreate,
    manager: ExpenseManager = Depends(get_expense_manager),
) -> ExpenseResponse:
    """Create a new expense."""

    created = manager.add_expense(
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        expense_date=expense.expense_date,
    )

    expenses = manager.get_all_expenses()
    expense_id = len(expenses) - 1

    return to_expense_response(created, expense_id)
