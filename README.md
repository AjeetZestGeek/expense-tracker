# Expense Tracker API (Python + FastAPI)

A production-quality Expense Tracker built incrementally to demonstrate modern Python development, clean architecture, REST API design, and comprehensive testing using **pytest**.

The project follows a layered architecture where the API layer, business logic, and persistence layer are completely separated, making the application maintainable and easy to extend.

---

# Features

## Expense Management

* Create Expense
* View All Expenses
* View Expense by UUID
* Update Expense
* Delete Expense
* Search Expenses *(Upcoming)*
* Filter by Category *(Upcoming)*
* Filter by Date *(Upcoming)*
* Total Expenses *(Upcoming)*
* Expense Count *(Upcoming)*
* Latest Expense *(Upcoming)*

---

# Technology Stack

## Backend

* Python 3.13+
* FastAPI
* Uvicorn
* Pydantic v2
* Dataclasses
* UUID
* JSON Storage
* pathlib

## Testing

* pytest
* pytest-cov
* FastAPI TestClient

## Future

* SQLAlchemy
* PostgreSQL
* Docker
* GitHub Actions
* Ruff
* Black
* Angular Frontend

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
                    Dependency Injection
                               │
                               ▼
                      ExpenseManager
                    (Business Logic)
                               │
                               ▼
                        JsonStorage
                      (Persistence)
                               │
                               ▼
                        expenses.json
```

---

# Project Structure

```text
expense-tracker/

expense_tracker/
│
├── api/
│   ├── dependencies.py
│   ├── mappers.py
│   └── routes/
│       ├── health.py
│       └── expenses.py
│
├── app.py
├── exceptions.py
├── manager.py
├── models.py
├── report.py
├── schemas.py
├── storage.py
└── utils.py

tests/

data/
```

---

# Current REST API

| Method | Endpoint                 | Status |
| ------ | ------------------------ | ------ |
| GET    | `/`                      | ✅      |
| GET    | `/health`                | ✅      |
| GET    | `/expenses`              | ✅      |
| GET    | `/expenses/{expense_id}` | ✅      |
| POST   | `/expenses`              | ✅      |
| PUT    | `/expenses/{expense_id}` | ✅      |
| DELETE | `/expenses/{expense_id}` | ✅      |

---

# UUID Based Resources

Every expense now owns a stable UUID.

Example:

```json
{
    "id": "b372f0ef-f27f-4e61-8cd5-ad599010620b",
    "amount": 250,
    "category": "Food",
    "description": "Lunch",
    "expense_date": "2026-08-07"
}
```

Using UUIDs instead of list indexes makes the API production-ready and prevents identifiers from changing when expenses are deleted.

---

# Design Principles

* Clean Architecture
* SOLID Principles
* Single Responsibility Principle
* Dependency Injection
* Separation of Concerns
* RESTful API Design
* Reusable Business Logic
* Type Hints
* Public Docstrings

---

# Completed Phases

## Phase 1

* Project Setup

## Phase 2

* Expense Dataclass

## Phase 3

* Validation Utilities

## Phase 4

* JSON Storage

## Phase 5

* Expense Manager

## Phase 6

### FastAPI

* FastAPI initialization
* Router architecture
* Swagger/OpenAPI
* Dependency Injection
* Request/Response Schemas
* API Mappers

### CRUD APIs

* GET All Expenses
* GET Expense by UUID
* POST Expense
* PUT Expense
* DELETE Expense

### UUID Migration

* UUID-based Expense model
* UUID serialization
* UUID deserialization
* UUID API responses
* UUID service layer

---

# Running the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn expense_tracker.app:app --reload
```

Swagger

```text
http://127.0.0.1:8000/docs
```

ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# Running Tests

```bash
python -m pytest -v
```

Coverage

```bash
python -m pytest --cov=expense_tracker
```

---

# Next Milestone

Phase 7 – Query & Reporting APIs

* Search Expenses
* Category Filter
* Date Filter
* Total Expenses
* Expense Count
* Latest Expense
* Monthly Report
* Category Summary

---

# Long-Term Roadmap

* SQLAlchemy Repository
* PostgreSQL
* Authentication & Authorization
* Angular Frontend
* Charts & Dashboard
* Docker
* GitHub Actions
* CI/CD
* Production Deployment

---

# Learning Outcomes

This project demonstrates:

* Modern Python
* FastAPI
* REST API Design
* UUID-based Resources
* Layered Architecture
* Service Layer Pattern
* Dependency Injection
* JSON Persistence
* API Validation
* Automated Testing
* Production-Oriented Development
