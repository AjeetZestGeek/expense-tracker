from __future__ import annotations

from datetime import date

from expense_tracker.models import Expense
from expense_tracker.storage import JsonStorage


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
            expense
            for expense in self.expenses
            if expense.category.lower() == category
        ]

    def total_expenses(self) -> float:
        return sum(expense.amount for expense in self.expenses)