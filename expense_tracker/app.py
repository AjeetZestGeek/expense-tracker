from datetime import date

from expense_tracker.manager import ExpenseManager
from expense_tracker.storage import JsonStorage


def main():
    storage = JsonStorage("data/expenses.json")
    manager = ExpenseManager(storage)

    manager.add_expense(
        250,
        "Food",
        "Burger",
        date.today(),
    )

    manager.add_expense(
        120,
        "Travel",
        "Metro",
        date.today(),
    )

    print("\nAll Expenses\n")

    for expense in manager.get_all_expenses():
        print(expense)

    print("\nFood Expenses")

    for expense in manager.filter_by_category("Food"):
        print(expense)

    print(f"\nTotal: ₹{manager.total_expenses():.2f}")


if __name__ == "__main__":
    main()