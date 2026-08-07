"""Expense API endpoints."""

from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException, Response

from expense_tracker.api.dependencies import get_expense_manager
from expense_tracker.api.mappers import to_expense_response
from expense_tracker.manager import ExpenseManager
from expense_tracker.schemas import ExpenseCreate, ExpenseResponse, ExpenseUpdate

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

    return [to_expense_response(expense) for expense in expenses]


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

    return to_expense_response(created)


@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
    summary="Get expense by ID",
)
def get_expense(
    expense_id: UUID,
    manager: ExpenseManager = Depends(get_expense_manager),
) -> ExpenseResponse:
    """
    Return a single expense by its UUID.
    """

    expense = manager.get_expense_by_id(expense_id)

    if expense is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    return to_expense_response(expense)


@router.put(
    "/{expense_id}",
    response_model=ExpenseResponse,
    summary="Update expense",
)
def update_expense(
    expense_id: UUID,
    expense_data: ExpenseUpdate,
    manager: ExpenseManager = Depends(get_expense_manager),
) -> ExpenseResponse:
    """
    Update an existing expense.
    """

    expense = manager.update_expense(
        expense_id=expense_id,
        amount=expense_data.amount,
        category=expense_data.category,
        description=expense_data.description,
        expense_date=expense_data.expense_date,
    )

    if expense is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    return to_expense_response(expense)


@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete expense",
)
def delete_expense(
    expense_id: UUID,
    manager: ExpenseManager = Depends(get_expense_manager),
) -> Response:
    """
    Delete an expense.
    """

    deleted = manager.delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
