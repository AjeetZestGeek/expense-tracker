from __future__ import annotations

import json
from pathlib import Path

from expense_tracker.exceptions import StorageError
from expense_tracker.models import Expense


class JsonStorage:
    """Handles saving and loading expenses."""

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def load(self) -> list[Expense]:
        """Load expenses from JSON."""

        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            return [Expense.from_dict(item) for item in data]

        except json.JSONDecodeError as exc:
            raise StorageError("Invalid JSON file.") from exc

        except Exception as exc:
            raise StorageError(str(exc)) from exc

    def save(self, expenses: list[Expense]) -> None:
        """Save expenses to JSON."""

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump(
                    [expense.to_dict() for expense in expenses],
                    file,
                    indent=4,
                )

        except Exception as exc:
            raise StorageError(str(exc)) from exc