# Expense Tracker API

A production-quality **Expense Tracker REST API** built with Python and FastAPI. The project is developed incrementally to demonstrate modern Python practices, clean architecture, REST API design, dependency injection, UUID-based resources, and comprehensive testing with pytest.

The project started as a command-line Expense Tracker and has evolved into a backend service designed to be consumed by an Angular frontend.

---

## Project Goals

* Build a maintainable Python backend.
* Practice clean architecture and separation of concerns.
* Apply SOLID principles where appropriate.
* Build RESTful APIs with FastAPI.
* Use UUIDs for stable resource identification.
* Keep business logic independent of the API layer.
* Write comprehensive automated tests with pytest.
* Prepare the backend for future Angular integration.
* Eventually migrate persistence from JSON to a relational database.

---

# Technology Stack

## Backend

* Python 3.12+
* FastAPI
* Uvicorn
* Pydantic
* Dataclasses
* UUID
* JSON
* pathlib
* datetime

## Testing

* pytest
* pytest-cov
* FastAPI TestClient

## Planned Technologies

* SQLAlchemy
* PostgreSQL
* Angular
* TypeScript
* Docker
* GitHub Actions
* Ruff
* Black
* pre-commit

---

# Architecture

```text
                         Angular
                       (Upcoming)
                           │
                      HTTP / JSON
                           │
                           ▼
                    FastAPI Routers
                           │
                  Dependency Injection
                           │
                           ▼
                    ExpenseManager
                   Business Layer
                           │
                           ▼
                     JsonStorage
                  Persistence Layer
                           │
                           ▼
                    expenses.json
```

### Layer Responsibilities

### API Layer

Responsible for:

* HTTP requests
* Request validation
* Response serialization
* HTTP status codes
* Routing
* API documentation

### Business Layer

Responsible for:

* Expense operations
* Searching
* Filtering
* Updating
* Deleting
* Aggregation
* Business rules

### Persistence Layer

Responsible for:

* Reading data
* Writing data
* JSON persistence
* Storage-related errors

The layers remain independent so that the persistence mechanism or API framework can change without rewriting the business logic.

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
│   ├── schemas.py
│   ├── utils.py
│   ├── report.py
│   ├── logger.py
│   ├── exceptions.py
│   │
│   └── api/
│       ├── __init__.py
│       ├── dependencies.py
│       ├── mappers.py
│       │
│       └── routes/
│           ├── __init__.py
│           ├── health.py
│           └── expenses.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_utils.py
│   ├── test_storage.py
│   ├── test_manager.py
│   └── test_api.py
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

## Phase 1 — Project Setup ✅

Implemented:

* Project structure
* Virtual environment
* requirements.txt
* pytest configuration
* .gitignore
* Git repository
* Python package structure

Learned:

* Python packages
* Virtual environments
* Project organization

---

## Phase 2 — Expense Model ✅

Implemented:

* Expense dataclass
* Type hints
* Validation
* `to_dict()`
* `from_dict()`
* `__str__()`

Learned:

* Dataclasses
* `__post_init__`
* Serialization
* Deserialization

---

## Phase 3 — Validation Utilities ✅

Implemented:

* `validate_amount()`
* `validate_category()`
* `validate_description()`
* `validate_date()`

Learned:

* Separation of Concerns
* Single Responsibility Principle
* Reusable validation

---

## Phase 4 — JSON Storage ✅

Implemented:

* `JsonStorage`
* `load()`
* `save()`
* Missing-file handling
* Invalid JSON handling
* `StorageError`
* pathlib-based file operations

Learned:

* Persistence layers
* JSON
* File handling
* Exception handling

---

## Phase 5 — Expense Manager ✅

Implemented:

* `add_expense()`
* `get_all_expenses()`
* `get_expense_by_id()`
* `update_expense()`
* `delete_expense()`
* `search_expenses()`
* `filter_by_category()`
* `expenses_by_date()`
* `total_expenses()`
* `count_expenses()`
* `latest_expense()`

Learned:

* Service Layer pattern
* CRUD
* Business logic
* Aggregation
* UUID-based resource management

---

# Phase 6 — FastAPI REST API ✅

## FastAPI Foundation

Implemented:

* FastAPI application
* Uvicorn
* APIRouter
* Dependency Injection
* Pydantic schemas
* API mapper layer
* Swagger/OpenAPI
* ReDoc

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## UUID Migration ✅

Expenses now use stable UUID identifiers instead of list indexes.

Example:

```json
{
  "id": "b372f0ef-f27f-4e61-8cd5-ad599010620b",
  "amount": 250,
  "category": "Food",
  "description": "Lunch at restaurant",
  "expense_date": "2026-08-01"
}
```

This prevents resource identifiers from changing when expenses are deleted or reordered.

---

## CRUD API

| Method | Endpoint                 | Purpose          |
| ------ | ------------------------ | ---------------- |
| GET    | `/expenses`              | Get all expenses |
| GET    | `/expenses/{expense_id}` | Get one expense  |
| POST   | `/expenses`              | Create expense   |
| PUT    | `/expenses/{expense_id}` | Update expense   |
| DELETE | `/expenses/{expense_id}` | Delete expense   |

