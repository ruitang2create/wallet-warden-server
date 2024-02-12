from pydantic import BaseModel, UUID4
from typing import List
from datetime import datetime


class IncomeBase(BaseModel):
    source: str
    amount: float
    currency: str
    income_type: str
    transaction_time: datetime
    is_regular: bool
    notes: str


class CreateIncomeRequestSchema(IncomeBase):
    ...


class CreateIncomeSchema(IncomeBase):
    user_id: UUID4


class IncomeResponseSchema(IncomeBase):
    id: UUID4
    user_id: UUID4

    class Config:
        orm_mode: True


class IncomeListResponseSchema(BaseModel):
    incomes: List[IncomeResponseSchema]
