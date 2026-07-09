from datetime import date

from expense_tracker.models import Expense


def main():
    expense = Expense(
        amount=250,
        category="Food",
        description="Pizza",
        expense_date=date.today(),
    )

    print(expense)
    print(expense.to_dict())


if __name__ == "__main__":
    main()