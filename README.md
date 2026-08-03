# Expense Tracker CLI – Project Context

## Project Goal

Build a production-quality Python command-line Expense Tracker that demonstrates modern Python development practices, clean architecture, and comprehensive testing using **pytest**.

The project is being developed incrementally in phases. Each phase should include:

* Clean, maintainable code
* Type hints
* Proper documentation (docstrings)
* Unit tests with `pytest`
* Explanation of important concepts
* Interview-level best practices
* Git commit message after each phase

The assistant should act as a senior Python mentor, explaining **why** something is implemented in a particular way instead of only providing code.

---

# Technology Stack

* Python 3.12+
* pytest
* pytest-cov
* JSON
* pathlib
* dataclasses
* typing
* datetime

Future additions:

* logging
* csv
* black
* ruff
* pre-commit
* GitHub Actions
* Docker (optional)

---

# Project Structure

```text
expense-tracker/

│
├── expense_tracker/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── manager.py
│   ├── storage.py
│   ├── utils.py
│   ├── report.py
│   ├── logger.py
│   └── exceptions.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_utils.py
│   ├── test_storage.py
│   └── test_manager.py
│
├── data/
│   └── expenses.json
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

---

# Completed Phases

## ✅ Phase 1 – Project Setup

Completed:

* Project structure
* Virtual environment
* requirements.txt
* pytest configuration
* .gitignore
* Git initialization
* Package structure

Learned:

* Python packages
* Virtual environments
* Project organization

---

## ✅ Phase 2 – Expense Model

Implemented:

* Expense dataclass
* Validation
* to_dict()
* from_dict()
* **str**()
* Type hints

Testing:

* Model creation
* Invalid values
* Serialization

Learned:

* dataclasses
* **post_init**
* Class methods
* Object serialization

---

## ✅ Phase 3 – Validation Utilities

Created:

* validate_amount()
* validate_category()
* validate_description()
* validate_date()

Refactored:

* Expense model now uses reusable validators.

Testing:

* pytest.mark.parametrize
* Type validation
* Value validation

Learned:

* Separation of Concerns
* Single Responsibility Principle (SRP)
* Reusable functions

---

## ✅ Phase 4 – JSON Storage

Created:

JsonStorage

Implemented:

* load()
* save()

Features:

* JSON persistence
* pathlib
* StorageError exception
* Missing file handling
* Invalid JSON handling

Testing:

* tmp_path fixture
* File operations
* Corrupted JSON
* Empty files

Learned:

* File handling
* JSON
* pathlib
* Persistence layer

---

## ✅ Phase 5 – Expense Manager

Created:

ExpenseManager

Implemented:

* add_expense()
* get_all_expenses()
* delete_expense()
* search()
* filter_by_category()
* total_expenses()

Additional challenge methods implemented:

* update_expense()
* count_expenses()
* latest_expense()
* expenses_by_date()

Business Logic:

ExpenseManager sits between the CLI and the storage layer.

Architecture:

CLI
↓
ExpenseManager
↓
JsonStorage
↓
expenses.json

Testing:

* CRUD operations
* Search
* Filter
* Total calculation
* Fixtures using conftest.py

Learned:

* Service Layer pattern
* Business logic
* CRUD
* Aggregation
* Shared pytest fixtures

---

# Current Architecture

```text
             app.py (CLI)
                    │
                    ▼
          ExpenseManager
                    │
                    ▼
            JsonStorage
                    │
                    ▼
              expenses.json

Expense
│
├── Validation
├── Serialization
└── Type Safety
```

---

# Testing Status

Implemented:

* pytest
* Fixtures
* Parametrize
* Exception testing
* tmp_path
* CRUD tests

Tests are executed using:

```bash
python -m pytest -v
```

Coverage command:

```bash
python -m pytest --cov=expense_tracker
```

---

# Coding Standards

Continue following these rules:

* Use type hints everywhere.
* Use docstrings for public classes and methods.
* Prefer pathlib over os.path.
* Keep functions focused on one responsibility.
* Reuse existing validation utilities.
* Follow SOLID principles where appropriate.
* Avoid duplicated code.
* Write tests for every new feature.
* Explain why code is written that way.
* End every phase with an appropriate Git commit message.

---

# Next Phase

## Phase 6 – Interactive Command Line Interface (CLI)

The next phase should implement a complete menu-driven CLI.

Requirements:

* Professional terminal menu
* Add Expense
* View Expenses
* Update Expense
* Delete Expense
* Search Expenses
* Filter by Category
* View Expenses by Date
* Show Total Expenses
* Show Expense Count
* Show Latest Expense
* Exit application

CLI should:

* Validate user input
* Handle invalid choices gracefully
* Catch exceptions without crashing
* Keep UI separate from business logic
* Use ExpenseManager for all operations

Suggested structure:

* Keep `app.py` minimal.
* Create reusable helper functions for menu display and input handling if needed.
* Follow clean architecture.

Testing:

* Add appropriate tests for any helper functions where practical.
* Explain what is and isn't worth unit testing for CLI code.

---

# Future Phases

Phase 7 – Reports

* Monthly report
* Category summary
* Daily summary

Phase 8 – CSV Export

* Export expenses
* Import expenses

Phase 9 – Logging

* logging module
* Error logs
* Activity logs

Phase 10 – Custom Exceptions

* Domain-specific exceptions
* Better error handling

Phase 11 – Advanced pytest

* Mocking
* monkeypatch
* capsys
* More fixtures

Phase 12 – Test Coverage

* pytest-cov
* HTML reports

Phase 13 – Code Quality

* black
* ruff
* pre-commit

Phase 14 – GitHub Actions

* CI pipeline
* Automated testing

Phase 15 – Documentation

* Complete README
* Architecture diagrams
* Installation guide
* Usage examples

---

# Mentor Instructions

Continue the project from the current phase without repeating completed work.

For every phase:

1. Explain the design before writing code.
2. Build production-quality code.
3. Explain important Python concepts.
4. Write comprehensive pytest tests.
5. Suggest improvements where appropriate.
6. End with a Git commit message.
7. Maintain consistency with the existing architecture and coding style.