All CRUD endpoints are implemented using UUID-based resource identification.

---

# Phase 7 — Query & Summary APIs ✅

Phase 7 adds search, filtering, and dashboard-oriented summary endpoints.

## Search

```http
GET /expenses/search?q=Lunch
```

Searches expense category and description.

---

## Category Filter

```http
GET /expenses/category/Food
```

Returns expenses belonging to the specified category.

---

## Date Filter

```http
GET /expenses/date/2026-08-05
```

Returns expenses for a specific date.

FastAPI automatically validates and converts the path parameter into a Python `date`.

---

## Total Expenses

```http
GET /expenses/total
```

Example response:

```json
{
  "total": 10668.0
}
```

---

## Expense Count

```http
GET /expenses/count
```

Example response:

```json
{
  "count": 10
}
```

---

## Latest Expense

```http
GET /expenses/latest
```

Returns the most recent expense based on `expense_date`.

If no expenses exist:

```http
404 Not Found
```

```json
{
  "detail": "No expenses found"
}
```

---

# Current API

| Method | Endpoint                        | Status |
| ------ | ------------------------------- | ------ |
| GET    | `/`                             | ✅      |
| GET    | `/health`                       | ✅      |
| GET    | `/expenses`                     | ✅      |
| POST   | `/expenses`                     | ✅      |
| GET    | `/expenses/{expense_id}`        | ✅      |
| PUT    | `/expenses/{expense_id}`        | ✅      |
| DELETE | `/expenses/{expense_id}`        | ✅      |
| GET    | `/expenses/search?q=`           | ✅      |
| GET    | `/expenses/category/{category}` | ✅      |
| GET    | `/expenses/date/{date}`         | ✅      |
| GET    | `/expenses/total`               | ✅      |
| GET    | `/expenses/count`               | ✅      |
| GET    | `/expenses/latest`              | ✅      |

---

# Important API Design Decisions

## UUID Instead of List Index

The API originally used list indexes as identifiers.

That was changed to UUIDs because indexes are not stable.

```text
Old:

/expenses/2


Current:

/expenses/b372f0ef-f27f-4e61-8cd5-ad599010620b
```

---

## Dependency Injection

FastAPI provides the `ExpenseManager` through:

```python
Depends(get_expense_manager)
```

This keeps endpoint functions independent from object construction and makes testing easier.

---

## Domain Model vs API Schema

The internal `Expense` dataclass is separate from Pydantic API schemas.

```text
Expense
   │
   ▼
API Mapper
   │
   ▼
ExpenseResponse
```

This prevents the external API contract from becoming tightly coupled to the internal domain model.

---

## API Layer vs Business Layer

The business layer does not raise FastAPI-specific exceptions.

For example:

```text
ExpenseManager
      │
      ├── Expense found → Expense
      │
      └── Not found → None
```

The API layer translates that result into:

```text
None
 ↓
HTTP 404
```

This keeps the business layer reusable.

---

# Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn expense_tracker.app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# Running Tests

Run all tests:

```bash
python -m pytest -v
```

Run with coverage:

```bash
python -m pytest --cov=expense_tracker
```

---

# Coding Standards

The project follows:

* Type hints
* Public docstrings
* SOLID principles
* Separation of Concerns
* Single Responsibility Principle
* DRY
* RESTful API design
* Dependency Injection
* Reusable validation
* Automated testing
* Clean architecture

---

# Next Phase

## Phase 8 — Test & API Quality

Before starting Angular integration, the backend will go through a quality and testing phase.

Planned work:

* Improve API fixtures
* Isolate tests from real `expenses.json`
* Test API success cases
* Test 404 cases
* Test validation errors
* Test UUID handling
* Test query endpoints
* Improve test coverage
* Review API response contracts

After the API is stable, we can begin the Angular frontend.

---

# Future Roadmap

## Phase 9 — Reports

* Monthly report
* Category summary
* Daily summary
* Date-range reports

## Phase 10 — CSV

* Export expenses
* Import expenses

## Phase 11 — Logging

* Application logging
* Error logging
* Activity logging

## Phase 12 — Database

* Repository abstraction
* SQLAlchemy
* PostgreSQL
* Database migrations

## Phase 13 — Authentication

* User registration
* Login
* JWT authentication
* Authorization

## Phase 14 — Angular Frontend

* Angular application
* Expense dashboard
* Expense list
* Add expense
* Edit expense
* Delete expense
* Search
* Filters
* Reports
* Charts

## Phase 15 — Code Quality & DevOps

* Ruff
* Black
* pre-commit
* GitHub Actions
* Docker
* CI/CD

---

# Long-Term Vision

The final goal is a full-stack expense management application demonstrating:

* Modern Python
* FastAPI
* REST API design
* Angular
* TypeScript
* Clean Architecture
* SOLID principles
* Dependency Injection
* Automated testing
* Database integration
* Authentication
* CI/CD
* Production deployment

The application is intentionally developed incrementally so each architectural decision and technology can be understood before moving to the next stage.
