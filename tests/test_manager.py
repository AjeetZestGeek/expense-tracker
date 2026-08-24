from datetime import date


def test_add_expense(manager):
    manager.add_expense(
        500,
        "Food",
        "Pizza",
        date.today(),
    )

    assert len(manager.get_all_expenses()) == 1


def test_total_expenses(manager):
    manager.add_expense(100, "Food", "Pizza", date.today())
    manager.add_expense(200, "Travel", "Bus", date.today())

    assert manager.total_expenses() == 300


def test_search(manager):
    manager.add_expense(
        400,
        "Shopping",
        "Shoes",
        date.today(),
    )

    results = manager.search_expenses("shoe")

    assert len(results) == 1
    assert manager.search_expenses("Laptop") == []


def test_filter(manager):
    manager.add_expense(
        100,
        "Food",
        "Pizza",
        date.today(),
    )

    manager.add_expense(
        200,
        "Travel",
        "Metro",
        date.today(),
    )

    food = manager.filter_by_category("Food")

    assert len(food) == 1


def test_delete(manager):
    expense = manager.add_expense(
        100,
        "Food",
        "Pizza",
        date.today(),
    )

    manager.delete_expense(expense.id)

    assert len(manager.get_all_expenses()) == 0


def test_search_not_found(manager):
    manager.add_expense(
        200,
        "Travel",
        "Bus",
        date.today(),
    )

    assert manager.search_expenses("Laptop") == []


def test_update_expense(manager):
    expense = manager.add_expense(
        100,
        "Food",
        "Pizza",
        date.today(),
    )

    updated = manager.update_expense(
        expense.id,
        amount=250,
        description="Burger",
    )

    assert updated.amount == 250
    assert updated.description == "Burger"
    assert updated.category == "Food"


def test_empty_total(manager):
    assert manager.total_expenses() == 0


def test_count_expenses(manager):
    assert manager.count_expenses() == 0

    manager.add_expense(
        100,
        "Food",
        "Pizza",
        date.today(),
    )

    assert manager.count_expenses() == 1


def test_latest_expense(manager):
    manager.add_expense(
        100,
        "Food",
        "Pizza",
        date.today(),
    )

    manager.add_expense(
        200,
        "Travel",
        "Metro",
        date.today(),
    )

    latest = manager.latest_expense()

    assert latest.description == "Metro"


def test_expenses_by_date(manager):
    today = date.today()

    manager.add_expense(
        100,
        "Food",
        "Pizza",
        today,
    )

    manager.add_expense(
        200,
        "Travel",
        "Bus",
        today,
    )

    expenses = manager.expenses_by_date(today)

    assert len(expenses) == 2
