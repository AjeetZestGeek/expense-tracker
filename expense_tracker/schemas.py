"""Pydantic schemas used by the REST API."""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

class ExpenseCreate(BaseModel):
    """Schema used to create a new expense."""

    amount: float = Field(..., gt=0)
    category: str
    description: str
    expense_date: date

class ExpenseUpdate(BaseModel):
    """Schema used to update an expense."""

    amount: float | None = Field(default = None, gt=0)
    category: str | None = None
    description: str | None = None
    expense_date: date | None = None

class ExpenseResponse(BaseModel):
    """
    Reponse schema for an expense.
    """

    id: int
    amount: float
    category: str
    description: str
    expense_date: date

    model_config = ConfigDict(from_attribute=True)