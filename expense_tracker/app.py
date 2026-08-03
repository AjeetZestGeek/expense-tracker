"""Application entry point for the Expense Tracker API."""

from fastapi import FastAPI

from expense_tracker.api.routes.health import router as health_router
from expense_tracker.api.routes.expenses import router as expense_router

app = FastAPI(
    title="Expense Tracker API",
    description="REST API for managing expenses.",
    version="1.0.0",
)

app.include_router(expense_router)
