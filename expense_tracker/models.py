from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import date, datetime
from expense_tracker.utils import (
    validate_amount,
    validate_category,
    validate_date,
    validate_description,
)


@dataclass(slots=True)
class Expense:
    """Represents a single expense."""

    amount: float
    category: str
    description: str
    expense_date: date
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        self.amount = validate_amount(self.amount)
        self.category = validate_category(self.category)
        self.description = validate_description(self.description)
        self.expense_date = validate_date(self.expense_date)

    def to_dict(self) -> dict:
        """Convert the expense into a JSON-serializable dictionary."""
        return {
            "id": str(self.id),
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "expense_date": self.expense_date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        """Create an Expense object from a dictionary."""
        return cls(
            id=UUID(data["id"]),
            amount=float(data["amount"]),
            category=data["category"],
            description=data["description"],
            expense_date=datetime.strptime(data["expense_date"], "%Y-%m-%d").date(),
        )

    def __str__(self) -> str:
        return (
            f"{self.expense_date} | "
            f"{self.category:<12} | "
            f"₹{self.amount:.2f} | "
            f"{self.description}"
        )
