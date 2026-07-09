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

    results = manager.search("shoe")

    assert len(results) == 1

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
    manager.add_expense(
        100,
        "Food",
        "Pizza",
        date.today(),
    )

    manager.delete_expense(0)

    assert len(manager.get_all_expenses()) == 0

def test_search_not_found(manager):
    manager.add_expense(
        200,
        "Travel",
        "Bus",
        date.today(),
    )

    assert manager.search("Laptop") == []

def test_empty_total(manager):
    assert manager.total_expenses() == 0