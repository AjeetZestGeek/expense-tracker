from __future__ import annotations

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

    def delete_expense(self, index: int) -> Expense:
        expense = self.expenses.pop(index)
        self.storage.save(self.expenses)
        return expense

    def search(self, keyword: str) -> list[Expense]:
        keyword = keyword.lower()

        return [
            expense
            for expense in self.expenses
            if keyword in expense.category.lower()
            or keyword in expense.description.lower()
        ]

    def filter_by_category(self, category: str) -> list[Expense]:
        category = category.lower()

        return [
            expense for expense in self.expenses if expense.category.lower() == category
        ]

    def total_expenses(self) -> float:
        return sum(expense.amount for expense in self.expenses)

    def update_expense(
        self,
        index: int,
        amount: float | None = None,
        category: str | None = None,
        description: str | None = None,
        expense_date: date | None = None,
    ) -> Expense:
        """Update an existing expense."""
        expense = self.expenses[index]

        if amount is not None:
            expense.amount = validate_amount(amount)

        if category is not None:
            expense.category = validate_category(category)

        if description is not None:
            expense.description = validate_description(description)

        if expense_date is not None:
            expense.expense_date = validate_date(expense_date)

        self.storage.save(self.expenses)

        return expense

    def count_expenses(self) -> int:
        """Return the total number of expenses."""
        return len(self.expenses)

    def latest_expense(self) -> Expense | None:
        if not self.expenses:
            return None

        return self.expenses[-1]

    def expenses_by_date(
        self,
        expense_date: date,
    ) -> list[Expense]:
        """Return expenses for a specific date."""
        return [
            expense for expense in self.expenses if expense.expense_date == expense_date
        ]
