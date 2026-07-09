from datetime import date

from expense_tracker.models import Expense
from expense_tracker.storage import JsonStorage


def main():
    storage = JsonStorage("data/expenses.json")

    expenses = [
        Expense(
            amount=300,
            category="Food",
            description="Pizza",
            expense_date=date.today(),
        ),
        Expense(
            amount=120,
            category="Travel",
            description="Metro",
            expense_date=date.today(),
        ),
    ]

    storage.save(expenses)

    loaded = storage.load()

    print("Saved Expenses")

    for expense in loaded:
        print(expense)


if __name__ == "__main__":
    main()