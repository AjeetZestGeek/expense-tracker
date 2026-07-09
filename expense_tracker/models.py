from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime


@dataclass(slots=True)
class Expense:
    """Represents a single expense."""

    amount: float
    category: str
    description: str
    expense_date: date

    def __post_init__(self) -> None:
        """Validate the expense after initialization."""
        if self.amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.category = self.category.strip()
        self.description = self.description.strip()

        if not self.category:
            raise ValueError("Category cannot be empty.")

        if not self.description:
            raise ValueError("Description cannot be empty.")

    def to_dict(self) -> dict:
        """Convert the expense into a JSON-serializable dictionary."""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "expense_date": self.expense_date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        """Create an Expense object from a dictionary."""
        return cls(
            amount=float(data["amount"]),
            category=data["category"],
            description=data["description"],
            expense_date=datetime.strptime(
                data["expense_date"], "%Y-%m-%d"
            ).date(),
        )

    def __str__(self) -> str:
        return (
            f"{self.expense_date} | "
            f"{self.category:<12} | "
            f"₹{self.amount:.2f} | "
            f"{self.description}"
        )