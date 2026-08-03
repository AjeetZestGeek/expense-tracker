"""Health check endpoints"""

from fastapi import APIRouter

router = APIRouter(tags=['Health'])

@router.get("/")
def root() -> dict[str, str]:
    """Root endpoint"""
    return {"message": "Welcome to Expense Tracker API"}

@router.get("/health")
def health() -> dict[str, str]:
    """Health check endenpoint."""
    return {
        "status": "healthy",
        "application": "Expense Tracker API"
    }