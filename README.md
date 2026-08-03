# Expense Tracker (Python + FastAPI)

A production-quality **Expense Tracker** project built incrementally to demonstrate modern Python development practices, clean architecture, REST API development, and comprehensive testing with **pytest**.

The project started as a Python application with a service layer and JSON persistence and is now evolving into a **FastAPI REST API** that will later be consumed by an **Angular frontend**.

---

# Project Goals

* Write clean, maintainable Python code.
* Follow SOLID principles and Clean Architecture.
* Build a reusable business layer independent of the presentation layer.
* Practice Test-Driven Development (TDD) with `pytest`.
* Build a REST API using FastAPI.
* Integrate the backend with an Angular frontend.
* Prepare the project for future migration to a database without changing business logic.

---

# Technology Stack

## Current

### Backend

* Python 3.12+
* FastAPI
* Uvicorn
* Pydantic
* JSON
* pathlib
* dataclasses
* typing
* datetime

### Testing

* pytest
* pytest-cov
* FastAPI TestClient (planned)

## Future

### Backend

* SQLite / PostgreSQL
* SQLAlchemy
* Logging
* CSV Import / Export
* Docker

### Frontend

* Angular
* Angular Material
* TypeScript

### Tooling

* Ruff
* Black
* pre-commit
* GitHub Actions

---

# Current Project Structure

```text
expense-tracker/

│
├── expense_tracker/
│   ├── __init__.py
│   ├── app.py
│   ├── manager.py
│   ├── models.py
│   ├── storage.py
│   ├── schemas.py
│   ├── utils.py
│   ├── exceptions.py
│   ├── report.py
│   ├── logger.py
│   │
│   └── api/
│       ├── __init__.py
│       ├── dependencies.py
│       ├── mappers.py
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
│   └── test_api.py (planned)
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

# Architecture

```text
                 Angular (Upcoming)
                        │
                  HTTP / JSON
                        │
                        ▼
                 FastAPI Routers
                        │
                        ▼
                ExpenseManager
             (Business / Service Layer)
                        │
                        ▼
                 JsonStorage
             (Persistence Layer)
                        │
                        ▼
                 expenses.json
```

## Layer Responsibilities

### API Layer

Responsible for:

* HTTP requests
* Request validation
* Response serialization
* Status codes
* Routing

### Business Layer

Responsible for:

* Expense operations
* Validation
* Search
* Filtering
* Aggregation

### Persistence Layer

Responsible for:

* Reading JSON
* Writing JSON
* Storage-related exceptions

Each layer has a single responsibility and can evolve independently.

---

# Completed Phases

## ✅ Phase 1 — Project Setup

Completed

* Project structure
* Virtual environment
* Git initialization
* Package organization
* pytest configuration
* .gitignore

Concepts

* Python packages
* Virtual environments
* Project organization

---

## ✅ Phase 2 — Expense Model

Implemented

* Expense dataclass
* Validation
* Serialization
* `to_dict()`
* `from_dict()`
* `__str__()`

Concepts

* Dataclasses
* `__post_init__`
* Object serialization

---

## ✅ Phase 3 — Validation Utilities

Implemented

* `validate_amount()`
* `validate_category()`
* `validate_description()`
* `validate_date()`

Concepts

* Reusable validation
* Single Responsibility Principle
* Separation of Concerns

---

## ✅ Phase 4 — JSON Storage

Implemented

* JsonStorage
* `load()`
* `save()`

Features

* JSON persistence
* Missing file handling
* Corrupted JSON handling
* StorageError

Concepts

* Persistence Layer
* File handling
* Exception handling

---

## ✅ Phase 5 — Expense Manager

Implemented

* Add Expense
* View Expenses
* Update Expense
* Delete Expense
* Search
* Filter by category
* Expenses by date
* Total expenses
* Expense count
* Latest expense

Concepts

* Service Layer Pattern
* CRUD operations
* Business logic
* Aggregation

---

## ✅ Phase 6 — FastAPI Foundation (Current)

Implemented

### FastAPI

* FastAPI application setup
* Uvicorn configuration
* Automatic Swagger documentation
* OpenAPI generation

### API Architecture

* API package
* Router-based architecture
* Dependency Injection
* Shared dependencies
* API mapper layer

### Endpoints

* `GET /`
* `GET /health`
* `GET /expenses`
* `POST /expenses`

### API Models

* ExpenseCreate
* ExpenseUpdate
* ExpenseResponse

Concepts Learned

* REST APIs
* APIRouter
* Dependency Injection
* Request/Response schemas
* Pydantic models
* Response models
* HTTP status codes
* OpenAPI
* Separation of domain models and API models

---

# Current API

| Method | Endpoint                        | Status      |
| ------ | ------------------------------- | ----------- |
| GET    | `/`                             | ✅ Completed |
| GET    | `/health`                       | ✅ Completed |
| GET    | `/expenses`                     | ✅ Completed |
| POST   | `/expenses`                     | ✅ Completed |
| GET    | `/expenses/{id}`                | ⏳ Planned   |
| PUT    | `/expenses/{id}`                | ⏳ Planned   |
| DELETE | `/expenses/{id}`                | ⏳ Planned   |
| GET    | `/expenses/search`              | ⏳ Planned   |
| GET    | `/expenses/category/{category}` | ⏳ Planned   |
| GET    | `/expenses/date/{date}`         | ⏳ Planned   |
| GET    | `/expenses/total`               | ⏳ Planned   |
| GET    | `/expenses/count`               | ⏳ Planned   |
| GET    | `/expenses/latest`              | ⏳ Planned   |

---

# Running the Application

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn expense_tracker.app:app --reload
```

Open Swagger

```text
http://127.0.0.1:8000/docs
```

Open ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# Running Tests

Run all tests

```bash
python -m pytest -v
```

Run with coverage

```bash
python -m pytest --cov=expense_tracker
```

---

# Coding Standards

The project follows these principles:

* Clean Architecture
* SOLID Principles
* Type hints everywhere
* Public docstrings
* Small, focused functions
* Separation of Concerns
* Reusable validation
* Comprehensive testing

---

# Next Phase

The next milestone focuses on completing the REST API.

## Planned Work

* Stable unique expense IDs
* GET expense by ID
* Update expense endpoint
* Delete expense endpoint
* Search endpoint
* Category filter endpoint
* Date filter endpoint
* Total endpoint
* Count endpoint
* Latest expense endpoint
* FastAPI TestClient integration
* API unit tests

---

# Future Roadmap

## Backend

* SQLAlchemy integration
* SQLite/PostgreSQL support
* Authentication & Authorization
* Logging
* CSV Import/Export

## Frontend

* Angular application
* Expense Dashboard
* CRUD interface
* Charts and Reports

## DevOps

* Ruff
* Black
* pre-commit
* GitHub Actions
* Docker

---

# Long-Term Vision

The goal of this project is to become a production-quality full-stack application demonstrating:

* Clean Architecture
* REST API Design
* FastAPI
* Automated Testing
* Angular Integration
* Modern Python Best Practices
* Scalable Software Design

The project is intentionally built in small phases so each concept can be understood before moving to the next, resulting in a maintainable, interview-ready, and portfolio-quality application.
