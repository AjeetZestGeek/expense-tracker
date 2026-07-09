from datetime import date

import pytest

from expense_tracker.utils import (
    validate_amount,
    validate_category,
    validate_date,
    validate_description,
)

@pytest.mark.parametrize(
    "amount",
    [1, 50, 99.99, 1000],
)
def test_validate_amount_success(amount):
    assert validate_amount(amount) == float(amount)

@pytest.mark.parametrize(
    "amount",
    [0, -1, -500],
)
def test_validate_amount_invalid(amount):
    with pytest.raises(ValueError):
        validate_amount(amount)

@pytest.mark.parametrize(
    "amount",
    ["abc", None, [], {}],
)
def test_validate_amount_type(amount):
    with pytest.raises(TypeError):
        validate_amount(amount)

@pytest.mark.parametrize(
    "category",
    [
        "Food",
        "Travel",
        "Shopping",
    ],
)
def test_validate_category_success(category):
    assert validate_category(category) == category

@pytest.mark.parametrize(
    "category",
    [
        "",
        " ",
        "     ",
    ],
)
def test_validate_category_empty(category):
    with pytest.raises(ValueError):
        validate_category(category)

@pytest.mark.parametrize(
    "description",
    [
        "Pizza",
        "Movie Ticket",
        "Bus Fare",
    ],
)
def test_validate_description_success(description):
    assert validate_description(description) == description

@pytest.mark.parametrize(
    "description",
    [
        "",
        " ",
    ],
)
def test_validate_description_empty(description):
    with pytest.raises(ValueError):
        validate_description(description)

def test_validate_date():
    today = date.today()
    assert validate_date(today) == today

@pytest.mark.parametrize(
    "value",
    [
        "2026-07-09",
        None,
        123,
        {},
        [],
    ],
)
def test_validate_date_invalid(value):
    with pytest.raises(TypeError):
        validate_date(value)