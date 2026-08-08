from __future__ import annotations

from uuid import UUID
from datetime import date

from expense_tracker.models import Expense
from expense_tracker.storage import JsonStorage

from expense_tracker.utils import (
    validate_amount,
    validate_category,
    validate_description,
    validate_date,
)


class ExpenseManager:
    """Business logic for managing expenses."""

    def __init__(self, storage: JsonStorage):
        self.storage = storage
        self.expenses = self.storage.load()

    def add_expense(
        self,
        amount: float,
        category: str,
        description: str,
        expense_date: date,
    ) -> Expense:
        expense = Expense(
            amount=amount,
            category=category,
            description=description,
            expense_date=expense_date,
        )

        self.expenses.append(expense)
        self.storage.save(self.expenses)

        return expense

    def get_all_expenses(self) -> list[Expense]:
        return list(self.expenses)

    def get_expense_by_id(self, expense_id: UUID) -> Expense | None:
        """
        Return an expense by its UUID.

        Args:
            expense_id: UUID of the expense.

        Returns:
            Expense if found, otherwise None.
        """

        for expense in self.expenses:
            if expense.id == expense_id:
                return expense

        return None

    def delete_expense(self, expense_id: UUID) -> bool:
        """
        Delete an expense by UUID.

        Args:
            expense_id: UUID of the expense.

        Returns:
            True if deleted, otherwise False.
        """

        expense = self.get_expense_by_id(expense_id)

        if expense is None:
            return False

        self.expenses.remove(expense)
        self.storage.save(self.expenses)

        return True

    def search_expenses(self, query: str) -> list[Expense]:
        """
        Search expenses by category or description.
        """

        query = query.strip().lower()

        return [
            expense
            for expense in self.expenses
            if query in expense.category.lower() or query in expense.description.lower()
        ]

    def filter_by_category(self, category: str) -> list[Expense]:
        """
        Return expenses matching the given category.

        Args:
            category: Category to filter by.

        Returns:
            List of matching expenses.
        """
        category = category.strip().lower()

        return [
            expense for expense in self.expenses if expense.category.lower() == category
        ]

    def total_expenses(self) -> float:
        """Return the total amount of all expenses."""
        return sum(expense.amount for expense in self.expenses)

    def update_expense(
        self,
        expense_id: UUID,
        amount: float | None = None,
        category: str | None = None,
        description: str | None = None,
        expense_date: date | None = None,
    ) -> Expense | None:
        """
        Update an existing expense by UUID.
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

    def count_expenses(self) -> int:
        """Return the number of expenses."""
        return len(self.expenses)

    def latest_expense(self) -> Expense | None:
        """
        Return the most recent expense.

        Returns:
            The latest expense, or None if no expenses exist.
        """
        if not self.expenses:
            return None

        return max(
            self.expenses,
            key=lambda expense: expense.expense_date,
        )

    def expenses_by_date(self, expense_date: date) -> list[Expense]:
        """
        Return expenses for a specific date.

        Args:
            expense_date: Date to filter expenses by.

        Returns:
            List of matching expenses.
        """
        return [
            expense for expense in self.expenses if expense.expense_date == expense_date
        ]
